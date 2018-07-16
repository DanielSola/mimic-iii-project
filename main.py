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
from sklearn import preprocessing
from fancyimpute import MICE as MICE

#Preprocessed features
categorical_features = Features().get_categorical_features();
numerical_features = Features().get_numerical_features();

#Imputing of missing numerical values
imputed_numerical_features = pd.DataFrame(MICE().complete(numerical_features));

#Scaling of numerical values
scaled_numerical_features = pd.DataFrame(preprocessing.scale(imputed_numerical_features));
scaled_numerical_features.columns = numerical_features;
scaled_numerical_features.index = numerical_features.index;

#Hot encoding of categorical features

hot_encoded_features_dfs = [];
for feature in categorical_features: 
    hot_encoded_feature = pd.get_dummies(categorical_features[feature]);
    hot_encoded_features_dfs.append(hot_encoded_feature);


#TODO: merge all data


#Auxiliary function to convert dataframes to markdown for exporting
def df_to_markdown(df, float_format='%.2g'):
    from os import linesep
    return linesep.join([
        '|'.join(df.columns),
        '|'.join(4 * '-' for i in df.columns),
        df.to_csv(sep='|', index=False, header=False, float_format=float_format)
    ]).replace('|', ' | ')


