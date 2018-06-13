# -*- coding: utf-8 -*-

import sys
import pandas as pd
import os, sys

all_data = []
#Import all csv files in mimic_data folder
for root, dirs, files in os.walk(os.getcwd()+'/mimic_data'):
    for name in files:
        if name.endswith('.csv'):
            imported_data = pd.read_csv(root + '/' + name, sep = '\t')
            all_data.append(imported_data)
            
