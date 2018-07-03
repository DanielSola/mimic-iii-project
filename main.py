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
from bokeh.plotting import figure, show, output_file
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
    
    def __init__(self):       
      self.demographic_data = demographic_data;

    def get_age_hist(self):
        
        age_hist, edges = np.histogram(self.demographic_data['age'], 
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
        
        return p1;
                
    def get_gender_pie_chart(self):
        
        genders = ["Male","Female"];
        gender_counts = [self.demographic_data.gender.value_counts()['M'], self.demographic_data.gender.value_counts()['F']];
      
        p2 = figure(x_range=(-1.2, 1.2), y_range=(-1.2, 1.2), title = 'Patient gender distribution');
        p2.wedge(x=0 , y=0, radius=1, start_angle=-0.5*pi, end_angle=(gender_counts[0]/(gender_counts[0] + gender_counts[1]))*pi, color="blue", legend = 'Male: 32950 (56%)');
        p2.wedge(x=0 , y=0, radius=1, start_angle=(gender_counts[0]/(gender_counts[0] + gender_counts[1]))*pi, end_angle=-0.5*pi, color="pink", legend = 'Female: 26026 (44%)');
        
        return p2;
    
    def get_marital_status_barplot(self):
        
        statuses = list(self.demographic_data.marital_status.value_counts().index);
        counts = list(self.demographic_data.marital_status.value_counts());
        source = ColumnDataSource(data=dict(statuses=statuses, counts=counts));
        p3 = figure(x_range=statuses, plot_height=600, plot_width=600, toolbar_location=None, title="Marital status counts");
        p3.vbar(x='statuses', top='counts', width=0.9, source=source, legend="statuses",
                line_color='white', fill_color=factor_cmap('statuses', palette=Spectral6, factors=statuses));
                          
        return p3;
    
    def get_ethnicity_barplot(self):
        
        ethnicities = list(self.demographic_data.ethnicity.value_counts().index);
        counts = list(self.demographic_data.ethnicity.value_counts());
        source = ColumnDataSource(data=dict(ethnicities=ethnicities, counts=counts));
        p4 = figure(x_range=ethnicities, plot_height=600, plot_width=600, toolbar_location=None, title="Ethnicity counts");
        p4.vbar(x='ethnicities', top='counts', width=0.9, source=source, legend="ethnicities",
                line_color='white', fill_color=factor_cmap('ethnicities', palette=Spectral6, factors=ethnicities));
                          
        return p4;
    
    def get_religion_pie_chart(self):

        religions = ['CHRISTIAN','NONE', 'JEWISH/HEBREW', 'ORTHODOX', 'BUDDHIST/HINDU', 'MUSLIM'];
        religion_counts = [self.demographic_data.religion.value_counts()['CHRISTIAN'],
                           self.demographic_data.religion.value_counts()['NONE'],
                           self.demographic_data.religion.value_counts()['JEWISH/HEBREW'],
                           self.demographic_data.religion.value_counts()['ORTHODOX'],
                           self.demographic_data.religion.value_counts()['BUDDHIST/HINDU'],
                           self.demographic_data.religion.value_counts()['MUSLIM']];
        total_count = self.demographic_data.religion.count();
        
        p5 = figure(x_range=(-1.2, 1.2), y_range=(-1.2, 1.2), title = 'Patient religion distribution');      
        christian_end_angle = (religion_counts[0]/total_count)*2*pi;
        p5.wedge(x=0 , y=0, radius=1, start_angle=0, end_angle=christian_end_angle, color="blue", legend = 'Christian: 29323 (49.7%)');      
        none_end_angle = christian_end_angle + (religion_counts[1]/total_count)*2*pi;
        p5.wedge(x=0 , y=0, radius=1, start_angle=christian_end_angle, end_angle=none_end_angle , color="pink", legend = 'None: 23176 (39.3%)');      
        jewish_end_angle = none_end_angle + (religion_counts[2]/total_count)*2*pi;        
        p5.wedge(x=0 , y=0, radius=1, start_angle=none_end_angle, end_angle=jewish_end_angle , color="green", legend = 'Jewish/Hebrew: 5330 (9%)');        
        orthodox_end_angle = jewish_end_angle + (religion_counts[3]/total_count)*2*pi;       
        p5.wedge(x=0 , y=0, radius=1, start_angle=jewish_end_angle, end_angle=orthodox_end_angle , color="yellow", legend = 'Orthodox: 542 (0.91%)');       
        buddhist_end_angle = orthodox_end_angle + (religion_counts[4]/total_count)*2*pi;   
        p5.wedge(x=0 , y=0, radius=1, start_angle=orthodox_end_angle, end_angle=buddhist_end_angle , color="magenta", legend = 'Buddhist/Hindu: 380 (0.64%)');
        p5.wedge(x=0 , y=0, radius=1, start_angle=buddhist_end_angle, end_angle=0 , color="cyan", legend = 'Muslim: 225 (0.38%)');

        return p5;
        
    
    def plot_figures(figures):
        
        output_file("demographic-plots.html", title="Demographic data plots");
        
        grid = gridplot(figures);

        show(grid);
        
PlottingService.demographic_data = demographic_data = DemographicData().get_demographic_data();
figure1 = PlottingService().get_age_hist();
figure2 = PlottingService().get_gender_pie_chart();
figure3 = PlottingService().get_marital_status_barplot();
figure4 = PlottingService().get_ethnicity_barplot();
figure5 = PlottingService().get_religion_pie_chart();

PlottingService.plot_figures([[figure1, figure3, figure2 ], [figure4, figure5]]);
#PlottingService().plot_figures([[figure1, None, None], [None, None]]);