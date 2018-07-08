import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

class PlottingService():
    
    def plot_kde(self, data, title, xlabel, ylabel):
        ax = sns.kdeplot(data, shade = True);
        ax.set_title(title);
        ax.set_xlabel(xlabel);
        ax.set_ylabel(ylabel);
        
    def plot_hist(self, data, title, xlabel, ylabel, bins):
        ax = sns.distplot(data, kde = False, bins = bins);
        ax.set_title(title);
        ax.set_xlabel(xlabel);
        ax.set_ylabel(ylabel);
        
    def plot_countplot(self, data, title, xlabel, ylabel):
        
        ax = sns.countplot(data);
        ax.set_title(title);
        ax.set_xlabel(xlabel);
        ax.set_ylabel(ylabel);
        plt.xticks(rotation=50)
        
    def jointplot(self, x_data, y_data, xlabel, ylabel):
        
        data = pd.DataFrame([x_data, y_data]).T;
        data.columns = [xlabel, ylabel];

        ax = sns.jointplot(x = data.columns[0], y = data.columns[1], data=data,  kind="kde");
        ax.set_title(title);
        ax.set_xlabel(xlabel);
        ax.set_ylabel(ylabel);



        
