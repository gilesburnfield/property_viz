# -*- coding: utf-8 -*-
"""
Created on Wed Jun 18 20:01:15 2014

@author: Giles
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
    return df
    
def convert_date(d):
    return dtdt.strptime(d, "%d.%m.%Y")

df = readcsv(filename)
    
df['Period'] = df.Period.apply(convert_date)

# make wide data long


col_list = df.columns.values.tolist()[1:1000]
df_long = pd.melt(df,"Period", col_list, var_name='Country' )


print df_long

df_long = df_long[df_long['Country'].isin(['Q:US','Q:GB','Q:AU','Q:FR' ])]







##

# GG plot

print ggplot(df_long, aes(x='Period', y='value', color = 'Country')) + geom_point() + geom_line() 
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

    
    
    
    
    
   







