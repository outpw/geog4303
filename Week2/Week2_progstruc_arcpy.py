#******************************
# Class03_01_Demo: Arcpy Program Structure
# Created by:  Stefan Leyk
# Created on:  01/24/2016
# Updated on:  01/24/2020
#******************************
#Description:  
'''
This script will perform the ArcGIS Buffer routine for a specified
feature class in order to demonstrate a typical arcpy scrip structure:
1. Workspaces
2. Input and output feature classes
3. Use of ArGIS geoprocessing functions
4. Defining paraeters for the ArcGIS Clip routine programmatically
5. try: except: for error handling
'''
# Caution: Built-in errors ...;-)

#******************************
# 1. import arcpy and other modules
import arcpy
import sys
import traceback
from arcpy import env
#******************************
# 2. Define arcpy workspace
env.workspace = r"C:\Users\phwh9568\GEOG_4303\Week2"
#******************************
# 3. Variable definitions in general and for geoprocessing functions
outpath = r"/results"
infile = r"/data/lyons_mrd.shp"
outfile = outpath + r"/ly_mrd_buff.shp" 
#******************************
# 4.  Add try: and except: blocks
try:
    # check to see if outfile already exists
    # if it does, delete it
    if arcpy.Exists(outfiles):  #why is here an error? (output)
        arcpy.Delete_management(outfile) #(outfile)
        print outfile, "had to be deleted"
        arcpy.GetMessages(0)
    #******************************
    # 5. Add and run geoprocessing routine (see ArcGIS Help)
    # check if the input exists and if so, run the tool    
    if arcpy.Exists(infile) == True: #why is here an error? (input)
        # Parameters using variables
        print "Starting Buffer routine"
        arcpy.Buffer_analysis(infile, outfile, "100","", "ROUNDa") #why is here an error? "ROUNDa"
        print "Buffer operation executed."
    else:
        print "Dataset does not exist in directory."
#except:
#    #******************************
#    # 6. Add exception code within except block
#    print "Try it again..."
#    print arcpy.GetMessage(2)
#    print arcpy.GetMessages(0)
# 
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n " +str(sys.exc_info()[1])    
    arcmsgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    # prints messages to the Python Shell
    print arcmsgs
    print pymsg
    print "\nCurrent Arcpy Messages:", arcpy.GetMessages()