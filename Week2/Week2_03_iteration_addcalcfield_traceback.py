#******************************
# Class03_03_Demo: Calculate Field Example
# Created by:  Stefan Leyk
# Created on:  01/27/2014
# Updated on:  01/07/2022, PW
#******************************
# Description:  Demonstrates how to apply the AddField()
# method in arcpy in a counted loop framework 
# Caution: Built-in errors ...;-)
#******************************

# import the modules needed
import arcpy
import traceback
import sys
from arcpy import env

# workspace:
env.workspace = "C:\Users\phwh9568\GEOG_4303\Week2"

# create your list of year values
period = range(1972,1979) # use the range function to define a list variable

try:
    for year in period:
        #all variables you will need you should declare right here
        print "********************************"
        print "Declaring all variables needed for year", year
        
        inFile = r"/data/samplePNT1_" + str(year) + ".shp"
        outFile = r"/results/samplePNT1_" + str(year) + ".shp"
        
        if arcpy.Exists(outFile)==True:
            arcpy.management.Delete(outFile)
            print "delete operation performed"
        arcpy.management.Copy(inFile,outFile)
        
        #Add a field to the table
        arcpy.management.AddField(outFile,"year","Long")
        
        #calculate the field "year"
        print "Calculating year field of", inFile
        arcpy.management.CalculateField(outFile, 'year',year , 'VB')

        
except:
    print "Try it again..."
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(0) + "\n"
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n " +str(sys.exc_info()[1])    
    print msgs
    print pymsg
