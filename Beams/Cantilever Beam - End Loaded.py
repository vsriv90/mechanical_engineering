#!/usr/bin/env python
# coding: utf-8

# # Cantilever beams - End Loaded

# ![Cantilever%20-%20End%20Loaded.jpeg](attachment:Cantilever%20-%20End%20Loaded.jpeg)

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn # to draw plots
# import plotly.express as px
# import csv
# import sympy

from PIL import Image

# SIMPLY SUPPORTED BEAM - Single Load: PARAMETERS

f = 700 # Value of load
l = 100 # Total length of beam

UnitF = str('N') # To show units of force
UnitL = str("mm") # To show units of length


# In[16]:


x = [0,l] 
y = [0,0] 

# plotting the points on X axis
plt.plot(x, y,label = "Beam", color='green', linewidth = 10,marker='o', markerfacecolor='blue', markersize=15) 
plt.legend() # giving a legend to my graph

##################### ENTERING LOADS TO GRAPH #####################
# fig,ax = plt.subplots(1)

AvX = [0,0] # x-axis values
AvY = [f/2,-f/2] # corresponding y-axis values
plt.plot(AvX, AvY, linestyle='--',marker='s',markersize=10, color='grey') # To create the reaction line 
plt.text(1,-f,str(round(f,2))+UnitF)  # To show the values on the points
 
LoadX = [l,l] 
LoadY = [0,f] 
 
plt.plot(LoadX, LoadY, linestyle='--',marker='v',markersize=10)  # To create the force line 
plt.text(l,f+1,str(round(f,2))+UnitF) # (Coordiante x, Coordinate y,the value in text+Unit)

SupportX = [0]
SupportY = [0]
plt.plot(SupportX, SupportX,marker='s',markersize=25)  # To create the force line 
plt.text(-2,20,"RIGID") # (Coordiante x, Coordinate y,the text)

#################### End of load entering ###########################

# AXIS LEGENDS 

plt.xlabel('Beam length in '+ UnitL)
plt.title('Loads on beam') # giving a title to graph 

plt.ylim(top=1.5*f) # to set maximum y-axis value
plt.ylim(bottom=-1.5*f) # to set minimum y-axis value

plt.gca().axes.get_yaxis().set_visible(False) # Make y-aixs values visible or invisible
plt.show() # function to show the plot 

# ---------------------------------------------------------------------
# SHEAR FORCE DIAGRAM

ShearX = [0,0,l,l] 
ShearY = [0,f,f,0] 
plt.plot(ShearX, ShearY, linestyle='--', marker='o')  #plotting the points on X axis

# To show the values on the points
plt.text(0,0,str(0)+UnitF)  # (Coordiante x, Coordinate y,the value in text+Unit) # point 1
plt.text(0,f,str(round(f,2))+UnitF) # point 2, with integers rounded off
plt.text(l,f,str(round(f,2))+UnitF)  # point 3
plt.text(l,0,str(0)+UnitF) # point 4

# Plotting the 0 line
ZeroLX = [0,l] 
ZeroLY = [0,0] 
plt.plot(ZeroLX, ZeroLY, color='black') # plotting the line 2 points 

# OVERALL DETAILS FOR THE GRAPH
plt.xlabel('Position along the beam')
plt.title('Shear/Transverse Force Diagram') # giving a title to graph 
plt.gca().axes.get_yaxis().set_visible(False) # Make y-aixs values visible or invisible
plt.show() # function to show the plot 

# ---------------------------------------------------------------------
# BENDING MOMENT DIAGRAM

MomX = [0,0,l] 
MomY = [0,f*l,0] 
plt.plot(MomX, MomY, linestyle=':', marker='o', label="Moment direction = Counter-clockwise") # plotting the points on X axis
plt.legend() #legend to show direction of moment

plt.text(0,0,str((0)))  # (Coordiante x, Coordinate y,the value in text+Unit) # point 1
plt.text(0,f*l,str(round((f*l),2))+UnitF+UnitL)  # To SHOW the Moment value at the point # point 2
plt.text(l,-10,str((0))) # point 3

plt.plot(ZeroLX, ZeroLY, color='black')

# OVERALL DETAILS FOR THE GRAPH
plt.xlabel('Position along the beam')
plt.title('Bending Moment Diagram') # giving a title to graph 
plt.gca().axes.get_yaxis().set_visible(False) # Make y-aixs values visible or invisible         
plt.show() # function to show the plot 


# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

# In[ ]:





# In[49]:


# help(plt.plot)


# In[ ]:




