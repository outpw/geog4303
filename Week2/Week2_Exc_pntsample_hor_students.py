#******************************
# Exercise Week2: Student Version - Creating Point and Line Features
# Created by:       Stefan Leyk
# Created on:       01/27/2014
# Updated on:       01/07/2022, PW
#******************************
#Description:  Describe here ... 
#******************************

import sys 
import arcpy
import traceback
import random
from arcpy import env

print "Creating and defining variables."
env.workspace = r"C:\Users\phwh9568results"
points = 'myOwnPoints.shp'
line = 'myOwnLine.shp'
myPntLiX = []
myPntLiY = []
try:
    # Test if points and line exist. If so delete them
       
    print "**********************"
    # Create a new empty feature class of type point
    # Create also a new empty feature class of type polyline

    print "feature clasess created"

    print "**********************"
    print "Given x and y coordinates of first point."
    myXCoord = 4777554.97279000000
    myYCoord = 4716268.70116000000
    
    print "These are the coordinates of my starting points:"
    print "x-coords:", myXCoord
    print "y-coords:", myYCoord
    
    # Create an array object (of type array) using the "CreateObject" function
    # Create also an object of type point
    print "**********************"
    print "Creating an array object and ONE point object."
    
    # Create an insert cursor object for the point feature class
    # Create an insert cursor for the polyline feature class
    print "**********************"
    print "Creating an insert-cursor for the point FC." 
    print "Creating an insert-cursor for the polyline FC." 
    
    # Time for looping: repeat as many times as needed (as you have to create 11 points...):
    # Calculate and assign the x and y properties of the point object
    # insert a new row using the current point object geometry
    # Add the current point object to a line array
    # Collect the point coordinates in a Python list
    # hint: range(0,11)
    print "**********************"
    print "Starting loop to create point objects and create new geometries"
        
    # Now use arcpy.Polyline(lineArray) to create a new polyline geom object
    # And use the cursor.insertRow(newPolyLine) to insert this new row with this geometry
    print "**********************"
    print "Creating new Polyline geometry and insert new row to the polyline FC

    # Don't forget...;-)
    del cursorPnt, cursorPolyL
    
    # Write the coords into a file using your created Python lists
    
except:
    # If an error occurred while running the tool print the error messages.
    print "Try it again..."
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n " +str(sys.exc_info()[1])    
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(0) + "\n"
    print msgs
    print pymsg

