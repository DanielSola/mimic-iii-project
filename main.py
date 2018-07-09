"""
MIMIC-III Project
@author: Daniel Solá
"""
from collections import Counter
import pandas as pd
import sys
import os
from get_features import *
from get_labels import *
from services.plotting_service import *
import pandas as pd
import seaborn as sns
sys.path.insert(0, os.path.dirname(os.path.realpath('__file__')));
from numpy import pi
import matplotlib as mplc
import matplotlib.pyplot as plt
#icu_data = ICUData().get_icu_data();
#severity_scores = Measures().get_severity_scores();
#ventilation_time = Measures().get_mechanical_ventilation_time();
#lab_data = Measures().get_lab_data();
#physio_data = Measures().get_physio_data();
icu_data = ICUData().get_icu_data();
#labels = PatientOutcomes().get_patient_outcomes();

        
icd9_groups = icu_data.icd9_group.value_counts(
        )

