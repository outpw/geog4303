#*******************************************************
# Week1 Exercise: How to Create Point Feature Classes
# Created by:  Stefan Leyk
# Created on:  01/27/2014
# Updated on:  01/07/2022, PW
#*******************************************************
# Description:  Student version. Go through the different steps carefully
# Complete the last step to iterate through the three 
# x-y coordinate pairs and create three point features
# in a point feature class 
#*******************************************************
import sys
import traceback
import arcpy
from arcpy import env


print "Creating and defining variables."
env.workspace = r"C:\Users\phwh9568\GEOG_4303\week1\results"
layer = 'myOwnPoints.shp'
try:
    if arcpy.Exists(layer):
        arcpy.management.Delete(layer)
    print "**********************"
    arcpy.management.CreateFeatureclass(env.workspace, layer, "point")
    arcpy.management.AddField(layer,'MyField',"Long")

    print "feature class created"
    print "**********************"
    print "Creating the PYTHON lists of x and y coordinates and myAttr."
    myXCoords = [4777554.97279000000,4777424.24792000000,4775424.24792000000]
    myYCoords = [4716268.70116000000,4715573.18061000000,4718573.18061000000]
    myAttr = [3425,4562,5689]
    
    
    print "These are the contents of the lists:"
    print "x-coords:", myXCoords
    print "y-coords:", myYCoords
    print "**********************"
    print "Creating ONE arcpy point object."
    point = arcpy.CreateObject("point")
    # we have three separate lists (xcoordinates, ycoordinates and myAttr)
    print "Creating an insert-cursor to access and create rows." 
    cursor = arcpy.da.InsertCursor(layer,["SHAPE@","MyField"]) #create the insert cursor
        


    #*****************************************************************
    # The below block of instructions needs to be adjusted
    # such that you create three points in a loop using 
    # the above lists with coordinates and add myAttr to each row   
    # You may need to comment out lines from above     
    # Update print statements as well 
   
    point.X = 111
    point.Y = 222
    print 'Point properties: '
    print "x: ", point.X, "y: ", point.Y
    myAttr = 3425
    print "**********************"
    cursor.insertRow([point,myAttr])
    print "**********************"
    del cursor
        
    
    
    
    #*****************************************************************
    # test for Serach Cursor:
#    cursor = arcpy.da.SearchCursor(layer,["SHAPE@XY"])
#    row = cursor.next()
#    row[0]
except:
    # If an error occurred while running the tool print the error messages.
    print "Try it again..."
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n " +str(sys.exc_info()[1])    
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(0) + "\n"
    print msgs
    print pymsg

