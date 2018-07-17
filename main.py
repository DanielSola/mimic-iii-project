"""
MIMIC-III Project
@author: Daniel Solá
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath('__file__')));
import pandas as pd
from get_features import *
from get_labels import *
from services.neural_network_service import *
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score

#Extraction of features
categorical_features = Features().get_categorical_features();
numerical_features = Features().get_numerical_features();
#Prepare features to neural network
numerical_features_to_nn = NeuralNetworkService().prepare_numerical_features(numerical_features);
categorical_features_to_nn = NeuralNetworkService().hot_encode_categorical_features(categorical_features);

#Extraction of readmission label
patient_outcomes = PatientOutcomes().get_patient_outcomes().set_index('hadm_id');
patient_outcomes.set_index('hadm_id', drop = True, inplace = True);
label = pd.DataFrame(patient_outcomes.readmission);

#Matching features and label by hadm_id
features = pd.merge(categorical_features_to_nn, numerical_features_to_nn, left_index = True, right_index = True, how = 'inner');
data = pd.merge(features, label, left_index = True, right_index = True, how = 'inner').dropna();

#Spliting of data in test / train sets
features = data.loc[:, 'F':'total_mech_vent_time'];
labels = pd.DataFrame(data.readmission);
hot_encoded_label = pd.get_dummies(labels);
X_train, X_test, y_train, y_test = train_test_split(features, hot_encoded_label, test_size=0.075, random_state=42)


# Prediciton of readmission labels (no-readmission, 0-6 months, 6+ months):
model = Sequential()
model.add(Dense(12, activation='relu', input_shape=(102,)))
model.add(Dense(8, activation='relu'))
model.add(Dense(3, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(X_train, y_train,epochs=3, batch_size=1, verbose=1)

#Evaluating model
y_pred = model.predict(X_test);
score = model.evaluate(X_test, y_test,verbose=1)

#Precision: 0.854 % , Loss: 0.356 





