# -*- coding: utf-8 -*-
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
from keras.layers import Dense
from keras.models import Sequential
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score, roc_auc_score

#Extraction of features
features = Features().get_nn_features();
categorical_labels = PatientOutcomes().get_categorical_outcomes();
label = pd.DataFrame(categorical_labels.readmission);
data = pd.merge(features, label, left_index = True, right_index = True, how = 'inner').dropna();
#Spliting of data in test / train sets
features = data.loc[:, 'F':'total_mech_vent_time'];
label = data.readmission;
hot_encoded_label = pd.get_dummies(label);


X_train, X_test, y_train, y_test = train_test_split(features, hot_encoded_label, test_size=0.075, random_state=42)


# Prediciton of readmission labels (no-readmission, 0-6 months, 6+ months):
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(102,)))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(3, activation='sigmoid'))
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
model.fit(X_train, y_train,epochs=3, batch_size=1, verbose=1)

#Evaluating model
y_pred = model.predict(X_test);
score = model.evaluate(X_test, y_test,verbose=1)
roc_score = roc_auc_score(y_test, y_pred);

#ROC_AUC_SCORE = 0.778