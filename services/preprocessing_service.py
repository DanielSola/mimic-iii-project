# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 19:06:14 2018

@author: Tiendeo
"""

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
    
    marital_status_groups = { 'MARRIED'           : 'MARRIED',
                              'LIFE PARTNER'      : 'MARRIED',
                              'SINGLE'            : 'SINGLE',
                              'DIVORCED'          : 'DIVORCED/SEPARATED',
                              'SEPARATED'         : 'DIVORCED/SEPARATED',
                               None              : 'UNKNOWN',
                              'UNKNOWN (DEFAULT)' : 'UNKNOWN',
                              'WIDOWED'           : 'WIDOWED'
                            }
    
    marital_status_df['marital_status'] = marital_status_df['marital_status'].map(marital_status_groups)
    
    return marital_status_df

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