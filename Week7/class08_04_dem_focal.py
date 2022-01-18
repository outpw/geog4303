#******************************
# Week07_04Demo: Numpy Demo for  Week7
# Created by:  Stefan Leyk & Galen Maclaurin
# Created on:  03/03/2014
# Updated on:  01/13/2022, PW
#******************************
# Description:  
## Purpose: Testing functionality of raster objects and Numpy arrays
## Max filter in a DEM; complete process
#******************************
# Import modules
#import time
#start script stopwatch
#start = time.clock()
import numpy as np
import arcpy
from arcpy import env
import arcpy.sa as sa

#*****Example 1: Write a DEM ratser into a mumpy array********************
# Get access to a DEM raster dataset
arcpy.CheckOutExtension("Spatial")
env.workspace = r"C:\Users\phwh9568\GEOG_4303\Week7"
# Create raster object from elevation dataset
demR = sa.Raster(r'\data\Flatirons_DEM_1m.tif')

demR.height #number of rows - Y axis
demR.width  #number of columns - X axis
cellSize = demR.meanCellHeight # get cell size
# Get lower left point of extent to write output after analysis
llpnt = demR.extent.lowerLeft
# Get spatial reference object from the raster object
spref = demR.spatialReference

# Write raster values into a numpy array
demA = arcpy.RasterToNumPyArray(demR)
# Raster query using numpy array
#demA_Out = np.where(np.greater(demA,2000),1,0)

# Raster focal max() function
demA_Out = np.zeros(demA.shape).astype(float)
for i in range (1,np.size(demA,1)-1):
    for j in range (1,np.size(demA,0)-1):
        demA_Out[j][i] = demA[j-1:j+2,i-1:i+2].max()

# Write the resulting numpy array back into a raster object
finalRast = arcpy.NumPyArrayToRaster(demA_Out,llpnt,cellSize,cellSize)
# Define the projection for the output raster object
arcpy.DefineProjection_management(finalRast,spref)
# Save a permanent raster layer
finalRast.save(env.workspace +r'\results\\DEMMaxF.tif')

