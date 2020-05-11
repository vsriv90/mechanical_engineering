#!/usr/bin/env python
# coding: utf-8

# https://www.code4example.com/python/tkinter/python-program-to-add-two-numbers-in-tkinter/

# In[1]:


import tkinter as tk # GUI library
from tkinter import *
from tkinter import filedialog, Text #Filedialog helps build the apps, Text helps show text on the GUI
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


def simply():
    f=set1[0]
    l=set1[1]
    a=set1[2]

    b = (l-a) # distance from right end of beam

    UnitF = str('N') # To show units of force
    UnitL = str("mm") # To show units of length

    x = [0,a,l] 
    y = [0,0,0] 

    # plotting the points on X axis
    plt.plot(x, y,label = "Beam", color='green', linewidth = 10,marker='o', markerfacecolor='blue', markersize=15) 
    plt.legend() # giving a legend to my graph

    ##################### ENTERING LOADS TO GRAPH #####################
    # fig,ax = plt.subplots(1)

    AvX = [0,0] 
    AvY = [0,-f*b/l] 

    plt.plot(AvX, AvY, linestyle='--',marker='^',markersize=10,color="grey") # To create the reaction line 
    plt.text(1,-f*b/l,str(round((f*b/l),2))+UnitF)  # To show the values on the points

    LoadX = [a,a] 
    LoadY = [0,f] 

    plt.plot(LoadX, LoadY, linestyle='--',marker='v',markersize=10,color="orange")  # To create the force line 
    plt.text(a+0.5,f+1,str(round((f),2))+UnitF) # (Coordiante x, Coordinate y,the value in text+Unit)


    BvX = [l,l] 
    BvY = [0,-f*a/l] 

    plt.plot(BvX, BvY, linestyle='--',marker='^',markersize=10,color="grey") # To create the reaction line 
    plt.text(l-(l/10),-f*a/l,str(round((f*a/l),2))+UnitF) # (Coordiante x, Coordinate y,the value in text+Unit)

    #################### End of load entering ###########################

    # AXIS LEGENDS 

    plt.xlabel('Beam length in '+ UnitL)
    plt.title('Loads on beam') # giving a title to graph 

    plt.ylim(top=2*f) # to set maximum y-axis value
    plt.ylim(bottom=-2*f/3) # to set minimum y-axis value

    plt.gca().axes.get_yaxis().set_visible(False) # Make y-aixs values visible or invisible

    plt.show() # function to show the plot 

    # ---------------------------------------------------------------------
    # SHEAR FORCE DIAGRAM

    ShearX = [0,0,a,a,l,l] 
    ShearY = [0,(f*b/l),(f*b/l),-(f*a/l),-(f*a/l),0] 
    plt.plot(ShearX, ShearY, linestyle='--', marker='o')  #plotting the points on X axis


    # To show the values on the points
    plt.text(0.5,0,str(0)+UnitF)  # (Coordiante x, Coordinate y,the value in text+Unit) # point 1
    plt.text(0.5,(f*b/l),str(round((f*b/l),2))+UnitF) # point 2, with integers rounded off
    plt.text(a,(f*b/l),str(round((f*b/l),2))+UnitF)  # point 3
    plt.text(a,-(f*a/l)+1.5,str(round((-f*a/l),2))+UnitF) # point 4
    plt.text(l-(l/10),-(f*a/l)+1.5,str(round((-f*a/l),2))+UnitF) # point 5
    plt.text(l,0,str(0)+UnitF) # point 6


    # Plotting the 0 line
    ZeroLX = [0,a,l] 
    ZeroLY = [0,0,0] 
    plt.plot(ZeroLX, ZeroLY, color='black') # plotting the line 2 points 

    plt.xlabel('Position along the beam')
    plt.title('Shear/Transverse Force Diagram') # giving a title to graph 

    plt.gca().axes.get_yaxis().set_visible(False) # Make y-aixs values visible or invisible
    plt.show() # function to show the plot 

    # ---------------------------------------------------------------------
    # BENDING MOMENT DIAGRAM

    MomX = [0,a,l] 
    MomY = [0,(-f*a*b/l),0] 
    plt.plot(MomX, MomY, linestyle=':', marker='o') # plotting the points on X axis

    plt.text(0,-10,str((0)))  # (Coordiante x, Coordinate y,the value in text+Unit) # point 1
    plt.text(a+(a/20),(-f*a*b/l),str(round((-f*a*b/l),2))+UnitF+UnitL)  # To SHOW the Moment value at the point # point 2
    plt.text(l,-10,str((0))) # point 3


    # plotting the line 2 points  
    plt.plot(ZeroLX, ZeroLY, color='black')

    plt.xlabel('Position along the beam')
    plt.title('Bending Moment Diagram') # giving a title to graph 

    plt.gca().axes.get_yaxis().set_visible(False) # Make y-aixs values visible or invisible
    plt.show() # function to show the plot 


    
