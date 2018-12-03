# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 17:26:01 2018

@author: linlinice
"""

# import numpy library as np
import numpy as np
import datetime
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


#read edge data
df = pd.read_csv('Z:\\Dropbox\\class\\GGS590\\project\\data\\Gowalla_edges.txt', sep="\t", header=None)
df.columns = ["user", "frined"]
#load data into networkx
g = nx.from_pandas_edgelist(df, source='user', target='frined') 
#drawing the graph -not working maybe dataset too large?
#nx.draw(g)
#plt.savefig("simple_path.png") # save as png
#plt.show() # display

#print("short distance:" +nx.shortest_path_length(g, source=196577, target=196576))
#print("short distance:" +nx.shortest_path_length(g, source=196577, target=122))

data = pd.read_csv('Z:\\Dropbox\\class\\GGS590\\project\\data\\Gowalla_totalCheckins.txt', sep="\t", header=None)
data.columns = ["user", "time", "lat", "lon", "loc"]    
data['time'] =  pd.to_datetime(data['time'])
data= data.set_index('time')


