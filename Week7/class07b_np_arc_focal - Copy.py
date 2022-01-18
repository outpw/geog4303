#******************************
# Class07bDemo: Numpy/arcpy Demo for Class 08
# Created by:  Stefan Leyk
# Created on:  03/10/2014
# Updated on:  03/10/2019
#******************************
# Description:  
# Purpose: Testing functions using arcpy and Numpy
#******************************
def createArrFromImgArc(arcpy, path, infile):
    print "Executing createArrFromImgArc()..."
    arcpy.CheckOutExtension("Spatial")
    arcpy.env.workspace = path
    arcpy.env.overwriteOutput = 1
    #create raster object
    ftc = arcpy.sa.Raster(infile)
    #rows and columns
    ftc.height 
    ftc.width 
    #cell size
    cellSize = ftc.meanCellHeight
    #lower left point
    llpnt = ftc.extent.lowerLeft
    #spatial reference object
    spref = ftc.spatialReference
    #raster to numpy array
    ftcA = arcpy.RasterToNumPyArray(ftc).astype(float)
    return ftcA,llpnt,cellSize,spref
       
def writeOutRasterArc(arcpy,path,resArray,llpnt,cellSize,spref):    
    print "Executing writeOutRasterArc()..."
    finalRast = arcpy.NumPyArrayToRaster(resArray,llpnt,cellSize,cellSize)
    #define the projection for the output raster object
    arcpy.DefineProjection_management(finalRast,spref)
    finalRast.save(path+'\\results\\testResult4') #save the output raster as a permanent file

def computeMeanFilter(myArray):
    print "Executing computeMeanFilter()..."
    myArrayMean = numpy.zeros(myArray.shape).astype(float)
    for i in range (1,numpy.size(myArray,1)-1):
        for j in range (1,numpy.size(myArray,0)-1):
            sum = 0.0
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    sum = sum + myArray[jj][ii]
            myArrayMean[j][i] = float(sum / 9)
        
    return myArrayMean

def computeMedianFilter(myArray):
    print "Executing computeMedianFilter()..."
    myArrayMedian = numpy.zeros(myArray.shape).astype(float)
    for i in range (1,numpy.size(myArray,1)-1):
        for j in range (1,numpy.size(myArray,0)-1):
            myVals = []
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    myVals.append(myArray[jj][ii])
            myArrayMedian[j][i] = scipy.median(myVals)
        
    return myArrayMedian

def computeMajorityFilter(myArray):
    print "Executing computeMajorityFilter()..."
    myArrayMax = numpy.zeros(myArray.shape).astype(int)
    for i in range (1,numpy.size(myArray,1)-1):
        for j in range (1,numpy.size(myArray,0)-1):
            myArrayMax[j][i] = 0.0
            sum = 0.0
            valueList = []
            countList = []
            for ii in range(i-1,i+2):
                for jj in range(j-1,j+2):
                    if myArray[jj][ii] not in valueList:
                        valueList.append(myArray[jj][ii])
                        countList.append(1)
                    else:
                        countList[valueList.index(myArray[jj][ii])] += 1
            maxCount = max(countList)
            myMainClass = valueList[countList.index(maxCount)]
            myArrayMax[j][i] = myMainClass
    return myArrayMax

def computeBoundary(myArray):
    print "Executing computeBoundary()..."
    myArrayBound = numpy.zeros(myArray.shape).astype(int)
    for i in range (1,numpy.size(myArray,1)-1):
        for j in range (1,numpy.size(myArray,0)-1):
            if myArray[j][i] == 42:
                for ii in range(i-1,i+2):
                    for jj in range(j-1,j+2):
                        if myArray[jj][ii] == 81 or myArray[jj][ii] == 82:
                            myArrayBound[j][i] = 1
    return myArrayBound

def computeBoundaryOfPatches(myArray,myPatchArray):
    print "Executing computeBoundaryOfPatches()..."
    myArrayBound = numpy.zeros(myArray.shape).astype(int)
    for i in range (1,numpy.size(myArray,1)-1):
        for j in range (1,numpy.size(myArray,0)-1):
            if (myArray[j][i] == 81 or myArray[j][i] == 82) and myPatchArray[j][i] != 1:
                for ii in range(i-1,i+2):
                    for jj in range(j-1,j+2):
                        if myPatchArray[jj][ii] == 1:
                            myArrayBound[j][i] = 1
    return myArrayBound

def findAgricIslands(myArray):
    print "Executing findAgricIslands()..."
    myArrayBound = numpy.zeros(myArray.shape).astype(int)
    for i in range (1,numpy.size(myArray,1)-1):
        for j in range (1,numpy.size(myArray,0)-1):
            if myArray[j][i] == 81 or myArray[j][i] == 82:
                countNonForEnv = 0
                for ii in range(i-1,i+2):
                    for jj in range(j-1,j+2):
                        if myArray[jj][ii] == 81 or myArray[jj][ii] == 82:
                            countNonForEnv += 1
                if countNonForEnv == 9:
                    myArrayBound[j][i] = 1
    return myArrayBound

# this is an example for forest exposure to insecticide application in grassland
# if forest has an adjacent grassland pixel (71) East of it the forest pixel is 
# potentially "exposed" otherwise not (East wind assumed)
def computeExposureWghtE(myArray):
    print "Executing computeExposureWght()..."
    myArrayBound = numpy.zeros(myArray.shape).astype(float)
    for i in range (1,numpy.size(myArray,1)-1):
        for j in range (1,numpy.size(myArray,0)-1):
            if myArray[j][i] == 42:
                for ii in range(i-1,i+2):
                    for jj in range(j-1,j+2):
                        if myArray[jj][ii] == 71 and myArrayBound[j][i] != 1:
                            if jj == j and ii == i+1:
                                myArrayBound[j][i] = 1
                            else:
                                myArrayBound[j][i] = 0
    return myArrayBound

#**************************************
#***Call the functions*****************
#**************************************    
import numpy,arcpy,sys,traceback,string, scipy
from arcpy import env
path = r"c:\GIS3"
##C:\\myDirectory
try:
    [theInputArray,llpnt,cellSize,spref] = createArrFromImgArc(arcpy,path, '\\data\\raster_focal\\input\\input_l')

#    resArray = computeMajorityFilter(theInputArray)
#    resArray = computeBoundary(theInputArray)
#    resArray = computeMedianFilter(theInputArray)
#    resArray = findAgricIslands(theInputArray)
    resArray = computeExposureWghtE(theInputArray)
    
    #to be used together to demonstrate how to work with 2 grids
#    patchArray = findAgricIslands(theInputArray)
#    resArray = computeBoundaryOfPatches(theInputArray,patchArray)
    
    writeOutRasterArc(arcpy,path,resArray,llpnt,cellSize,spref)
    
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n " +str(sys.exc_info()[1])    
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    #arcpy.AddError(msgs)
    #arcpy.AddError(pymsg)
    print msgs
    print pymsg