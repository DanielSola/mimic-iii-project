# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 21:51:04 2018

@author: Daniel Solá
"""

import sys
import os
from get_preprocessed_data import *
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.realpath('__file__')))

##DemographicData().get_demographic_data();
##Measures().get_lab_data();
##Measures().get_physio_data();
a = AdministrativeData().get_total_length_of_stay();