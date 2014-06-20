# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 20:01:15 2014

@author: Giles b
"""

import numpy as np
import pandas as pd
from datetime import datetime as dtdt

from ggplot import *

import os

###  Read in data 

from bokeh.plotting import *

os.chdir('/Users/Giles/Dropbox/Anylsis/International Property')


filename = 'pp_long.csv'
def readcsv(filename):
    df = pd.read_csv(filename)
    df= df.rename(columns=lambda x: x.strip())
    df['Period']= df['Period'].apply(lambda d: dtdt.strptime(d, "%d.%m.%Y"))
    
    return df
    
df = readcsv(filename)    

def reshape(df):
    col_list = df.columns.values.tolist()[1:1000]
    return pd.melt(df,"Period", col_list, var_name='Country' )

df_long = reshape(df)
     
"""    
    return df
    
def convert_date(d):
    return dtdt.strptime(d, "%d.%m.%Y")

df = readcsv(filename)
    
df['Period'] = df.Period.apply(convert_date)

"""

# make wide data long


#col_list = df.columns.values.tolist()[1:1000]
#df_long = pd.melt(df,"Period", col_list, var_name='Country' )
#print df_long


Countrylist= ['Q:US','Q:GB','Q:AU','Q:FR']


df_long = df_long[df_long['Country'].isin(Countrylist)]


start_date = "1980-12-31"
end_date = "2013-12-31"



# Date format  1980-12-31
def tp(df_long, start_date, end_date ):
    
    start = dtdt.strptime(start_date, "%Y-%m-%d")
    end = dtdt.strptime(end_date, "%Y-%m-%d")
    
    return df_long[(df_long['Period'] >= start) & (df_long['Period'] <=end)]
    
    
print tp(df_long,"1980-12-31","2006-11-14")




class Statgb:
    def __init_(self,mean,sd,period_growt):
        self.mean = self.calc_mean
        self.sd = self.calc_SD
        self.period_growth = self.calc_period_growth
        
        
        
def calc_mean(a):
    return a.mean()
    
def calc_SD(a):
    return a.std()  
 

  

def calc_period_growth(start_date, end_date) :   
    
    
    start = dtdt.strptime(start_date, "%Y-%m-%d")
    end = dtdt.strptime(end_date, "%Y-%m-%d")
    
    # when i have multiple value columns i would like to have to have value as an updating object from a loop. or as flat file another condtional staement
    value_var_start = df_long[['value','Country']][df_long['Period']==start]
    value_var_end = df_long[['value','Country']][df_long['Period']==end]
    
    # Growth is outpting all starts dates.. e.g for each country.. HOw do you remove the index coolumns and multiply the vectors?
    
    return value_var_start, value_var_end
    
    
    
    pd.DataFrame(df2)
    

    
    
start, end = calc_period_growth(start_date, end_date)
print start, end
    

df2=(start['value'].values - (end['value'].values)/start['value'].values)
    

        
        
        
        
        
        
        
        

        
        
        



#mean = df_long_test['value'].sum()














#& (df_long['Period'] <= 2005-03-31)


# GG plot

#print ggplot(df_long, aes(x='Period', y='value', color = 'Country')) + geom_point() + geom_line() 
#Plot = Plot + ggtitle('Number of Home Runs by year') + xlab('Year') + ylab('Home Runs')



"""
## Plot on bokeh
    
output_file("stocks.html", title="stocks.py example")
   
hold()

line(
    df['Period'],                                       # x coordinates
    df['Q:AU'], 
    df['Q:US'],                                 # y coordinates
    color='#A6CEE3',                                    # set a color for the line
    legend='Metric',                                      # attach a legend label
    x_axis_type = "datetime",                           # NOTE: only needed on first
    tools="pan,wheel_zoom,box_zoom,reset,previewsave"   # NOTE: only needed on first
)
    
show()


"""

    
    
    
    
    
   







