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
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.layouts import row
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap
from bokeh.palettes import Spectral6

sys.path.insert(0, os.path.dirname(os.path.realpath('__file__')));
from numpy import pi

#demographic_data = DemographicData().get_demographic_data();
#severity_scores = Measures().get_severity_scores();
#ventilation_time = Measures().get_mechanical_ventilation_time();
#lab_data = Measures().get_lab_data();
#physio_data = Measures().get_physio_data();
#administrative_data = AdministrativeData().get_administrative_data();


#labels = PatientOutcomes().get_patient_outcomes();

class PlottingService():
    
    def plot_demographic_data():
        
        demographic_data = DemographicData().get_demographic_data();
        
            #Age histogram
    
            age_hist, edges = np.histogram(demographic_data['age'], 
                               bins = 17, 
                               range = [0, 90])
            ages = pd.DataFrame({'age': age_hist, 
                       'left': edges[:-1], 
                       'right': edges[1:]});

            p1 = figure(plot_height = 600, plot_width = 600, 
                       title = 'Histogram of Patient age at admission',
                       x_axis_label = 'Age (years)', 
                       y_axis_label = 'Number of patients');
                        
            p1.quad(bottom=0, top=ages['age'], 
                    left=ages['left'], right=ages['right'], 
                    fill_color='red', line_color='black');
                    
            #Gender pie chart
            genders = ["Male","Female"];
            gender_counts = [demographic_data.gender.value_counts()['M'], demographic_data.gender.value_counts()['F']];
          
            p2 = figure(x_range=(-1.2, 1.2), y_range=(-1.2, 1.2), title = 'Patient gender distribution');
            p2.wedge(x=0 , y=0, radius=1, start_angle=-0.5*pi, end_angle=(gender_counts[0]/(gender_counts[0] + gender_counts[1]))*pi, color="blue", legend = 'Male: 32950 (56%)');
            p2.wedge(x=0 , y=0, radius=1, start_angle=(gender_counts[0]/(gender_counts[0] + gender_counts[1]))*pi, end_angle=-0.5*pi, color="pink", legend = 'Female: 26026 (44%)');

            #Marital status barplot
            
            statuses = list(demographic_data.marital_status.value_counts().index);
            counts = list(demographic_data.marital_status.value_counts());
            source = ColumnDataSource(data=dict(statuses=statuses, counts=counts));
            p3 = figure(x_range=statuses, plot_height=600, plot_width=600, toolbar_location=None, title="Marital status counts");
            p3.vbar(x='statuses', top='counts', width=0.9, source=source, legend="statuses",
                    line_color='white', fill_color=factor_cmap('statuses', palette=Spectral6, factors=statuses));
                              
            grid = gridplot([[p1, p2, p3], [None, None]]);

            show(grid);