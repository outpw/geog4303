#******************************
# Class03_05_Demo: Using Search and Update Cursors
# Created by:  Stefan Leyk
# Created on:  01/27/2014
# Updated on:  01/27/2020
#******************************
# Description:  We will use this script interactively to learn more
# about Cursors and how to wrok with them
#******************************

import arcpy
import traceback
import sys
from arcpy import env

env.workspace = r"C:\Users\phwh9568\GEOG_4303\Week2\data"
print arcpy.ListFeatureClasses()
env.workspace = r"C:\Users\phwh9568\GEOG_4303\Week2"
inFC = r'/data/lyons_mrd.shp'
copFC = r'/results/cp_lyons_mrd1.shp'
count80540 = 0

try:
    if arcpy.Exists(copFC):
        arcpy.Delete_management(copFC)
        print "Existing prior results deleted."
    arcpy.Copy_management(inFC,copFC)   
    
    #**********************************************
    # Demo search cursor
    #**********************************************
    #----------------------------------------------
    # Access to attributes in rows
    #----------------------------------------------
    with arcpy.da.SearchCursor(copFC,["FID","ZIPL"]) as scur:
        for row in scur: 
            if row[1] == '80540':
                count80540 = count80540 + 1
                print "ZIP at " + str(row[0]) +" is " + str(row[1])
    print "The ZIP 80540 occurs "+str(count80540)+" times."


   
#    #----------------------------------------------
#    # Let's look at GEOMETRY 
#    #----------------------------------------------
#    #copFC is now copied from lyons_sub.shp
    
#    with arcpy.da.SearchCursor(copFC,["SHAPE@"]) as scur:
#    # First row content -> tuple    
    #    row = scur.next()
    #    # Polyline object and some properties
    #    pLine = row[0]
    #    pLine.isMultipart    
    #    pLine.partCount      
    #    pLine.pointCount     
    #    pLine.length
    #    # Access the Array object of the first part
    #    pLineArr = pLine.getPart(0) #this returns the first index
    #    # Get access to all point objects in the Array through indexing
    #    # and their properties (x and y values)
    #    point1 = pLineArr[0]  # or: pLineArr.getObject(0)
    #    print point1.X
    #    print point1.Y
    #    # Iterate through all point objects in the Array in given order
    #    for p in pLineArr: 
    #        print p
    #    # some interesting tests (topology)
    #    point1.touches(pLine) 
    ##    newPolyLine=arcpy.Polyline(pLineArr)    #make a new line feature from one of the line segments
    ##    print newPolyLine
    #    
    
    #************************************************   
    # Demo update cursor for editing table and geometry 
    #************************************************
    #----------------------------------------------
    # Update Table Attributes
    #----------------------------------------------
#    arcpy.management.AddField(copFC,'ZIP2', 'LONG')
    #    with arcpy.da.UpdateCursor(copFC ,["FID","ZIPL","ZIP2"]) as ucur:
        #    for row in ucur:
        #        if row[1] == '80540':
        #            count80540 = count80540 + 1
        #            row[2] = 3562
        #            print "ZIP at " + str(row[0])+" is changed to " + str(row[2])
        #        ucur.updateRow(row)
        

    #----------------------------------------------
    # Let's look at GEOMETRY -- interactive!!!
    #----------------------------------------------

#    with arcpy.da.UpdateCursor(copFC,["SHAPE@"]) as ucur:
    #    row = ucur.next()
    #    pLine = row[0]
    #    pLine.isMultipart    
    #    pLine.pointCount
    #    pLineArr = pLine.getPart(0)
    #    p1 = pLineArr[0]
    #    p1.X
    #    p1.X = p1.X+2000
    #    pLineArr[0]=p1   # adds another points at the beginning of the array
    #    newPolyLine=arcpy.Polyline(pLineArr)
    #    ucur.updateRow([newPolyLine])
    #del pLineArr
    
    # Here a way to change the coordinates of all points of a line array
#    ucur = arcpy.da.UpdateCursor(copFC,["SHAPE@"])
#    row = ucur.next()
#    pLine = row[0]
#    pLine.isMultipart    
#    pLine.pointCount
#    pLineArr = pLine.getPart(0)
#    for i in range(len(pLineArr)):
#        p=pLineArr[i]
#        p.X = p.X+2000
    
#    newPolyLine=arcpy.Polyline(pLineArr)
#    ucur.updateRow([newPolyLine])
#    del ucur,pLineArr

#**************************************************
    

#***********************
    #WHILE variant

#    scur = arcpy.da.SearchCursor(copFC,["FID","ZIPL"])
#    countRows = 0; countRows2 = 0
#    for i in scur:
#        countRows+=1
#    scur.reset()
#    row = scur.next()
#    while countRows2<countRows:
#        if row[1] == '80540':
#            count80540 += 1
#            print "ZIP at " + str(row[0]) +" is " + str(row[1])
#        countRows2 += 1
#        if countRows2<countRows: row = scur.next()
#        
#    del scur
    
except:
    print "Try it again..."
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n " +str(sys.exc_info()[1])    
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(0) + "\n"
    print msgs
    print pymsg