#******************************
# Class03_04_Demo: Example for GP List Funtions
# Created by:  Stefan Leyk
# Created on:  01/27/2014
# Updated on:  12/29/2021, Phil White
#******************************
# Description:  Example how to use List() and Describe()
# methods in arcpy
#******************************

import arcpy
import traceback
import sys
from arcpy import env

env.workspace = r'c:/users/phwh9568/GEOG_4303/week2/data'

try:
    #==========================================================

    myLayerList = arcpy.ListFeatureClasses('l*', )   #point/line
            
    print "**************************************************************************"
    print "We are working with", len(myLayerList), "layers that fulfill the filter conditions."
    print "**************************************************************************"
    #listOfFields_GP = gp.listFields(myThemesList[1])
    
    for layer in myLayerList:
        listOfFields_GP = arcpy.ListFields(layer)
        print '*******************'
        print layer, "has", len(listOfFields_GP), "fields"
        print "This layer is type", arcpy.Describe(layer).extension
        print "The shape type is:", arcpy.Describe(layer).shapeType
        for field in listOfFields_GP:
            print 'field name is:',field.name
        

            
except:
    print "Try it again..."
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n " +str(sys.exc_info()[1])    
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(0) + "\n"
    print msgs
    print pymsg
    
