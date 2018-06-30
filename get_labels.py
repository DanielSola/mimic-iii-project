# -*- coding: utf-8 -*-

import importlib
from resources.queries import *
from resources.mappings import *
from services.preprocessing_service import *
from services import preprocessing_service
from services.query_service import query_database
import pandas as pd
from functools import reduce
import numpy as np

class PatientOutcomes():
    
    def _get_mortality(self):
        
        return query_database(MORTALITY_QUERY);

    def _get_readmissions(self):
        
        admissions_data = query_database(ADMISSION_DATA_QUERY);
        
        return extract_readmissions(admissions_data);
    
    def _get_readmission_time(self):
        
        admissions_data = query_database(ADMISSION_DATA_QUERY);
        
        return extract_readmission_time(admissions_data);
    
    def _get_mortality_time(self):
        
        return query_database(MORTALITY_TIME_QUERY);
    
    def get_patient_outcomes(self):
        
        mortality        = self._get_mortality();
        mortality_days   = self._get_mortality_time();
        readmission     = self._get_readmissions();
        readmission_days = self._get_readmission_time();
        
        patient_outcomes = [mortality, mortality_days, readmission, readmission_days];
        
        return reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id', how = 'outer'), patient_outcomes);

        
    
  