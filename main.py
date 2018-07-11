"""
MIMIC-III Project
@author: Daniel Solá
"""
import pandas as pd
import sys
import os
from get_features import *
from get_labels import *
import pandas as pd
import seaborn as sns
sys.path.insert(0, os.path.dirname(os.path.realpath('__file__')));
from sklearn import preprocessing
from fancyimpute import MICE as MICE

#Joined all data
icu_data = ICUData().get_icu_data();
measures = Measures().get_measures();
demo_data = DemographicData().get_demographic_data();
features_array = [icu_data, measures, demo_data];
features = reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id', how = 'outer'), features_array);
labels = PatientOutcomes().get_patient_outcomes();

data = reduce(lambda left, right: pd.merge(left, right, on = 'hadm_id', how = 'outer'), [features, labels]);

#Split data between numerical and categorical features

numerical_features = ['total_icu_time',
       'total_los_days', 'admissions_count','procedure_count',
       'oasis_avg', 'sofa_avg', 'saps_avg', 'total_mech_vent_time',
       'avg_blood_urea_nitrogen', 'std_blood_urea_nitrogen',
       'avg_platelet_count', 'std_platelet_count', 'avg_hematrocrit',
       'std_hematrocrit', 'avg_potasssium', 'std_potasssium', 'avg_sodium',
       'std_sodium', 'avg_creatinine', 'std_creatinine', 'avg_bicarbonate',
       'std_bicarbonate', 'avg_white_blood_cells', 'std_white_blood_cells',
       'avg_blood_glucose', 'std_blood_glucose', 'avg_albumin', 'std_albumin',
       'avg_hr', 'std_hr', 'avg_resp_rate', 'std_resp_rate', 'avg_sys_press',
       'std_sys_press', 'avg_dias_press', 'std_dias_press', 'avg_temp',
       'std_temp', 'avg_cvp', 'std_cvp', 'avg_art_ph', 'std_art_ph',
       'avg_spo2', 'std_spo2', 'age']

categorical_features = ['service',
                        'icd9_group',
                        'SURGERY_FLAG',
                        'marital_status',
                        'religion',
                        'gender',
                        'ethnicity',];

numerical_data = data[numerical_features];
categorical_data = data[categorical_features];

#Count of null values

numerical_data_null = numerical_data.isnull().sum().sort_values();

#Imputation of missing data using MICE algorithm

completed_numerical_data = pd.DataFrame(MICE().complete(numerical_data));
completed_numerical_data.columns = numerical_features;

#Scaling of data

scaled_data = pd.DataFrame(preprocessing.scale(completed_numerical_data));
scaled_data.columns = numerical_features;

#Correlation matrix 

correlation_matrix = scaled_data.corr()
correlations = correlation_matrix.unstack()
sorted_correlations = pd.DataFrame(correlations.sort_values(kind="quicksort")).reset_index();

strong_positive_feature_correlations = sorted_correlations[(sorted_correlations > 0.5) & (sorted_correlations < 1)];
strong_negative_feature_correlations = sorted_correlations[(sorted_correlations < -0.5)];

sns.heatmap(features);

#TODO: prepare neural network



#Auxiliary function to convert dataframes to markdown for exporting
def df_to_markdown(df, float_format='%.2g'):
    from os import linesep
    return linesep.join([
        '|'.join(df.columns),
        '|'.join(4 * '-' for i in df.columns),
        df.to_csv(sep='|', index=False, header=False, float_format=float_format)
    ]).replace('|', ' | ')



