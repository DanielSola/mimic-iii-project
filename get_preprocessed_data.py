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

class DemographicData():
    
    def __get_ages(self):
        
        ages = query_database(AGE_QUERY)
        
        ages['age'] = ages.apply(lambda x: x['age'] if x['age'] < 300 else 91.4, axis = 1)
        
        return ages
        
    def __get_genders(self):
        
        return query_database(GENDER_QUERY)
    	
    
    def __get_marital_status(self):
        
        marital_status_df = query_database(MARITAL_STATUS_QUERY)
        
        return preprocessing_service.group_marital_status(marital_status_df)
    
    def __get_religion(self):
        
        religion_df = query_database(RELIGION_QUERY)
        
        return preprocessing_service.group_religion(religion_df)
    
    def __get_ethnic_group(self):
        
        ethnic_group_df = query_database(ETHNICITY_QUERY)
        
        return preprocessing_service.group_ethnic_groups(ethnic_group_df)
    
    def get_demographic_data(self):
        
        age             = self.__get_ages()
        gender          = self.__get_genders()
        marital_status  = self.__get_marital_status()
        religion        = self.__get_religion()
        ethnic_group    = self.__get_ethnic_group()
        
        demographic_dfs = [age, gender, marital_status, religion, ethnic_group]
        
        demo_data = reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id'), demographic_dfs)
        
        demo_data.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\DEMOGRAPHIC_DATA\\DEMO_DATA.csv''', sep = '\t');

        print('DEMOGRAPHIC DATA EXPORTING FINISHED')
        
class Measures():
    
    def get_severity_scores(self):
        
        print('Querying database...');
        
        severity_scores = query_database(SEVERITY_SCORES_QUERY);
        
        severity_scores.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\HOSPITAL_DATA\\SEVERITY_SCORES.csv''', sep = '\t');
    
    def get_mechanical_ventilation_time(self):
        
        print('Querying database...');
        
        mechanical_ventilation_time = query_database(MECHANICAL_VENTILATION_TIME_QUERY);
        
        mechanical_ventilation_time.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\HOSPITAL_DATA\\MECH_VENT_TIME.csv''', sep = '\t');
        
        
    def get_lab_data(self):
        
        lab_results_dfs = []
    
        for measure in LAB_TEST:
            
            print(f'''Querying {measure['test']}...''' )
            
            lab_test_df = query_database(f'''SELECT 
                                      hadm_id,
                                      avg(valuenum) AS AVG_{measure['test']},
                                      stddev(valuenum) AS STD_{measure['test']}
                                      FROM labevents
                                      WHERE itemid in ({measure['itemid']} )
                                      GROUP BY hadm_id
                                      ''')
            
            print('Returned ' + str(lab_test_df.shape[0]) + ' rows')
            print('Writing to CSV file...')
            
            lab_test_df.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\LAB_DATA\\{measure['test']}.csv''', sep = '\t')

        print('Exporting done')

    def get_physio_data(self):
        
        icu_length_of_stay = query_database(f'''SELECT
                                        hadm_id, 
                                        sum(los) AS total_icu_time
                                        FROM icustays
                                        GROUP BY hadm_id
                                        ORDER BY hadm_id
                                        ''')
                
        for measure in PHYSIO_MEASURES:
            
            print(f'''Querying {measure['name']}...''' )
            
            physio_data = query_database(f'''SELECT 
                                            hadm_id,
                                            avg(valuenum) AS AVG_{measure['name']},
                                            stddev(valuenum) AS STD_{measure['name']},
                                            count(valuenum) AS SAMPLES
                                            FROM chartevents
                                            WHERE itemid in ({measure['itemid']})
                                            GROUP BY hadm_id
                                            ''')     
            
            physio_data = reduce(lambda left, right: pd.merge(left, right, how = 'outer', on = 'hadm_id'), [physio_data, icu_length_of_stay])
            
            filtered_data = PhysioPreprocess().discard_undersampled_outliers(physio_data)
            
            print('Writing to CSV file...')
            
            filtered_data.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\PHYSIO_DATA\\{measure['name']}.csv''', sep = '\t')
            
        print('Exporting finished')
        

class AdministrativeData():

    def get_services(self):
        
        print('Querying admission services...');
    
        services = query_database(SERVICE_QUERY);
        
        print('Preprocessing data...')

        relevant_services_list = list(services.apply(lambda x: preprocessing_service.get_relevant_admission_service(x['hadm_id'], services), axis = 1))
    
        relevant_services_df = pd.DataFrame(relevant_services_list, columns = ['hadm_id','service'])
    
        preprocessed_service_data = relevant_services_df.groupby("hadm_id").first();
        
        print('Writing to CSV file...')

        preprocessed_service_data.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\ADMINISTRATIVE_DATA\\SERVICES.csv''', sep = '\t')

    
    def get_icd9_diag_codes(self):
        
        print('Querying ICD9 diagnostic codes...');

        icd9_codes = query_database(DIAG_ICD9_CODES_QUERY);
        
        print('Preprocessing data...')
        
        icd9_codes['icd9_group'] = icd9_codes.apply(lambda x: preprocessing_service.group_diag_icd9_code(x['icd9_code']), axis = 1)

        preprocessed_icd9_diag_codes = icd9_codes[['hadm_id', 'icd9_group']];
        
        print('Writing to CSV file...')
        
        preprocessed_icd9_diag_codes.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\ADMINISTRATIVE_DATA\\ICD9_DIAG.csv''', sep = '\t');

    def get_surgery_flags(self):
        
        def convert_flag_to_category(flag):
            if flag == 2:
                return 'NARROW'
            if flag == 1:
                return 'BROAD'
            else:
                return 'NO SURGERY'
        
        print('Getting surgery flags...');
        
        surgery_flags = pd.read_csv('C:\\mimic-iii-project\\resources\\surgery_flags_i9_2015.csv');
        
        surgery_flags.columns = ['ICD9_PROC_CODE','SURGERY_FLAG','DESC'];
        
        surgery_flags['ICD9_PROC_CODE'] = surgery_flags.apply(lambda x: int(x['ICD9_PROC_CODE'][1:5]), axis = 1)
        surgery_flags['SURGERY_FLAG'] = surgery_flags.apply(lambda x: int(x['SURGERY_FLAG'][1:2]), axis = 1)
        
        icd9_proc_codes = query_database(PROC_ICD9_CODES_QUERY);
        
        icd9_proc_codes['icd9_code'] = icd9_proc_codes['icd9_code'].astype(int);
        
        merge = pd.merge(surgery_flags, icd9_proc_codes, left_on='ICD9_PROC_CODE', right_on='icd9_code', how = 'outer');

        merge['SURGERY_FLAG'] = merge['SURGERY_FLAG'].map(lambda x: convert_flag_to_category(x));
        
        df_surgery_flags = merge[['hadm_id','SURGERY_FLAG']].dropna();
        
        print('Writing to file...')
        
        df_surgery_flags.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\ADMINISTRATIVE_DATA\\SURGERY_FLAGS.csv''', sep = '\t');
        
    def get_icu_length_of_stay(self):
        
        icu_los = query_database(ICU_LOS_QUERY);

        print('Writing to file...')
        
        icu_los.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\ADMINISTRATIVE_DATA\\ICU_LOS.csv''', sep = '\t');
        
    def get_total_length_of_stay(self):
        
        total_los = query_database(TOTAL_LOS_QUERY);
        
        print('Writing to file...');
        
        total_los.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\ADMINISTRATIVE_DATA\\TOTAL_LOS.csv''', sep = '\t');

    def get_previous_admissions_count(self):
        
        admissions = query_database(PREVIOUS_ADMISSIONS_QUERY);
        
        admission_count = get_admission_number(admissions);
        
        print('Writing to file...');

        
        admission_count.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\ADMINISTRATIVE_DATA\\PREVIOUS_ADMISSION_COUNT.csv''', sep = '\t');

        
    def get_procedure_count(self):
        
        procedure_counts = query_database(PROCEDURE_COUNT_QUERY);
        
        print('Writing to file...');

        procedure_counts.to_csv(f'''C:\\mimic-iii-project\\mimic_data\\ADMINISTRATIVE_DATA\\PROCEDURE_COUTNS.csv''', sep = '\t');

        
        
        
        
        

    

