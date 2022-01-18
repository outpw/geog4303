#******************************
# IDO computation Demo: Numpy/arcpy Demo for IDO calculation
# Created by:  Stefan Leyk
# Created on:  
# Updated on:  
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
       
def writeOutRasterArc(arcpy,path,resArray,llpnt,cellSize,spref,output):    
    print "Executing writeOutRasterArc()..."
    finalRast = arcpy.NumPyArrayToRaster(resArray,llpnt,cellSize,cellSize)
    #define the projection for the output raster object
    arcpy.DefineProjection_management(finalRast,spref)
    finalRast.save(path+output) #save the output raster as a permanent file

def compIDO(myArrayNLCD):
    print "Executing compIDO()..."
    #myArrayIDO = numpy.zeros(myArrayNLCD.shape).astype(float)
    myArray = numpy.where(numpy.equal(myArrayNLCD,42),1,0)
    myArrayIDO = numpy.where(numpy.equal(myArray,1),1,0)
    countNN=1
    while countNN>0:
        print "loop finished"
        countNN=0
        for i in range (1,numpy.size(myArray,1)-1):
            for j in range (1,numpy.size(myArray,0)-1):
                if myArray[j][i]>=1 and myArray[j-1:j+2,i-1:i+2].min()>=1:
#                    a = myArray[j-1:j+2,i-1:i+2]
#                    if a.min()>=1:
                    myArrayIDO[j][i]+=1
                    myArray[j][i]+=1
                    countNN+=1
                    
        myArray=numpy.where(numpy.greater(myArray,1),1,0)
    return myArrayIDO

#**************************************
#***Call the functions*****************
#**************************************    
import numpy,arcpy,sys,traceback,string, scipy
from arcpy import env
path = r"c:\GIS3"
outfile= r'\results\idoImage.tif'
infile = r'\\data\\input_l'

try:
    [theInputArray,llpnt,cellSize,spref] = createArrFromImgArc(arcpy,path,infile)
    
    resArray = compIDO(theInputArray)
        
    writeOutRasterArc(arcpy,path,resArray,llpnt,cellSize,spref,outfile)
    
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n " +str(sys.exc_info()[1])    
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"
    #arcpy.AddError(msgs)
    #arcpy.AddError(pymsg)
    print msgs
    print pymsg