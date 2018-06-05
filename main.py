# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 21:51:04 2018

@author: Daniel Solá
"""

import sys
import os
from get_preprocessed_data import *

sys.path.insert(0, os.path.dirname(os.path.realpath('__file__')))

    
demographic_data = DemographicData().get_demographic_data()

lab_data         = LaboratoryMeasures().get_lab_data()
