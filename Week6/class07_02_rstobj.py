#******************************
# Class07Demo: Numpy Demo for Class 07
# Created by:  Stefan Leyk & Galen Maclaurin
# Created on:  03/03/2014
# Updated on:  28/02/2020
#******************************
# Description:  
## Purpose: Testing functionality of raster objects and Numpy arrays
## Applied to a DEM and a Landsat image (calculating NDVI)
#******************************
# Import modules
import time
#start script stopwatch
start = time.clock()
import numpy as np
import arcpy
from arcpy import env
import arcpy.sa as sa

#*****Example 1: Write a DEM ratser into a mumpy array********************
#Get access to a DEM raster dataset
arcpy.CheckOutExtension("Spatial")
env.workspace = r'C:\Users\phwh9568\GEOG_4303'
#create raster object from elevation dataset
demR = sa.Raster(r'\data\ned_30m_blder')
demA = arcpy.RasterToNumPyArray(demR)

#Get access to two bands of a remote sensing image raster dataset
arcpy.CheckOutExtension("Spatial")
env.overwriteOutput = 1

#******Example 2****************************************
#create raster objects from input grids. These grids have the same dimensions
#perform map algebra, and calculate NDVI; write a new NDVI raster layer
#*******************************************************
band3 = sa.Raster(r'\data\granby\l5_granby_b3')
band4 = sa.Raster(r'\data\granby\l5_granby_b4')
#Find the number of rows and columns
band3.height #number of rows - Y axis
band3.width #number of columns - X axis
#get cell size; first check that cells are square (or close enough)
assert(band3.meanCellHeight-band3.meanCellWidth<0.00001)
cellSize = band3.meanCellHeight
#get lower left point of extent to write output after analysis
llpnt = band3.extent.lowerLeft
#get spatial reference object from the raster object
spref = band3.spatialReference
spref.exporttostring()

#convert raster objects to numpy arrays
b3 = arcpy.RasterToNumPyArray(band3)
b3 = b3.astype(float) #convert to float type for ndvi calculation
b4 = arcpy.RasterToNumPyArray(band4).astype(float) #or faster, link the methods
#calculate ndvi
ndvi = (b4-b3)/(b3+b4) #this won't work as you expect if arrays are int type
ndvi.dtype #check the datatype of the array; np arrays have one data type

#convert numpy arrays to arc grids
finalRast = arcpy.NumPyArrayToRaster(ndvi,llpnt,cellSize,cellSize)
#define the projection for the output raster object
arcpy.DefineProjection_management(finalRast,spref)
finalRast.save(env.workspace +r'\\results\\NDVItest') #save the output raster as a permanent file

