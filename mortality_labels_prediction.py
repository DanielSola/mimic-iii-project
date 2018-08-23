"""
MIMIC-III Project
@author: Daniel Solá
"""
import itertools

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.realpath('__file__')));
import pandas as pd
from neural_network import get_neural_network_data
from keras.layers import Dense
from keras.models import Sequential
from sklearn.metrics import confusion_matrix, classification_report, precision_score, recall_score, log_loss, f1_score, mean_squared_error, roc_auc_score, accuracy_score
import time
from keras.optimizers import SGD, Adam, RMSprop, Adagrad
from hyperopt import hp, Trials, fmin, tpe
import keras.layers.advanced_activations
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
    model.fit(X_train, Y_train,epochs=epochs, batch_size=batch_size, verbose=1);
    elapsed_time = time.time() - start_time;
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
    print(train_accuracy, test_accuracy, f1_score_model, loss, mse, roc_auroc);
    return 1-roc_auroc;

#Hyperparameter tuning by Bayesian optimization


def f(params):
    return train_neural_newtork(X_train, Y_train, X_test, Y_test, params);


params_space = {'n_layers': hp.choice('n_layers', range(2,8)),
                    'n_neurons': hp.choice('n_neurons', [8, 16, 32, 64]),
                    'optimizer': hp.choice('optimizer', ['SGD', 'Adam', 'RMSprop', 'Adagrad']),
                    'epochs': hp.choice('epochs', [10, 25, 35]),
                    'batch_size': hp.choice('batch_size', [1, 25, 50])
                };

trials_mse = Trials()

best = fmin(fn=f, space=params_space, algo=tpe.suggest, max_evals=50, trials=trials_mse);

## Optimal MSE params

params = {'n_layers':6,
                    'n_neurons':16,
                    'optimizer': 'Adam',
                    'epochs':50,
                    'batch_size':50
                };


optimal_mse = train_neural_newtork(X_train, Y_train, X_test, Y_test, params)

### AUROC PLOTS


n_clases = 3
fpr = dict()
tpr = dict()
roc_auc = dict()
for i in range(n_classes):
    Y_test = np.array(Y_test)
    Y_pred = np.array(Y_pred)
    fpr[i], tpr[i], _ = roc_curve(Y_test[:, i], Y_pred[:, i])
    roc_auc[i] = auc(fpr[i], tpr[i])

import seaborn as sns

sns.regplot(x=fpr[0], y = tpr[0])


import seaborn as sns
sns.set('talk', 'whitegrid', 'dark', font_scale=0.70, font='Ricty',
        rc={"lines.linewidth": 2, 'grid.linestyle': '--'})

def plot_roc_auroc_curves(tpr, fpr, roc_auc, title):
    plt.figure()
    plt.plot(fpr[1], tpr[1], color='green',
         lw=lw, label='ROC Curve (AUC = %0.2f)' % roc_auc[1])
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(title)
    plt.legend(loc="lower right")
    plt.show()
    plt.savefig('roc_auc.png')
    plt.close()
    
plot_roc_auroc_curves(tpr[2], fpr[2], roc_auc[2], 'ROC Curve for >12 months mortality')


# Compute macro-average ROC curve and ROC area

# First aggregate all false positive rates
all_fpr = np.unique(np.concatenate([fpr[i] for i in range(n_classes)]))

# Then interpolate all ROC curves at this points
mean_tpr = np.zeros_like(all_fpr)
for i in range(n_classes):
    mean_tpr += interp(all_fpr, fpr[i], tpr[i])

# Finally average it and compute AUC
mean_tpr /= n_classes

fpr["macro"] = all_fpr
tpr["macro"] = mean_tpr
roc_auc["macro"] = auc(fpr["macro"], tpr["macro"])

# Plot all ROC curves
plt.figure()

colors = cycle(['aqua', 'darkorange', 'cornflowerblue'])
for i, color in zip(range(n_classes), colors):
    plt.plot(fpr[i], tpr[i], color=color, lw=lw,
             label='Curva ROC clase {0} (area = {1:0.2f})'
             ''.format(i, roc_auc[i]))

plt.plot([0, 1], [0, 1], 'k--', lw=lw)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Ratio Falsos Positivos')
plt.ylabel('Ratio Veraderos Positivos')
plt.title('Curvas ROC para clasificación multiclase')
plt.legend(loc="lower right")
plt.show()



### CONFUSION MATRIX

from mlxtend.evaluate import confusion_matrix 

Y_test_ravel = Y_test.argmax(axis = 1)
Y_pred_ravel = Y_pred.argmax(axis = 1)

cm = confusion_matrix(y_target=Y_test_ravel, 
                      y_predicted=Y_pred_ravel, 
                      binary=False)

def plot_confusion_matrix_seaborn(cm):
    cm_norm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    r = sns.heatmap(cm_norm, annot=True, 
            yticklabels=['<1 mes', '1-12 meses', '>12 meses'],
            xticklabels=['<1 mes', '1-12 meses', '>12 meses'],
            cbar = False)
    r.set_title('Matriz de confusión normalizada');
    r.set(xlabel='Valor Predicho', ylabel='Valor Real')
plot_confusion_matrix_seaborn(cm)

print(classification_report(Y_test_ravel, Y_pred_ravel))