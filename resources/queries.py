"""
MIMIC-III Project 

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
                            WHERE seq_num = 1"""
                            
PROC_ICD9_CODES_QUERY = """ SELECT hadm_id, procedures_icd.icd9_code
                            FROM procedures_icd 
                            INNER JOIN d_icd_procedures
                            ON procedures_icd.icd9_code = d_icd_procedures.icd9_code
                            WHERE hadm_id is not null
                            AND seq_num = 1"""
                            
ICU_LOS_QUERY = """SELECT hadm_id, sum(los) AS total_icu_time 
                   FROM icustays
                   GROUP BY hadm_id
                   ORDER BY hadm_id"""
                   
TOTAL_LOS_QUERY = """SELECT hadm_id, 
                     EXTRACT(epoch FROM(dischtime - admittime))/(3600*24) AS total_los_days
                     FROM admissions"""
                
PREVIOUS_ADMISSIONS_QUERY = """SELECT hadm_id, subject_id, admittime
                               FROM admissions
                               ORDER BY admittime ASC"""
                               
PROCEDURE_COUNT_QUERY = """SELECT hadm_id, count(*) AS procedure_count
                           FROM procedures_icd
                           GROUP BY hadm_id"""
                            
MECHANICAL_VENTILATION_TIME_QUERY = """SELECT hadm_id, SUM(duration_hours) AS total_mech_vent_time
                                       FROM ventdurations v
                                       INNER JOIN icustays i
                                       ON v.icustay_id = i.icustay_id
                                       GROUP BY hadm_id"""
                                        
SEVERITY_SCORES_QUERY = """SELECT o.hadm_id, AVG(o.oasis) AS oasis_avg, AVG(so.sofa) AS sofa_avg, AVG(sa.saps) as saps_avg
                           FROM oasis o
                           INNER JOIN sofa so
                           ON o.hadm_id = so.hadm_id
                           INNER JOIN saps sa
                           ON sa.hadm_id = so.hadm_id
                           GROUP BY o.hadm_id"""
                           
GLASGOW_COMA_SCALE_QUERY = """SELECT hadm_id, AVG(gcs) AS GCS
                              FROM pivoted_gcs gcs
                              INNER JOIN icustays i
                              ON gcs.icustay_id = i.icustay_id
                              GROUP by hadm_id"""
                           
MORTALITY_QUERY = """   
                        SELECT hadm_id,
                        CASE 
    									WHEN 
                                      EXTRACT(epoch FROM (dod-dischtime))/(3600*24*30) >= 12
         
    									THEN '12+ months'
    							
                        	WHEN 
                        		EXTRACT(epoch FROM (dod-dischtime))/(3600*24*30) < 12 AND
    								EXTRACT(epoch FROM (dod-dischtime))/(3600*24*30) >= 1

                        	THEN '1-12 months'
    									
									WHEN
										EXTRACT(epoch FROM (dod-dischtime))/(3600*24*30) < 1 AND
										EXTRACT(epoch FROM (dod-dischtime))/(3600*24*30) > -0.5
									THEN '0-1 months'	
									
									END

                        AS mortality
                        FROM admissions a
                        INNER JOIN patients p
                        ON a.subject_id = p.subject_id
                        WHERE p.expire_flag = 1
                 """
                                 
                                
ADMISSION_DATA_QUERY = """SELECT hadm_id, p.subject_id, admittime, dischtime
                        FROM admissions a
                        INNER JOIN patients p
                        ON a.subject_id = p.subject_id
                        WHERE EXTRACT(epoch FROM (a.admittime - p.dob)) / (365 * 24 * 3600) BETWEEN 18 AND 80
                        ORDER BY subject_id ASC"""
                            
MORTALITY_TIME_QUERY = """SELECT hadm_id, EXTRACT(epoch FROM (dod-dischtime))/(3600*24) AS expire_days
                            FROM admissions a
                            INNER JOIN patients p
                            ON a.subject_id = p.subject_id
							    WHERE EXTRACT(epoch FROM (dod-dischtime))/(3600*24) > 0.5
                            AND p.expire_flag = 1"""

HOSPITAL_EXPIRE_FLAG_QUERY = """SELECT hadm_id, hospital_expire_flag
                                FROM admissions"""