#!/usr/bin/env python
# coding: utf-8

# #### Show the common numbers for $x^2=y^3$
# 
# [Link](https://www.quora.com/Is-64-the-first-perfect-square-and-a-perfect-cube-Is-it-the-only-one/answer/Alon-Amit?ch=3&share=e27e1c03&srid=iBLa) to Quora (Alon Amit's answer)
# 
# 
# 

# In[1]:


import numpy
import sympy
import pandas
import csv
import matplotlib.pyplot as plt
import seaborn as sn # to draw plots
import plotly.express as px


# In[2]:


import keyword
print(keyword.kwlist) # A list of all 33 keywords in python


# In[68]:


list1 = [] # for all sqaured values
list2 = [] # for all cubed values

n = 100    # till what values of n to check


for i in range(0,n): # if i is in the above given range
    j=i**2 
    k=i**3
    list1.append(j) # add the squared values to list1
    list2.append(k) # add the cubed values to list2
    
elem = set(list1) & set(list2) # check if an element is on both "list1" and "list2"
print(elem) # print the list

# print(set(list1)) # if you want to see the list as a set

    


# In[ ]:





# In[ ]:




