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
    
    def get_mortality(self):
        
        return query_database(MORTALITY_QUERY);
    
    def get_mortality_time(self):
        
        return query_database(MORTALITY_TIME_QUERY);
    
    def get_categorical_outcomes(self):
        
        mortality        = self._get_mortality();
        
        mortality.set_index('hadm_id', drop = True, inplace = True);
        return mortality;
    
    def get_numerical_outcomes(self):
        
        mortality_days   = self._get_mortality_time();
        readmission_days = self._get_readmission_time();
        
        patient_outcomes_dfs = [mortality_days, readmission_days];    
        numerical_outcomes = reduce(lambda left, right: pd.merge(left,right, on = 'hadm_id', how = 'outer'), patient_outcomes_dfs);
        numerical_outcomes.set_index('hadm_id', drop = True, inplace = True);
        return numerical_outcomes;




    
  