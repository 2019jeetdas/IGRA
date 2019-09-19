# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#[B]processing station list

# Reading and converting to CSV file

station_list = pd.read_table('/home/jeet/Desktop/IGRA-Data-description/igra2-station-list.txt')
station_list.to_csv("/home/jeet/Desktop/IGRA-Data-description/igra2-station-list.csv")

# Reading the newly created CSV file

sl = pd.read_csv("/home/jeet/Desktop/IGRA-Data-description/igra2-station-list.csv")  

print("\n------- output data :-----------\n")
print("\t Station list for IGRA project:")
print("\n-----------------------------------\n")

#-------splitting the text file -------------  
 
data = sl[0:2688] 

for i in range(0,101):
     print(i,'--->',data[0:i])

