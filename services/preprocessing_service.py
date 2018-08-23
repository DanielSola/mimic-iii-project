# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 19:06:14 2018

@author: Daniel Solá
"""
import numpy as np
from resources.mappings import *
import pandas as pd
from fancyimpute import MICE as MICE
from sklearn import preprocessing
from functools import reduce

def remove_outliers(data, column_index, low_quantile, high_quantile):
    
    low_quantile_value = float(data.iloc[:, column_index].quantile(low_quantile));
    high_quantile_value = float(data.iloc[:, column_index].quantile(high_quantile));

    data.iloc[:,column_index] = data.iloc[:,column_index].apply(lambda x: x if (x <= high_quantile_value and x >= low_quantile_value)  else np.NaN);
    
    return data;

def get_relevant_admission_service(hadm_id, services_df):
    
    admission_services = list(services_df.loc[services_df['hadm_id'] == hadm_id].curr_service)
    
    special_surgery_service = list(filter(lambda x: 'SURG' in x and x != "SURG", admission_services)) ##Cirugia especial
    general_surgery_service = list(filter(lambda x:  x == 'SURG', admission_services)) ##Cirugia general
    specialised_service = list(filter(lambda x:  x != 'MED' and not 'SURG' in x, admission_services)) ##No medicina general
    general_medicine_service = list(filter(lambda x:  x == 'MED', admission_services)) ##medicina general
    
    if special_surgery_service:
        return (hadm_id, special_surgery_service[0])
    if general_surgery_service:
        return (hadm_id, general_surgery_service[0])
    if specialised_service:
        return (hadm_id, specialised_service[0])
    if general_medicine_service:
        return (hadm_id, general_medicine_service[0])
    
def group_marital_status(marital_status_df):

    marital_status_df['marital_status'] = marital_status_df['marital_status'].map(MARITAL_STATUS_GROUPS);
    
    return marital_status_df;

def group_religion(religion_df):
    
    religion_df['religion'] = religion_df['religion'].map(RELIGION_GROUPS);
    
    return religion_df;

def group_ethnic_groups(ethnic_group_df):
    
    ethnic_group_df['ethnicity'] = ethnic_group_df['ethnicity'].map(ETHNIC_GROUPS);
    
    return ethnic_group_df;

def convert_surgery_flag_to_category(flag):
    if flag == 2 or flag == 1:
        return 'NARROW';
    else:
        return 'NO SURGERY';
    
def get_admission_number(admissions):

    already_admitted_subjects = [];
    previous_admissions = [];
    for (index, row) in admissions.iterrows():
    
        already_admitted_subjects.append(row.subject_id)
    
        admissions_count = already_admitted_subjects.count(row.subject_id)
        previous_admissions.append({
    				'subject_id':row.subject_id,
    				'hadm_id':row.hadm_id,
    				'admissions_count':admissions_count
    				})
    
    return pd.DataFrame(previous_admissions);

def group_diag_icd9_code(icd9_code):
    
    if not 'V' in icd9_code and not 'E' in icd9_code:
        
        truncated_code = int((icd9_code)[0:3]);
        
        if truncated_code > 0 and truncated_code <= 139:
            return 'infectious and parasitic diseases';
        if truncated_code > 139 and truncated_code <= 239:
            return 'neoplasms';
        if truncated_code > 239 and truncated_code <= 279:
            return 'endocrine, nutritional and metabolic diseases, and immunity disorders';
        if truncated_code > 279 and truncated_code <= 289:
            return 'diseases of the blood and blood-forming organs';
        if truncated_code > 289 and truncated_code <= 320:
            return 'mental disorders';
        if truncated_code > 320 and truncated_code <= 389:
            return 'diseases of the nervous system and sense organs';
        if truncated_code > 389 and truncated_code <= 459:
            return 'diseases of the circulatory system';
        if truncated_code > 459 and truncated_code <= 519:
            return 'diseases of the respiratory system';
        if truncated_code > 519 and truncated_code <= 579:
            return 'diseases of the digestive system';
        if truncated_code > 579 and truncated_code <= 629:
            return 'diseases of the genitourinary system';
        if truncated_code > 629 and truncated_code <= 679:
            return 'complications of pregnancy, childbirth, and the puerperium';
        if truncated_code > 679 and truncated_code <= 709:
            return 'diseases of the skin and subcutaneous tissue';
        if truncated_code > 709 and truncated_code <= 739:
            return 'diseases of the musculoskeletal system and connective tissue';
        if truncated_code > 739 and truncated_code <= 759:
            return 'congenital anomalies';
        if truncated_code > 759 and truncated_code <= 779:
            return 'certain conditions originating in the perinatal period';        
        if truncated_code > 779 and truncated_code <= 799:
            return 'symptoms, signs, and ill-defined conditions';       
        if truncated_code > 799 and truncated_code <= 999:
            return 'injury and poisoning';                         
    if 'E' in icd9_code: 
        return 'external causes of injury';
    if 'V' in icd9_code: 
        return 'supplementary classification of factors influencing health status';    

def extract_readmissions(admissions_data):
    
    total_readmissions = [];
    for index in range(admissions_data.shape[0] - 1):
        if admissions_data.ix[index].subject_id == admissions_data.ix[index + 1].subject_id:
            
            if (
                (admissions_data.ix[index + 1].admittime - admissions_data.ix[index].dischtime).days < (30 * 12)
                and 
                (admissions_data.ix[index + 1].admittime - admissions_data.ix[index].dischtime).days > (30* 0)
                
            ):
                readmission = '0-12 months';
                
            if (
                (admissions_data.ix[index + 1].admittime - admissions_data.ix[index].dischtime).days < (30 * 36)
                and 
                (admissions_data.ix[index + 1].admittime - admissions_data.ix[index].dischtime).days >= (30 * 12)
            ):
                readmission = '12-36 months';               
        else:
            readmission = '36+ months';
    
        total_readmissions.append({
                    'hadm_id': admissions_data.ix[index].hadm_id, 
                    'readmission': readmission
                    });
    
    return pd.DataFrame(total_readmissions);

def extract_readmission_time(admissions_data):
    
    readmission_times = [];
    for index in range(admissions_data.shape[0] - 1):
        if admissions_data.ix[index].subject_id == admissions_data.ix[index + 1].subject_id:
            readmission_days = (admissions_data.ix[index + 1].admittime - admissions_data.ix[index].dischtime).days
            if readmission_days > 0.5:
                readmission_times.append({
                        'hadm_id': admissions_data.ix[index].hadm_id, 
                        'readmission_days': readmission_days
                        });
    
    return pd.DataFrame(readmission_times);
    
def calculate_imputation_error(feature, numerical_data, numerical_features):
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

def impute_missing_values(numerical_features):
    imputed_numerical_features = pd.DataFrame(MICE().complete(numerical_features));
    imputed_numerical_features.columns = numerical_features.columns;
    
    return imputed_numerical_features;

def scale_numerical_features(imputed_numerical_features):
    scaled_numerical_features = pd.DataFrame(preprocessing.scale(imputed_numerical_features));
    scaled_numerical_features.columns = imputed_numerical_features.columns;
    scaled_numerical_features.index = imputed_numerical_features.index;
    
    return scaled_numerical_features;

def hot_encode_categorical_features(categorical_features):
    
    hot_encoded_features_dfs = [];
    for feature in categorical_features: 
        hot_encoded_feature = pd.get_dummies(categorical_features[feature]);
        hot_encoded_features_dfs.append(hot_encoded_feature);

    hot_encoded_categorical_features = reduce(lambda left,right: pd.merge(left,right,left_index = True, right_index = True), hot_encoded_features_dfs);
    hot_encoded_categorical_features = hot_encoded_categorical_features[~hot_encoded_categorical_features.index.duplicated(keep='first')];
   
    return hot_encoded_categorical_features;

def prepare_numerical_features(numerical_features):
    
    imputed_numerical_features = impute_missing_values(numerical_features);
    scaled_numerical_features = scale_numerical_features(imputed_numerical_features);
    scaled_numerical_features.index = numerical_features.index;
    
    return scaled_numerical_features;
#Auxiliary function to convert dataframes to markdown for exporting
def df_to_markdown(df, float_format='%.2g'):
    from os import linesep
    return linesep.join([
        '|'.join(df.columns),
        '|'.join(4 * '-' for i in df.columns),
        df.to_csv(sep='|', index=False, header=False, float_format=float_format)
    ]).replace('|', ' | ')