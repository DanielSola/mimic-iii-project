import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class PlottingService():
    sns.set_style("darkgrid");
    
    def plot_kde(self, data, title, xlabel, ylabel, xlimit):
        filtered_data = data[data < xlimit]
        ax = sns.kdeplot(filtered_data, shade = True);
        ax.set_title(title);
        ax.set_xlabel(xlabel);
        ax.set_ylabel(ylabel);
        
    def plot_hist(self, data, title, xlabel, ylabel, bins, xlimit):
        filtered_data = data[data < xlimit]
        ax = sns.distplot(filtered_data, kde = False, bins = bins);
        ax.set_title(title);
        ax.set_xlabel(xlabel);
        ax.set_ylabel(ylabel);
        
    def plot_countplot(self, data, title, xlabel, ylabel):
        
        ax = sns.countplot(data, orient);
        ax.set_title(title);
        ax.set_xlabel(xlabel);
        ax.set_ylabel(ylabel);
        plt.xticks(rotation=45)
        
    def jointplot(self, x_data, y_data, xlabel, ylabel):
        
        data = pd.DataFrame([x_data, y_data]).T;
        data.columns = [xlabel, ylabel];

        ax = sns.jointplot(x = data.columns[0], y = data.columns[1], data=data,  kind="kde");
        ax.set_title(title);
        ax.set_xlabel(xlabel);
        ax.set_ylabel(ylabel);
    
    def boxplot(self, data, title, xlabel, ylabel):
        
        ax = sns.boxplot(data, shade = True);
        ax.set_title(title);
        ax.set_xlabel(xlabel);
        ax.set_ylabel(ylabel);



        
