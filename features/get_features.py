# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 19:48:15 2018

@author: Daniel Solá
"""
import importlib
from resources.queries import *
from resources.mappings import *
from services.preprocessing_service import *
from services import preprocessing_service
from services.query_service import query_database
import pandas as pd
from functools import reduce
import numpy as np

class Features():
    
    def get_features(self):
        categorical_features = self.get_categorical_features();
        numerical_features = self.get_numerical_features();        
        return pd.merge(numerical_features, categorical_features, left_index = True, right_index = True, how = 'inner');

    def get_nn_features(self):

        categorical_features = self.get_categorical_features();
        numerical_features = self.get_numerical_features();        
        numerical_features_to_nn = preprocessing_service.prepare_numerical_features(numerical_features);
        categorical_features_to_nn = preprocessing_service.hot_encode_categorical_features(categorical_features);       
        
        return pd.merge(categorical_features_to_nn, numerical_features_to_nn, left_index = True, right_index = True, how = 'inner');

    def get_prediction_features(self, prediction_features):

        categorical_features = self.get_categorical_features();
        numerical_features = self.get_numerical_features();        
        numerical_features_to_nn = preprocessing_service.prepare_numerical_features(numerical_features);
        categorical_features_to_nn = preprocessing_service.hot_encode_categorical_features(categorical_features);       
        
        return pd.merge(categorical_features_to_nn, numerical_features_to_nn, left_index = True, right_index = True, how = 'inner');

    
    def get_numerical_features(self):
        
        age = self.DemographicData()._get_ages();
        measures = self.Measures().get_measures();
        icu_los = self.ICUData()._get_icu_length_of_stay();
        total_los = self.ICUData()._get_total_length_of_stay();
        previous_admission_count = self.ICUData()._get_previous_admissions_count();
        procedure_count = self.ICUData()._get_procedure_count();
        severity_scores = self.ICUData()._get_severity_scores();
        glascow_coma_scale = self.ICUData()._get_glasgow_coma_scale();
        mech_vent_time = self.ICUData()._get_mechanical_ventilation_time();
        ##hospital_expire_flag = self.ICUData()._get_hospital_expire_flag();

        numerical_features_dfs = [ age, measures, icu_los, total_los, previous_admission_count, procedure_count, severity_scores, glascow_coma_scale, mech_vent_time ];     
        numerical_features = reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id', how = 'outer'), numerical_features_dfs);
                
        numerical_features['total_mech_vent_time'].fillna(0, inplace = True);
        numerical_features['procedure_count'].fillna(1, inplace = True);
        numerical_features['gcs'].fillna(13, inplace = True);
        numerical_features.set_index('hadm_id', drop=True, inplace = True);    
        numerical_features.drop('subject_id', inplace = True, axis = 1);

        return numerical_features;
    
    def get_categorical_features(self):
        
        gender = self.DemographicData()._get_genders();
        marital_status = self.DemographicData()._get_marital_status();
        religion = self.DemographicData()._get_religion();
        ethnicity = self.DemographicData()._get_ethnic_group();
        
        admission_service = self.ICUData()._get_services();
        icd9_diag_code = self.ICUData()._get_icd9_diag_codes();
        surgery_flag = self.ICUData()._get_surgery_flags();
        
        categorical_features_dfs = [ gender, marital_status, religion, ethnicity, admission_service, icd9_diag_code, surgery_flag ];     
        
        categorical_features = reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id', how = 'outer'), categorical_features_dfs);
        categorical_features['SURGERY_FLAG'].fillna('NO SURGERY', inplace = True);
        categorical_features['service'].fillna('MED', inplace = True);   
        categorical_features.dropna(inplace = True);
        categorical_features.set_index('hadm_id', drop=True, inplace = True);        
        
        return categorical_features;
        
    class DemographicData():
        
        def _get_ages(self):
            
            ages = query_database(AGE_QUERY);
            
            ages['age'] = ages.apply(lambda x: x['age'] if x['age'] < 300 else 91.4, axis = 1);
            
            return ages;
            
        def _get_genders(self):
            
            return query_database(GENDER_QUERY);
        
        def _get_marital_status(self):
            
            marital_status_df = query_database(MARITAL_STATUS_QUERY);
            
            return preprocessing_service.group_marital_status(marital_status_df);
        
        def _get_religion(self):
            
            religion_df = query_database(RELIGION_QUERY);
            
            return preprocessing_service.group_religion(religion_df);
        
        def _get_ethnic_group(self):
            
            ethnic_group_df = query_database(ETHNICITY_QUERY);
            
            return preprocessing_service.group_ethnic_groups(ethnic_group_df);
        
        def get_demographic_data(self):
            
            age             = self._get_ages();
            gender          = self._get_genders();
            marital_status  = self._get_marital_status();
            religion        = self._get_religion();
            ethnic_group    = self._get_ethnic_group();
            
            demographic_dfs = [age, gender, marital_status, religion, ethnic_group];
            
            return reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id'), demographic_dfs);
            
    class Measures():
                    
        def get_lab_data(self):
            
            lab_results_dfs = [];
        
            for measure in LAB_TEST:
                
                print(f"""Querying {measure['test']}""" );
    
                lab_test_df = query_database(f'''SELECT hadm_id, 
                                             avg(valuenum) AS AVG_{measure['test']},
                                             stddev(valuenum) AS STD_{measure['test']}
                                             FROM labevents
                                             WHERE itemid in ({measure['itemid']} )
                                             GROUP BY hadm_id'''
                                             );            
                
                filtered_data = remove_outliers(lab_test_df, 1, 0.01, 0.99);
                                        
                lab_results_dfs.append(filtered_data);
    
            return reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id', how = 'outer'), lab_results_dfs);
    
                
        def get_physio_data(self):
            
            all_physio_data = [];
                    
            for measure in PHYSIO_MEASURES:
                
                print(f"""Querying {measure['name']}""");
                            
                physio_data = query_database(f'''SELECT 
                                                hadm_id,
                                                avg(valuenum) AS AVG_{measure['name']},
                                                stddev(valuenum) AS STD_{measure['name']}
                                                FROM chartevents
                                                WHERE itemid in ({measure['itemid']})
                                                GROUP BY hadm_id
                                                ''');
                
                filtered_avg_data = remove_outliers(physio_data, 1, 0.01, 0.99);
                filtered_all_data = remove_outliers(physio_data, 2, 0.01, 0.99);
    
                all_physio_data.append(filtered_all_data);
                
            return reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id', how = 'outer'), all_physio_data);
        
        def get_measures(self):
            
            lab_data = self.get_lab_data();
            physio_data = self.get_physio_data();
            
            measures = [lab_data, physio_data];
            
            return reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id', how = 'outer'), measures);
                
    class ICUData():
    
        def _get_services(self):
                
            services = query_database(SERVICE_QUERY);       
            relevant_services_list = list(services.apply(lambda x: preprocessing_service.get_relevant_admission_service(x['hadm_id'], services), axis = 1));
            relevant_services_df = pd.DataFrame(relevant_services_list, columns = ['hadm_id','service']);
            grouped_services = relevant_services_df.groupby("hadm_id").first();
            grouped_services['hadm_id'] = grouped_services.index;
            return grouped_services;
            
        def _get_icd9_diag_codes(self):
            
            icd9_codes = query_database(DIAG_ICD9_CODES_QUERY);
            icd9_codes['icd9_group'] = icd9_codes.apply(lambda x: preprocessing_service.group_diag_icd9_code(x['icd9_code']), axis = 1);
    
            return icd9_codes[['hadm_id', 'icd9_group']];
                    
        def _get_surgery_flags(self):
            
            surgery_flags = pd.read_csv('C:\\mimic-iii-project\\resources\\surgery_flags_i9_2015.csv');
            surgery_flags.columns = ['ICD9_PROC_CODE','SURGERY_FLAG','DESC'];
            surgery_flags['ICD9_PROC_CODE'] = surgery_flags.apply(lambda x: int(x['ICD9_PROC_CODE'][1:5]), axis = 1);
            surgery_flags['SURGERY_FLAG'] = surgery_flags.apply(lambda x: int(x['SURGERY_FLAG'][1:2]), axis = 1);
            
            icd9_proc_codes = query_database(PROC_ICD9_CODES_QUERY);
            icd9_proc_codes['icd9_code'] = icd9_proc_codes['icd9_code'].astype(int);
            
            merge = pd.merge(surgery_flags, icd9_proc_codes, left_on='ICD9_PROC_CODE', right_on='icd9_code', how = 'outer');
            merge['SURGERY_FLAG'] = merge['SURGERY_FLAG'].map(lambda x: preprocessing_service.convert_surgery_flag_to_category(x));
            surgery_flags =  merge[['hadm_id','SURGERY_FLAG']];
            surgery_flags.dropna(inplace = True);

            return surgery_flags;
        
        def _get_icu_length_of_stay(self):
            
            return query_database(ICU_LOS_QUERY);
    
        def _get_total_length_of_stay(self):
            
            return query_database(TOTAL_LOS_QUERY);
    
        def _get_previous_admissions_count(self):
            
            admissions = query_database(PREVIOUS_ADMISSIONS_QUERY);
            
            return get_admission_number(admissions);
              
        def _get_procedure_count(self):
            
            return query_database(PROCEDURE_COUNT_QUERY);
        
        def _get_severity_scores(self):
                    
            return query_database(SEVERITY_SCORES_QUERY);
        
        def _get_glasgow_coma_scale(self):
            
            return query_database(GLASGOW_COMA_SCALE_QUERY);
        
        def _get_mechanical_ventilation_time(self):
                    
            return query_database(MECHANICAL_VENTILATION_TIME_QUERY);
        
        def _get_hospital_expire_flag(self):
            
            return query_database(HOSPITAL_EXPIRE_FLAG_QUERY);
        
        def get_icu_data(self):
            
            admission_service         = self._get_services();
            icd9_diags                = self._get_icd9_diag_codes();
            surgery_flags             = self._get_surgery_flags();
            icu_los                   = self._get_icu_length_of_stay();
            total_los                 = self._get_total_length_of_stay();
            previous_admissions_count = self._get_previous_admissions_count();
            procedure_count           = self._get_procedure_count();
            severity_scores           = self._get_severity_scores();
            glasgow_coma_scale        = self._get_glasgow_coma_scale();
            mechanical_vent_time      = self._get_mechanical_ventilation_time();
            hospital_expire_flag      = self._get_hospital_expire_flag();
            
            icu_dfs = [admission_service,
                         icd9_diags,
                         surgery_flags,
                         icu_los,
                         total_los,
                         previous_admissions_count,
                         procedure_count,
                         severity_scores,
                         glasgow_coma_scale,
                         mechanical_vent_time,
                         hospital_expire_flag];
            
            
            merged_icu_data = reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id', how = 'inner'), icu_dfs);
                
            merged_icu_data['total_mech_vent_time'].fillna(0, inplace = True);
            merged_icu_data['procedure_count'].fillna(1, inplace = True);
            
            return merged_icu_data;
        
        

        
        

    

