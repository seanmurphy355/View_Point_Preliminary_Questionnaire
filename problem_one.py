# -*- coding: utf-8 -*-
"""Problem_One.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vtUZDYN4DJ5cpl_OiTeDaqR1DKdUeeGd
"""

import numpy as np
import pandas as pd
from pandas import DataFrame 

# df_One is = the data frame version of the name_tables table that was given in the problem. (one change is that this data frame version does contain a index on the left hand side.)
df_One = pd.DataFrame(
    [['V001','Abe'],
    ['V002','Abhay'],
    ['V003','Acelin'],
    ['V004','Adelphos']],
    columns = ['StudentID','Name'])

# data frame version of mark_table
df_Two = pd.DataFrame(
    [['V001',95],
    ['V002',80],
    ['V003',74],
    ['V004',81]],
    columns = ['StudentID','Total_marks'])

#part B 
def CaseConverter(data_Frame):

  #Convert our data into an array
  data_Frame = np.array(data_Frame)

  #Find what we need to change
  for data in range (0,4):
      if "e" in data_Frame[data][1]:
        data_Frame[data][1] = data_Frame[data][1].upper()
      if "E" in data_Frame[data][1]:
        data_Frame[data][1] = data_Frame[data][1].upper()
      else:
        data_Frame[data][1] = data_Frame[data][1].lower()

  #convert everything baack to a data frame
  Case_Frame =  pd.DataFrame({'StudentID': data_Frame[:,0],'Name': data_Frame[:,1]})
  return Case_Frame

#Run and print results
Case_Frame = CaseConverter(df_One)
print("Results for part B")
print (Case_Frame)
print('\n')

#function for solving part C
def convertedTable(df_Two,Case_Frame):

  #convert our data into a merged data table
  results = pd.merge(Case_Frame, df_Two, how ='inner')
  return results

#Call convertedTable to do work
Part_C = convertedTable(df_Two,Case_Frame)
print("Results for part C")
print(Part_C)

