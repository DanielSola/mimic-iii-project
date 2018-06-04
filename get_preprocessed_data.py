# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 19:48:15 2018

@author: Tiendeo
"""

import importlib
from resources import queries
from services import preprocessing_service
from services.query_service import query_database
import pandas as pd

importlib.reload(preprocessing_service)


def get_services():
    
    services = query_database(queries.SERVICE_QUERY)
        
    relevant_services_list = list(services.apply(lambda x: preprocessing_service.get_relevant_admission_service(x['hadm_id'], services), axis = 1))
    
    relevant_services_df = pd.DataFrame(relevant_services_list, columns = ['hadm_id','service'])
    
    return relevant_services_df.groupby("hadm_id").first()
    

def get_ages():
    
    ages = query_database(queries.AGE_QUERY + ' LIMIT 100')
    
    return ages.apply(lambda x: x['age'] if x['age'] < 300 else 91.4, axis = 1)
    
def get_genders():
    
    return query_database(queries.GENDER_QUERY + ' LIMIT 100')
	

def get_marital_status():
    
    marital_status_df = query_database(queries.MARITAL_STATUS_QUERY)
    
    return preprocessing_service.group_marital_status(marital_status_df)

