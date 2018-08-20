"""
MIMIC-III Project
@author: Daniel Solá
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath('__file__')));
import pandas as pd
from neural_network import get_neural_network_data
from keras.layers import Dense
from keras.models import Sequential
from sklearn.metrics import confusion_matrix, precision_score, recall_score, log_loss, f1_score, mean_squared_error, roc_auc_score, accuracy_score
import time
from keras.optimizers import SGD, Adam, RMSprop, Adagrad
from hyperopt import hp, Trials, fmin, tpe

nn_data =  get_neural_network_data.get_nn_data();

X_train = nn_data['mortality_data']['X_train'];
X_test = nn_data['mortality_data']['X_test'];
Y_train = nn_data['mortality_data']['Y_train'];
Y_test = nn_data['mortality_data']['Y_test'];

def train_neural_newtork(X_train, Y_train, X_test, Y_test, params):
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
    start_time = time.time();
    model.fit(X_train, Y_train,epochs=epochs, batch_size=batch_size, verbose=0);
    elapsed_time = time.time() - start_time;
    #Evaluating model
    Y_pred = model.predict(X_test);
    Y_train_pred = pd.get_dummies(model.predict(X_train).argmax(axis = 1));
    Y_test_pred = pd.get_dummies(Y_pred.argmax(axis = 1));
    #Train and test accuracies
    #train_accuracy = accuracy_score(Y_train, Y_train_pred);
    #test_accuracy = accuracy_score(Y_test, Y_test_pred);
    #f1_score_model = f1_score(Y_test_pred, Y_test, average = 'samples');
    loss, accuracy, mse = model.evaluate(X_test, Y_test,verbose=0)
    roc_auroc = roc_auc_score(Y_test, Y_pred);
    print(roc_auroc);
    return 1 - roc_auroc;

#Hyperparameter tuning by Bayesian optimization


def f(params):
    return train_neural_newtork(X_train, Y_train, X_test, Y_test, params);


params_space = {'n_layers': hp.choice('n_layers', range(1,10)),
                    'n_neurons': hp.choice('n_neurons', [8, 16, 32, 64]),
                    'optimizer': hp.choice('optimizer', ['SGD', 'Adam', 'RMSprop', 'Adagrad']),
                    'epochs': hp.choice('epochs', range(1,10,100)),
                    'batch_size': hp.choice('batch_size', range(1,50,500))
                };

trials = Trials()

best = fmin(fn=f, space=params_space, algo=tpe.suggest, max_evals=50, trials=trials);


