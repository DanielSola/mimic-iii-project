# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 19:06:14 2018

@author: Daniel Solá
"""
import numpy as np
from resources.mappings import *

class PhysioPreprocess():
    
    def check_outlier(self, value, avg, std):
        if value > avg + 2*std or value < avg - 2*std:
            return True 
        else: 
            return False
    
    def check_undersampled(self, samples, samples_avg, samples_std):
        if samples < samples_avg - 2*samples_std:
            return True
        else:
            return False
        
    def discard_undersampled_outliers(self, physio_data):
                
        print('Discarding undersampled_outliers...')

        physio_data['samples/day'] = physio_data['samples']/physio_data['total_icu_time']
        
        value_mean = np.nanmean(physio_data.iloc[:,1])
        value_std = np.nanstd(physio_data.iloc[:,1])
        
        samples_mean = np.nanmean(physio_data['samples/day'])
        samples_std = np.nanstd(physio_data['samples/day'])
        
        for index, row in physio_data.iterrows():
            
            if ( 
                    self.check_outlier(row[1], value_mean, value_std) is True and
                    self.check_undersampled(row[5], samples_mean, samples_std) is True       
                ):
                
                physio_data.iloc[index, 1] = 'UNDERSAMPLED OUTLIER'
                physio_data.iloc[index, 2] = 'UNDERSAMPLED OUTLIER'
            
            
        return physio_data.iloc[:,0:3]
    
    

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
    

    marital_status_df['marital_status'] = marital_status_df['marital_status'].map(MARITAL_STATUS_GROUPS)
    return marital_status_df

def group_religion(religion_df):
    
    religion_df['religion'] = religion_df['religion'].map(RELIGION_GROUPS)
    
    return religion_df

def group_ethnic_groups(ethnic_group_df):
    
    ethnic_group_df['ethnicity'] = ethnic_group_df['ethnicity'].map(ETHNIC_GROUPS)
    
    return ethnic_group_df


def get_admission_number(admissions_df):

	for index, row in admissions.iterrows():
    
		already_admitted_subjects.append(row.subject_id)
    
		admissions_count = already_admitted_subjects.count(row.subject_id)
    
		previous_admissions.append({
				'subject_id':row.subject_id,
				'hadm_id':row.hadm_id,
				'admissions_count':admissions_count
				})
    
	return pd.DataFrame(previous_admissions)  

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
        if truncated_code > 289 and truncated_code <= 319:
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
    
    
    
    