def simply_end():
    
    f=set1[0]
    l=set1[1]
    a=set1[2]
    
    b = (l-a) # distance from right end of beam

    UnitF = str('N') # To show units of force
    UnitL = str("mm") # To show units of length
    
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



def cantilever():
    
    f=set1[0]
    l=set1[1]
    a=set1[2]
    
    UnitF = str('N') # To show units of force
    UnitL = str("mm") # To show units of length
    
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



    
# ALL BEAM MODELS ABOVE
# ALL BUTTONS/DROP-DOWN MENUS BELOW




set1=[]
set2=[]

def InputValues():
    f = int(enterforce.get()) # to get the value the user enters in the textbox created above
    l = int(enterlength.get()) # to get the value the user enters in the textbox created above
    a = int(enterloadlength.get()) # to get the value the user enters in the textbox created above
    Text1.set(f) # TO CREATE A SET OF WHAT'S ABOVE
    Text2.set(l)
    Text3.set(a)    
    
    set1.append(f)
    set1.append(l)
    set1.append(a)
    
    return set1

    
def select():
    def select1():
        model = var.get()
        print(model[:])
        if model[:] == "Simply Supported - Centre Loaded":
            simply()
        elif model[:] == "Simply Supported - End Loaded":
            simply_end()
        elif model[:] == "Cantilever":
            cantilever()    
        else:
            print("No function for this currently exists")

    win = tk.Tk()
    win.title("Beam Models") # Title of the whole window

    var = tk.StringVar(win)

    var.set('Choose here') # initial default 

    choices = ['Simply Supported - Centre Loaded', 'Simply Supported - End Loaded', 'Cantilever']
    option = tk.OptionMenu(win, var, *choices)
    option.pack(side='left', padx=10, pady=10)

    button = tk.Button(win, text="Select", command=select1)
    button.pack(side='left', padx=20, pady=10)

    win.mainloop()

    

# THE WHOLE GUI PROGRAM #########

window1 = tk.Tk()
Text1=tk.StringVar();
Text2=tk.StringVar();
Text3=tk.StringVar();


# Force 
tk.Label(window1, text="Enter Force 'F' ").grid(row=0, column=0, sticky=W) # Row and coloumn numbers start with 0
enterforce = tk.Entry() # A text entry widget that allows only a single line of text;
enterforce.grid(row=0, column=1) #location of the entryline in the grid

# Length L
tk.Label(window1, text="Enter Length 'L' ").grid(row=1, column=0, sticky=W) # Row and coloumn numbers start with 0
enterlength = tk.Entry() # A text entry widget that allows only a single line of text;
enterlength.grid(row=1, column=1) #location of the entryline in the grid


# Length a
tk.Label(window1, text="Enter Length 'a' ").grid(row=2, column=0, sticky=W) # Row and coloumn numbers start with 0
enterloadlength = tk.Entry() # A text entry widget that allows only a single line of text;
enterloadlength.grid(row=2, column=1) #location of the entryline in the grid

b1 = tk.Button(window1, text="Submit values as input", command=InputValues) #takes the input and plays the program "addNumbers"
b1.grid(row=4, column=0,columnspan=60, rowspan=1,sticky=W+E+N+S, padx=5, pady=5) # Size of the button

b2 = tk.Button(window1, text="Choose beam model", command=select) #takes the input and plays the program "addNumbers"
b2.grid(row=5, column=0,columnspan=60, rowspan=1,sticky=W+E+N+S, padx=5, pady=5) # Size of the button


b3 = tk.Button(window1, text ="Close the window", command = window1.destroy)
b3.grid(row=7, column=0,columnspan=60, rowspan=1,sticky=W+E+N+S, padx=5, pady=5) # Size of the button


window1.mainloop(); # Opens the GUI created above

