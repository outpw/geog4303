#******************************
# Demo Class03_06:     Creating Line Features
# Created by:       Stefan Leyk
# Created on:       01/27/2014
# Updated on:       12/22/2021
#******************************
# Description:  A quick example how to create Line features using insert cursor
# based on exercise of class 02 (point maker) 
#******************************

import sys
import arcpy
import traceback
from arcpy import env


# Create and define variables
env.workspace = r"C:\Users\phwh9568\GEOG_4303\Week2\Results"
line = 'myNewLine.shp'


try:
    if arcpy.Exists(line):
        arcpy.Delete_management(line)
        
    # create a feature class
    arcpy.CreateFeatureclass_management(env.workspace, line, "polyline")

    
    # Creating the lists of x and y coordinates.
    myXCoords = [4777554.97279000000,4777424.24792000000,4775424.24792000000]
    myYCoords = [4716268.70116000000,4715573.18061000000,4718573.18061000000]
    

    # Creating an GP array object and ONE GP point object
    # Think of these as empty features which you will populate below with a loop
    lineArray = arcpy.CreateObject("array")
    point = arcpy.CreateObject("point")
    
    # Now we'll use insert cursor to insert our geometry.
    # create the insert cursor in order to add the points to our own polyline feature class
    with arcpy.da.InsertCursor(line,['SHAPE@']) as cursor: 

        for i in range(len(myXCoords)): #each element select from the looplist:
            point.X = myXCoords[i]
            point.Y = myYCoords[i]
            lineArray.add(point) #add the point to the polyline array ...       
        
        # Create the new polyline using the line array you just created above 
        newPolyLine=arcpy.Polyline(lineArray)
        # Insert this new polyline into the feature class as a new row
        cursor.insertRow([newPolyLine])
    
    print "You've added a new line feature to the feature class"
    
except:
    # If an error occurred while running the tool print the error messages.
    print "Try it again..."
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n " +str(sys.exc_info()[1])    
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(0) + "\n"
    print msgs
    print pymsg

