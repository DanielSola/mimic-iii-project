"""
MIMIC-III Project
@author: Daniel Solá
"""
import pandas as pd
import sys
import os
from get_features import *
from get_labels import *
import pandas as pd
from bokeh.plotting import figure
from bokeh.io import gridplot, output_file, show
from bokeh.layouts import row
from bokeh.layouts import gridplot
from bokeh._legacy_charts import Donut
sys.path.insert(0, os.path.dirname(os.path.realpath('__file__')));

demographic_data = DemographicData().get_demographic_data();
severity_scores = Measures().get_severity_scores();
ventilation_time = Measures().get_mechanical_ventilation_time();
lab_data = Measures().get_lab_data();
physio_data = Measures().get_physio_data();
administrative_data = AdministrativeData().get_administrative_data();


labels = PatientOutcomes().get_patient_outcomes();

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
            
            gender_data = pd.Series(gender_counts, index = genders);
            p2 = Donut(gender_data);

            grid = gridplot([[p1, p2], [None, None]]);

            show(grid);