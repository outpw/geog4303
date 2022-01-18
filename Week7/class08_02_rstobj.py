#******************************
# Week07_02Demo: Numpy Demo for Weeks 07 & 08
# Created by:  Stefan Leyk, Galen Maclaurin, Phil White
# Created on:  03/03/2014
# Updated on:  01/13/2022, PW
#******************************
# Description:  
## Purpose: Testing functionality of raster objects and Numpy arrays
## Applied to a DEM and a Landsat image (calculating NDVI)
#******************************
# Import modules
#import time
#start script stopwatch
#start = time.clock()
import numpy as np
import arcpy
from arcpy import env
import arcpy.sa as sa

#*****STEP THROUGH LINE BY LINE*****s
#*****Example 1: Write a DEM ratser into a mumpy array********************
# Get access to a DEM raster dataset
arcpy.CheckOutExtension("Spatial")
env.workspace = r"C:\Users\phwh9568\GEOG_4303\week7" #change to your path
# Create raster object from elevation dataset
demR = sa.Raster(r'\data\flatirons_dem_1m.tif')

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
demA_Out = np.where(np.greater(demA,2000),1,0)

# Write the resulting numpy array back into a raster object
finalRast = arcpy.NumPyArrayToRaster(demA_Out,llpnt,cellSize,cellSize)
# Define the projection for the output raster object
arcpy.management.DefineProjection(finalRast,spref)
# Save a permanent raster layer
finalRast.save(env.workspace +r'\results\DEMQuery.tif')

#******Example 2****************************************
#create raster objects from input grids. These grids have the same dimensions
#perform map algebra, and calculate NDVI; write a new NDVI raster layer
#*******************************************************
# Get access to two bands of a remote sensing image raster dataset
arcpy.CheckOutExtension("Spatial")
env.workspace = r"C:\Users\phwh9568\GEOG_4303\week7"
env.overwriteOutput = 1
band4 = sa.Raster(r'\data\LC08_Steamboat_B4.tif')
band5 = sa.Raster(r'\data\LC08_Steamboat_B5.tif')

# Find the number of rows and columns
band4.height #number of rows - Y axis
band4.width #number of columns - X axis
# Get cell size; first check that cells are square (or close enough)
assert(band4.meanCellHeight-band4.meanCellWidth<0.00001)
cellSize = band4.meanCellHeight
# Get lower left point of extent to write output after analysis
llpnt = band4.extent.lowerLeft
# Get spatial reference object from the raster object
spref = band4.spatialReference
print spref.exporttostring()

# Convert raster objects to numpy arrays
b4 = arcpy.RasterToNumPyArray(band4)
b4 = b4.astype(float) #convert to float type for ndvi calculation
b5 = arcpy.RasterToNumPyArray(band5).astype(float) #or faster, link the methods
# Calculate ndvi
ndvi = (b5-b4)/(b5+b4) #this won't work as you expect if arrays are int type
ndvi.dtype #check the datatype of the array; np arrays have one data type

# Convert numpy arrays to arc grids
finalRast = arcpy.NumPyArrayToRaster(ndvi,llpnt,cellSize,cellSize)
# Define the projection for the output raster object
arcpy.DefineProjection_management(finalRast,spref)
finalRast.save(env.workspace +r'\\results\\NDVItest.tif') #save the output raster as a permanent tiff file

