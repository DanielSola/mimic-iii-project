# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 19:06:14 2018

@author: Daniel Solá
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
                               None               : 'UNKNOWN',
                              'UNKNOWN (DEFAULT)' : 'UNKNOWN',
                              'WIDOWED'           : 'WIDOWED'
                            }
    
    marital_status_df['marital_status'] = marital_status_df['marital_status'].map(marital_status_groups)
    
    return marital_status_df

def group_religion(religion_df):
    
    religion_groups = { 'CATHOLIC'                : 'CHRISTIAN',
                        'PROTESTANT QUAKER'       : 'CHRISTIAN',
                        'EPISCOPALIAN'            : 'CHRISTIAN',
                        'CHRISTIAN SCIENTIST'     : 'CHRISTIAN',
                        '''JEHOVAH'S WITNESS'''   : 'CHRISTIAN',
                        'UNITARIAN-UNIVERSALIST'  : 'CHRISTIAN',
                        '7TH DAY ADVENTIST'       : 'CHRISTIAN',
                        'BAPTIST'                 : 'CHRISTIAN',
                        'LUTHERAN'                : 'CHRISTIAN',
                        'METHODIST'               : 'CHRISTIAN',
                        'GREEK ORTHODOX'          : 'ORTHODOX',
                        'ROMANIAN EAST. ORTH'     : 'ORTHODOX',
                        'JEWISH'                  : 'JEWISH/HEBREW',
                        'HEBREW'                  : 'JEWISH/HEBREW',
                        'NOT SPECIFIED'           : 'NONE',
                        'UNOBTAINABLE'            : 'NONE',
                        'OTHER'                   : 'NONE',
                         None                     : 'NONE',
                        'BUDDHIST'                : 'BUDDHIST/HINDU',
                        'HINDU'                   : 'BUDDHIST/HINDU',
                        'MUSLIM'                  : 'MUSLIM'
                                  
                    }
    
    religion_df['religion'] = religion_df['religion'].map(religion_groups)
    
    return religion_df

def group_ethnic_groups(ethnic_group_df):
    
    ethnic_groups = {'WHITE'  													              :  'WHITE',
                     'WHITE - RUSSIAN'  											           :  'WHITE',
                     'WHITE - OTHER EUROPEAN'  									           :  'WHITE',
                     'PORTUGUESE'  												              :  'WHITE',
                     'WHITE - BRAZILIAN'  									              :  'WHITE',
                     'WHITE - EASTERN EUROPEAN'  								           :  'WHITE',
                     'BLACK/AFRICAN AMERICAN'  									           :  'BLACK',
                     'BLACK/CAPE VERDEAN'  										           :  'BLACK',
                     'BLACK/HAITIAN'  											              :  'BLACK',
                     'BLACK/AFRICAN'  											              :  'BLACK',
                     'UNKNOWN/NOT SPECIFIED'  								              :  'NONE',
                     'UNABLE TO OBTAIN' 									                 :  'NONE',
                     'PATIENT DECLINED TO ANSWER'  								        :  'NONE',
                     'HISPANIC OR LATINO'  										           :  'HISPANIC',
                     'HISPANIC/LATINO - PUERTO RICAN'  							        :  'HISPANIC',
                     'HISPANIC/LATINO - DOMINICAN'  								        :  'HISPANIC',
                     'HISPANIC/LATINO - GUATEMALAN'  							           :  'HISPANIC',
                     'HISPANIC/LATINO - CUBAN'  								           :  'HISPANIC',
                     'HISPANIC/LATINO - SALVADORAN'  							           :  'HISPANIC',
                     'HISPANIC/LATINO - MEXICAN'  								           :  'HISPANIC',
                     'HISPANIC/LATINO - CENTRAL AMERICAN (OTHER)'  				     :  'HISPANIC',
                     'HISPANIC/LATINO - COLOMBIAN'  								        :  'HISPANIC',
                     'SOUTH AMERICAN'  											           :  'HISPANIC',
                     'HISPANIC/LATINO - HONDURAN'  								        :  'HISPANIC',
                     'OTHER' 													                 :  'OTHER',
                     'MULTI RACE ETHNICITY'  									           :  'OTHER',
                     'AMERICAN INDIAN/ALASKA NATIVE'  							        :  'OTHER',
                     'MIDDLE EASTERN'  											           :  'OTHER',
                     'NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER'  				     :  'OTHER',
                     'CARIBBEAN ISLAND'  										              :  'OTHER',
                     'AMERICAN INDIAN/ALASKA NATIVE FEDERALLY RECOGNIZED TRIBE'    :  'OTHER',
                     'ASIAN'  													              :  'ASIAN',
                     'ASIAN - CHINESE'  											           :  'ASIAN',
                     'ASIAN - ASIAN INDIAN'  									           :  'ASIAN',
                     'ASIAN - VIETNAMESE'  										           :  'ASIAN',
                     'ASIAN - FILIPINO'  										              :  'ASIAN',
                     'ASIAN - CAMBODIAN'  										           :  'ASIAN',
                     'ASIAN - OTHER'  											              :  'ASIAN',
                     'ASIAN - KOREAN'  											           :  'ASIAN',
                     'ASIAN - JAPANESE'  										              :  'ASIAN',
                     'ASIAN - THAI'  											              :  'ASIAN'    
                    }
    
    ethnic_group_df['ethnicity'] = ethnic_group_df['ethnicity'].map(ethnic_groups)
    
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