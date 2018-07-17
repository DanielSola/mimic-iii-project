# -*- coding: utf-8 -*-
from fancyimpute import MICE as MICE
import pandas as pd
from sklearn import preprocessing

class NeuralNetworkService():
    
    def calculate_imputation_error(self, feature, numerical_data, numerical_features):
        numerical_data = numerical_data.copy(deep=True);
        feature_data = numerical_data[feature][0:200].copy().reset_index(drop = True);
        numerical_data[feature][0:200] = np.nan
        completed_numerical_data = pd.DataFrame(MICE(verbose = False).complete(numerical_data));
        completed_numerical_data.columns = numerical_features;
        imputed_feature = completed_numerical_data[feature][0:200];
        imputed_data = pd.DataFrame([feature_data, imputed_feature]).T
        imputed_data.columns =['Real value', 'Imputed value'];
        imputed_data['Imputation error (%)'] = np.abs((imputed_data['Real value']-imputed_data['Imputed value']) / imputed_data['Real value'])*100
        imputation_error = np.mean(imputed_data['Imputation error (%)'])
        print('Imputation error for',feature,': ', imputation_error);
        
        return [feature, imputation_error];
    
    def impute_missing_values(self, numerical_features):
        imputed_numerical_features = pd.DataFrame(MICE().complete(numerical_features));
        imputed_numerical_features.columns = numerical_features.columns;
        
        return imputed_numerical_features;
    
    def scale_numerical_features(self, imputed_numerical_features):
        scaled_numerical_features = pd.DataFrame(preprocessing.scale(imputed_numerical_features));
        scaled_numerical_features.columns = imputed_numerical_features.columns;
        scaled_numerical_features.index = imputed_numerical_features.index;
        
        return scaled_numerical_features;
    
    def hot_encode_categorical_features(self, categorical_features):
        
        hot_encoded_features_dfs = [];
        for feature in categorical_features: 
            hot_encoded_feature = pd.get_dummies(categorical_features[feature]);
            hot_encoded_features_dfs.append(hot_encoded_feature);
    
        hot_encoded_categorical_features = reduce(lambda left,right: pd.merge(left,right,left_index = True, right_index = True), hot_encoded_features_dfs);
        hot_encoded_categorical_features = hot_encoded_categorical_features[~hot_encoded_categorical_features.index.duplicated(keep='first')];
       
        return hot_encoded_categorical_features;
    
    def prepare_numerical_features(self, numerical_features):
        
        imputed_numerical_features = self.impute_missing_values(numerical_features);
        scaled_numerical_features = self.scale_numerical_features(imputed_numerical_features);
        scaled_numerical_features.index = numerical_features.index;
        
        return scaled_numerical_features;

