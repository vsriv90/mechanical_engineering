#!/usr/bin/env python
# coding: utf-8

# # Simply supported beams - End Load

# ![Simply%20supported%20beams%20-%20End%20Loaded.jpeg](attachment:Simply%20supported%20beams%20-%20End%20Loaded.jpeg)

# In[3]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn # to draw plots
# import plotly.express as px
# import csv
# import sympy

from PIL import Image

# SIMPLY SUPPORTED BEAM - Single Load: PARAMETERS

f = 50 # Value of load

l = 50 # Total length of beam
a = 35 # distance from left end of beam
b = (l-a) # distance from right end of beam

UnitF = str('N') # To show units of force
UnitL = str("mm") # To show units of length


# In[5]:


x = [0,a,l] 
y = [0,0,0] 

# plotting the points on X axis
plt.plot(x, y,label = "Beam", color='green', linewidth = 10,marker='o', markerfacecolor='blue', markersize=15) 
plt.legend() # giving a legend to my graph

##################### ENTERING LOADS TO GRAPH #####################
# fig,ax = plt.subplots(1)

AvX = [0,0] 
AvY = [0,-f*b/a] 

plt.plot(AvX, AvY, linestyle='--',marker='^',markersize=10,color="grey") # To create the reaction line 
plt.text(1,-f*b/l,str(round((-f*b/a),2))+UnitF)  # To show the values on the points


BvX = [a,a] 
BvY = [0,-f*l/a] 
 
plt.plot(BvX, BvY, linestyle='--',marker='^',markersize=10,color="grey") # To create the reaction line 
plt.text(a-(a/10),-f*l/a,str(round((f*l/a),2))+UnitF) # (Coordiante x, Coordinate y,the value in text+Unit)


LoadX = [l,l] 
LoadY = [0,f] 
 
plt.plot(LoadX, LoadY, linestyle='--',marker='v',markersize=10,color="orange")  # To create the force line 
plt.text(l,f+10,str(round((f),2))+UnitF) # (Coordiante x, Coordinate y,the value in text+Unit)


#################### End of load entering ###########################

# AXIS LEGENDS 

plt.xlabel('Beam length in '+ UnitL)
plt.ylabel('Values in legend')

plt.title('Loads on beam') # giving a title to graph 

plt.ylim(top=2*f) # to set maximum y-axis value
plt.ylim(bottom=-2*f) # to set minimum y-axis value


plt.gca().axes.get_yaxis().set_visible(False) # Make y-aixs values visible or invisible

plt.show() # function to show the plot 

# ---------------------------------------------------------------------
# SHEAR FORCE DIAGRAM

ShearX = [0,0,a,a,l,l] 
ShearY = [0,(-f*b/a),(-f*b/a),(f*l/a),(f*l/a),0] 
plt.plot(ShearX, ShearY, linestyle='--', marker='o')  #plotting the points on X axis


# To show the values on the points
plt.text(0.5,0,str(0)+UnitF)  # (Coordiante x, Coordinate y,the value in text+Unit) # point 1
plt.text(0.5,(-f*b/a),str(round((-f*b/a),2))+UnitF) # point 2, with integers rounded off
plt.text(a,(-f*b/a),str(round((-f*b/a),2))+UnitF)  # point 3
plt.text(a,(f*l/a)+1.5,str(round((f*l/a),2))+UnitF) # point 4
plt.text(l-(l/10),(f*l/a)+1.5,str(round((f*l/a),2))+UnitF) # point 5
plt.text(l,0,str(0)+UnitF) # point 6


# Plotting the 0 line
ZeroLX = [0,a,l] 
ZeroLY = [0,0,0] 
plt.plot(ZeroLX, ZeroLY, color='black') # plotting the line 2 points 


plt.gca().axes.get_yaxis().set_visible(False) # Make y-aixs values visible or invisible

plt.xlabel('Position along the beam')
plt.ylabel('Shear Value')
plt.title('Shear/Transverse Force Diagram') # giving a title to graph 
plt.show() # function to show the plot 

# ---------------------------------------------------------------------
# BENDING MOMENT DIAGRAM

MomX = [0,a,l] 
MomY = [0,(f*b),0] 
plt.plot(MomX, MomY, linestyle=':', marker='o') # plotting the points on X axis

plt.text(0,-10,str((0)))  # (Coordiante x, Coordinate y,the value in text+Unit) # point 1
plt.text(a+(a/20),(f*b),str(round((f*b),2))+UnitF+UnitL)  # To SHOW the Moment value at the point # point 2
plt.text(l,-10,str((0))) # point 3


# plotting the line 2 points  
plt.plot(ZeroLX, ZeroLY, color='black')
plt.gca().axes.get_yaxis().set_visible(False) # Make y-aixs values visible or invisible



plt.xlabel('Position along the beam')
plt.ylabel('Moment Value')
plt.title('Bending Moment Diagram') # giving a title to graph 
         
plt.show() # function to show the plot 


# https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




