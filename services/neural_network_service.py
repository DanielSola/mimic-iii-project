# -*- coding: utf-8 -*-

import pandas as pd
from features.get_features import *
from labels.get_labels import *
from sklearn.model_selection import train_test_split
from keras.layers import Dense
from keras.models import Sequential
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, log_loss, f1_score, mean_squared_error, roc_auc_score, accuracy_score
from services.preprocessing_service import *

class NeuralNetworkService():
    
    def get_nn_data(self):
    
        #Extraction, filtering and preparation of numerical features
        numerical_features = Features().get_numerical_features();
        filtered_numerical_features = numerical_features.query('age > 18 & age < 95');
        numerical_features_to_nn = preprocessing_service.prepare_numerical_features(filtered_numerical_features);
    
        #Extraction, filtering and preparation of categorical features
        categorical_features = Features().get_categorical_features();
        categorical_features_to_nn = preprocessing_service.hot_encode_categorical_features(categorical_features);       
    
        #Merging of numerical and categorical features
        features = pd.merge(categorical_features_to_nn, numerical_features_to_nn, left_index = True, right_index = True, how = 'inner');
    
        #Extraction of labels
        mortality = PatientOutcomes().get_mortality().set_index('hadm_id');
    
        #Merging of features and labels
        mortality_data = pd.merge(features, mortality, left_index = True, right_index = True, how = 'inner').dropna();
    
        #Hot encoding of labels
        hot_encoded_mortality = pd.get_dummies(mortality_data.mortality);
    
        #Spliting of data in test / train sets
        mortality_features = mortality_data.loc[:, 'F':'total_mech_vent_time'];
    
        X_train_mortality, X_test_mortality, Y_train_mortality, Y_test_mortality = train_test_split(mortality_features, hot_encoded_mortality, test_size=0.075, random_state=42);
    
        return { 'mortality_data' : {'X_train':X_train_mortality,'X_test': X_test_mortality,'Y_train': Y_train_mortality, 'Y_test':Y_test_mortality }};
            

    
    def train_neural_network(self, X_train, Y_train, X_test, Y_test, params):
        print(params);
        n_layers = params['n_layers'];
        n_neurons = params['n_neurons'];
        batch_size = params['batch_size'];
        epochs = params['epochs'];
        optimizer = params['optimizer'];
    
        model = Sequential();
        for i in range(n_layers):
            model.add(Dense(n_neurons, activation='relu', input_shape=(101,)))
        model.add(Dense(3, activation='softmax'));
        model.compile(loss='binary_crossentropy',
                  optimizer=optimizer,
                  metrics=['accuracy', 'mse'])
        model.fit(X_train, Y_train,epochs=epochs, batch_size=batch_size, verbose=1);
        #Evaluating model
        Y_pred = model.predict(X_test);
        Y_train_pred = pd.get_dummies(model.predict(X_train).argmax(axis = 1));
        Y_test_pred = pd.get_dummies(Y_pred.argmax(axis = 1));
        #Train and test accuracies
        train_accuracy = accuracy_score(Y_train, Y_train_pred);
        test_accuracy = accuracy_score(Y_test, Y_test_pred);
        f1_score_model = f1_score(Y_test_pred, Y_test, average = 'samples');
        loss, accuracy, mse = model.evaluate(X_test, Y_test,verbose=0)
        roc_auroc = roc_auc_score(Y_test, Y_pred);
        print('TRAIN ACCURACY:',train_accuracy, 'TEST ACCURACY:',test_accuracy,'F1 SCORE:', f1_score_model,'LOSS:', loss, 'MSE:',mse, 'AUROC:', roc_auroc);
        return model;

    def preprocess_prediction_data(self, patient_features, imputed_numerical_features, categorical_features):
    
        patient_categorical_features = patient_features['patient_categorical_features'];
        patient_lab_tests = patient_features['patient_lab_tests'];
        patient_numerical_features = patient_features['patient_numerical_features'];
        patient_physio_measures = patient_features['patient_physio_measures'];
    
        #Get Average and STD of patient data
        treated_physio_measures = self.get_physio_avg_std(patient_physio_measures);
        treated_lab_tests = self.get_lab_avg_std(patient_lab_tests);

        #Appending of patient categorical features
        patient_categorical_features_df = pd.DataFrame.from_dict(patient_categorical_features, orient = 'index').T;
        categorical_features_with_patient =  categorical_features.append(patient_categorical_features_df, sort=False);

        #Appending of patient numerical features
        all_patient_numerical_features = {}
        all_patient_numerical_features.update(patient_numerical_features);
        all_patient_numerical_features.update(treated_lab_tests);
        all_patient_numerical_features.update(treated_physio_measures);
        all_patient_numerical_features_df = pd.DataFrame.from_dict(all_patient_numerical_features, orient = 'index').T
        numerical_features_with_patient = imputed_numerical_features.append(all_patient_numerical_features_df, sort=False);

        if all_patient_numerical_features_df.isnull().values.any():
            numerical_features_with_patient = impute_missing_values(numerical_features_with_patient);
            
        #Prepreprocess categorical and numerical data for use in neural network
        numerical_features_to_nn = preprocessing_service.scale_numerical_features(numerical_features_with_patient);
        categorical_features_to_nn = preprocessing_service.hot_encode_categorical_features(categorical_features_with_patient);       

        return pd.DataFrame(pd.merge(categorical_features_to_nn, numerical_features_to_nn, left_index = True, right_index = True, how = 'inner').ix[0]).T;

    def get_physio_avg_std(self, patient_physio_measures):
        return {'avg_hr':np.mean(patient_physio_measures['heart_rate']),
                           'std_hr':np.std(patient_physio_measures['heart_rate']),
                           'avg_resp_rate':np.mean(patient_physio_measures['resp_rate']),
                           'std_resp_rate':np.std(patient_physio_measures['resp_rate']),
                           'avg_sys_press':np.mean(patient_physio_measures['sys_press']),
                           'std_sys_press':np.std(patient_physio_measures['sys_press']),
                           'avg_dias_press':np.mean(patient_physio_measures['dias_press']),
                           'std_dias_press':np.std(patient_physio_measures['dias_press']),
                           'avg_temp':np.mean(patient_physio_measures['temp']),
                           'std_temp':np.std(patient_physio_measures['temp']),
                           'avg_spo2':np.mean(patient_physio_measures['spo2']),
                           'std_spo2':np.std(patient_physio_measures['spo2'])
                           };
    
    def get_lab_avg_std(self, patient_lab_tests):
        return {'avg_blood_urea_nitrogen': np.mean(patient_lab_tests['blood_urea_nitrogen']),
                     'std_blood_urea_nitrogen': np.std(patient_lab_tests['blood_urea_nitrogen']),
                     'avg_platelet_count': np.mean(patient_lab_tests['platelet_count']),
                     'std_platelet_count': np.std(patient_lab_tests['platelet_count']),
                     'avg_hematrocrit':np.mean(patient_lab_tests['hematocrit']),
                     'std_hematrocrit':np.std(patient_lab_tests['hematocrit']),
                     'avg_potasssium':np.mean(patient_lab_tests['potassium']),
                     'std_potasssium':np.std(patient_lab_tests['potassium']),
                     'avg_sodium':np.mean(patient_lab_tests['sodium']),
                     'std_sodium':np.std(patient_lab_tests['sodium']),
                     'avg_creatinine':np.mean(patient_lab_tests['creatinine']),
                     'std_creatinine':np.std(patient_lab_tests['creatinine']),
                     'avg_bicarbonate':np.mean(patient_lab_tests['bicarbonate']),
                     'std_bicarbonate':np.std(patient_lab_tests['bicarbonate']),
                     'avg_white_blood_cells':np.mean(patient_lab_tests['white_blood_cells']),
                     'std_white_blood_cells':np.std(patient_lab_tests['white_blood_cells']),
                     'avg_blood_glucose':np.mean(patient_lab_tests['blood_glucose']),
                     'std_blood_glucose':np.std(patient_lab_tests['blood_glucose']),
                     'avg_albumin':np.mean(patient_lab_tests['albumin']),
                     'std_albumin':np.std(patient_lab_tests['albumin'])
                     };