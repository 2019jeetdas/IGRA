# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

# [A] Country list data processing 

# Reading and converting to CSV file

country_list = pd.read_table('/home/jeet/Desktop/IGRA-Data-description/igra2-country-list.txt')
country_list.to_csv("/home/jeet/Desktop/IGRA-Data-description/igra2-country-list.csv", encoding='utf-8',sep=' ',index=False)

# Reading the newly created CSV file

country_list = pd.read_csv("/home/jeet/Desktop/IGRA-Data-description/igra2-country-list.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("\t Country list for IGRA project:")
print("\n-----------------------------------\n")

#-------- Question-00 --------------------

# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",country_list.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in country_list.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

print(country_list)


#[B]processing station list

# Reading and converting to CSV file

station_list = pd.read_table('/home/jeet/Desktop/IGRA-Data-description/igra2-station-list.txt')
station_list.to_csv("/home/jeet/Desktop/IGRA-Data-description/igra2-station-list.csv", encoding='utf-8',sep=' ',index=False)

# Reading the newly created CSV file

station_list = pd.read_csv("/home/jeet/Desktop/IGRA-Data-description/igra2-station-list.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("\t Station list for IGRA project:")
print("\n-----------------------------------\n")

list(open('/home/jeet/Desktop/IGRA-Data-description/igra2-station-list.txt'))

#[C] US state list

# Reading and converting to CSV file

state_list = pd.read_table('/home/jeet/Desktop/IGRA-Data-description/igra2-us-states.txt')
state_list.to_csv("/home/jeet/Desktop/IGRA-Data-description/igra2-us-states.csv", encoding='utf-8',sep=' ',index=False)

# Reading the newly created CSV file

state_list = pd.read_csv("/home/jeet/Desktop/IGRA-Data-description/igra2-us-states.csv", encoding='utf-8')  

print("\n------- output data :-----------\n")
print("\t State list of US for IGRA project:")
print("\n-----------------------------------\n")

list(open('/home/jeet/Desktop/IGRA-Data-description/igra2-us-states.txt'))

#-------------------- data center - 1---------------------------

data_center_1 = pd.read_table('/home/jeet/Desktop/ACM00078861-data.txt')
data_center_1.to_csv("/home/jeet/Desktop/ACM00078861-data.csv", encoding='utf-8',sep=',',index=False)



# importing pandas module  
import pandas as pd 
   
# reading csv file from url  
data = pd.read_csv("/home/jeet/Desktop/ACM00078861-data.csv") 
  
# dropping null value columns to avoid errors 
data.dropna(inplace = True) 
  
# new data frame with split value columns 
new = data["#ACM00078861 1947 01 08 01 9999   10 ncdc6310           171170  -617830"].str.split(" ", n = 1, expand = True) 
  
# making separate first name column from new data frame 
data["column-1"]= new[0] 
  
# making separate last name column from new data frame 
data["column-2"]= new[1] 
  
# Dropping old Name columns 
data.drop(columns =["#ACM00078861 1947 01 08 01 9999   10 ncdc6310           171170  -617830"], inplace = True) 
  
# df display 
data 

