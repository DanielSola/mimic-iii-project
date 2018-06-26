# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 19:50:42 2018

@author: Daniel Solá
"""

AGE_QUERY = """SELECT hadm_id, EXTRACT(epoch FROM (admittime - dob))/(3600*24*365)
               AS age
               FROM admissions a
               INNER JOIN patients p
               ON a.subject_id = p.subject_id"""
               
GENDER_QUERY = """SELECT hadm_id, gender
                  FROM admissions a
                  INNER JOIN patients p
                  ON a.subject_id = p.subject_id"""
               
               
MARITAL_STATUS_QUERY = """SELECT hadm_id, marital_status 
                          FROM admissions a
                          INNER JOIN patients p
                          ON a.subject_id = p.subject_id"""
                          
RELIGION_QUERY = """SELECT hadm_id, religion 
                    FROM admissions a
                    INNER JOIN patients p
                    ON a.subject_id = p.subject_id"""       

ETHNICITY_QUERY = """SELECT hadm_id, ethnicity 
                    FROM admissions a
                    INNER JOIN patients p
                    ON a.subject_id = p.subject_id"""             

                         
                
SERVICE_QUERY = """SELECT hadm_id, curr_service
                    FROM services
                    ORDER BY hadm_id ASC"""
                    
DIAG_ICD9_CODES_QUERY = """SELECT hadm_id, diagnoses_icd.icd9_code
                            FROM diagnoses_icd 
                            INNER JOIN d_icd_diagnoses 
                            ON diagnoses_icd.icd9_code = d_icd_diagnoses.icd9_code
                            WHERE seq_num = 1"""