# -*- coding: utf-8 -*-

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from features.get_features import *
from labels.get_labels import *
from sklearn.model_selection import train_test_split

def get_nn_data():
    
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
    readmission = PatientOutcomes().get_readmissions().set_index('hadm_id');
    
    #Merging of features and labels
    mortality_data = pd.merge(features, mortality, left_index = True, right_index = True, how = 'inner').dropna();
    readmission_data = pd.merge(features, readmission, left_index = True, right_index = True, how = 'inner').dropna();
    
    #Hot encoding of labels
    hot_encoded_mortality = pd.get_dummies(mortality_data.mortality);
    hot_encoded_readmissions = pd.get_dummies(readmission_data.readmission);
    
    #Spliting of data in test / train sets
    mortality_features = mortality_data.loc[:, 'F':'total_mech_vent_time'];
    readmissions_features = readmission_data.loc[:, 'F':'total_mech_vent_time'];
    
    X_train_mortality, X_test_mortality, Y_train_mortality, Y_test_mortality = train_test_split(mortality_features, hot_encoded_mortality, test_size=0.075, random_state=42);
    X_train_readmission, X_test_readmission, Y_train_readmission, Y_test_readmission = train_test_split(mortality_features, hot_encoded_mortality, test_size=0.075, random_state=42);
    
    return { 'mortality_data' : {'X_train':X_train_mortality,'X_test': X_test_mortality,'Y_train': Y_train_mortality, 'Y_test':Y_test_mortality },
             'readmission_data':  {'X_train':X_train_readmission,'X_test': X_test_readmission,'Y_train': Y_train_readmission, 'Y_test':Y_test_mortality }};
            

        