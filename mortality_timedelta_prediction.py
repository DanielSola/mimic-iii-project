# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 22:08:39 2018

@author: Daniel
"""

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
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score, r2_score, roc_auc_score
import seaborn as sns
#Extraction of features
features = Features().get_nn_features();
numerical_labels = PatientOutcomes().get_numerical_outcomes();
label = pd.DataFrame(numerical_labels.expire_days);
data = pd.merge(features, label, left_index = True, right_index = True, how = 'inner').dropna();
#Spliting of data in test / train sets
features = data.loc[:, 'F':'total_mech_vent_time'];
scaled_label = preprocessing.scale(data.expire_days);
X_train, X_test, y_train, y_test = train_test_split(features, scaled_label, test_size=0.075, random_state=42)

# Prediciton of readmission labels (no-readmission, 0-6 months, 6+ months):
model = Sequential()
model.add(Dense(64, activation='relu', input_shape=(102,)))
model.add(Dense(64, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(loss='mse',
              optimizer='adam',
               metrics=['mse','mae'])
model.fit(X_train, y_train,epochs=10, batch_size=1, verbose=1)

#Evaluating model
y_pred = model.predict(X_test);
score = model.evaluate(X_test, y_test,verbose=1)
r2 = r2_score(y_test, y_pred);
#R2 score = 0.191