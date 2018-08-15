"""
MIMIC-III Project
@author: Daniel Solá
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath('__file__')));
import pandas as pd
from features.get_features import *
from labels.get_labels import *
from neural_network import get_neural_network_data
from services.query_service import *
from services.plotting_service import *
from keras.layers import Dense
from keras.models import Sequential
from neural_network import *
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, cohen_kappa_score, roc_auc_score
import time

nn_data =  get_neural_network_data.get_nn_data();

X_train = nn_data['mortality_data']['X_train'];
X_test = nn_data['mortality_data']['X_test'];
Y_train = nn_data['mortality_data']['Y_train'];
Y_test = nn_data['mortality_data']['Y_test'];

layers_array = [3, 4, 5, 6];
neurons_array = [8, 16, 32];
epochs_array = [1, 5, 10, 15];
batch_sizes_array = [32, 64, 128];


def train_neural_newtork(X_train, Y_train, X_test, Y_test, n_layers, n_neurons, epochs, batch_size):    
    model = Sequential();
    for i in range(n_layers):
        model.add(Dense(n_neurons, activation='relu', input_shape=(101,)))
    model.add(Dense(3, activation='softmax'));
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy', 'mse'])
    start_time = time.time();
    model.fit(X_train, Y_train,epochs=epochs, batch_size=batch_size, verbose=0);
    elapsed_time = time.time() - start_time;
    #Evaluating model
    Y_pred = model.predict(X_test);
    loss, accuracy, mse = model.evaluate(X_test, Y_test,verbose=0)
    roc_auroc = roc_auc_score(Y_test, Y_pred);
    return loss, accuracy, mse, roc_auroc, elapsed_time;

#Hyperparameter tuning
metrics = [];
for layer in layers_array:
    for neurons in neurons_array:
        for epochs in epochs_array:
            for batch_size in batch_sizes_array:
                print('Fitting model... layers:', layer, 'neurons:', neurons, 'epochs:', epochs, 'batch_size:', batch_size);
                loss, accuracy, mse, roc_auroc, elapsed_time = train_neural_newtork(X_train, Y_train, X_test, Y_test, 2, 2, 1, 1);
                setting_metrics = {'n_layers': layer,
                                    'n_neurons': neurons,
                                    'n_epochs': epochs,
                                    'batch_size': batch_size,
                                    'loss': loss,
                                    'accuracy': accuracy,
                                    'mean_squared_error': mse,
                                    'roc_auroc': roc_auroc,
                                    'elapsed_time': elapsed_time}
                print('Loss:',round(loss,3),'Accuracy:',round(accuracy,3),'MSE:',round(mse,3),'AUROC:', round(roc_auroc,3), 'Time:', round(elapsed_time,3));
                metrics.append(setting_metrics);
      
metrics_df = pd.DataFrame(metrics);
        
##loss, accuracy, mse, roc_auroc, elapsed_time = train_neural_newtork(X_train, Y_train, X_test, Y_test, 2, 2, 1, 1);


