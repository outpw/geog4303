#****************************************
# Week01Demo(4): My First GP Script
# Filename:       Week1_04_firstGPbuff.py
# Created by:     Stefan Leyk
# Created on:     01/17/2017
# Updated on:     01/07/2020
#-----------------------------------------
# Description:  This script demos a few first geoprocessing examples and the 
# use of different programming techniques (ex. Buffer)
#******************************

import arcpy
from arcpy import env

#************************************************
# (1) Example for sequential Geoprocessing script
#------------------------------------------------

env.workspace = r'C:\Users\phwh9568\GEOG_4303\Week1' #modify path to run this on your own machine
inputFC = r'/data/lyons_mrd.shp'
outputFC = r'/results/ly_mrd_buff.shp'

try:
    # Buffer roads based on a distance
    arcpy.Buffer_analysis(inputFC, outputFC, "100","", "ROUND","ALL")

    print "Buffer operation 1 executed."
    
except:
    print "Try it again..."



#************************************************
# (2) Example for branching in a Geoprocessing script
#------------------------------------------------
'''
env.workspace = r'C:\Users\phwh9568\GEOG_4303\Week1' #modify path to run this on your own machine
inputFC = r'/data/lyons_mrd.shp'
outputFC = r'/results/ly_mrd_buff.shp'

# pay attention to indentation here
try:
    if arcpy.Exists(inputFC) == True:
        if arcpy.Exists(outputFC) == True:
            arcpy.Delete_management(outputFC)
            print "old output file exploded."
        arcpy.Buffer_analysis(inputFC, outputFC, "300","", "ROUND")
        print "Buffer operation 2 executed!"
    else:
        print "Dataset does not exist in directory."
except:
    print "Try it again..."
    print arcpy.GetMessage(2)
    print arcpy.GetMessages(0)
'''


#************************************************
# (3) Example for looping (counted loop) in a GP script
#------------------------------------------------
'''
env.workspace = r"C://WS_GEOG_4303_5303" #modify path to run this on your own machine
inputFC = r"/data/lyons_mrd.shp"
outputFC = r"/results/ly_mrd_buff" #note, this is different

try:
    for a in range(100,300,20):
        arcpy.Buffer_analysis(inputFC, outputFC+str(a)+".shp", str(a), "", "ROUND")
    
    print "Buffer operation 3 executed."    
except:
    print "Try it again..."

'''

#************************************************
# (4) Example for looping (conditional looping) in a GP script
#------------------------------------------------
'''
env.workspace = r"C://WS_GEOG_4303_5303"
inputFC = r"/data/lyons_mrd.shp"
outputFC = r"/results/ly_mrd_buff" #note, this is different

try:
    b = 100
    while b < 200:
        arcpy.Buffer_analysis(inputFC,outputFC+str(b)+".shp",str(b),"","ROUND")
        b = b + 20
    print "Buffer operation 4 executed."
except:
    print "Try it again..."
'''    
##************************************************