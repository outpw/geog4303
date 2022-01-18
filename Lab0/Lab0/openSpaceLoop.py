'''
*********************************************
author: Galen Maclaurin
Date: 10/31/2012

Purpose: This script will clip the open space layer to the Boulder, Lafayette
and Louisville city limits

Modified: Alex Stum 1/24/2017: Added relative path instructions, formatting

Explantionat of sys.path variable: https://docs.python.org/2/library/sys.html
*********************************************
'''

#import arc license and set workspace
import arcpy, sys
from arcpy import env

####### NOTE: change path to sys.path[0] before turning lab in
#think of it as setting your relative path

path = r'D:\GIS3\lab0' #sys.path[0]
env.workspace = path+'\data'
env.overwriteOutput = 1


#Part 1



#Part 2
#say you wanted to know what feature classes are in your workspace    
print 'listing feature classes in workspace:'
print arcpy.ListFeatureClasses()

#define variables
openSpace = 'boulderCountyOpen.shp'

#create lists of shapefile names
cities = ['boulder','lafayette','louisville']
sites = ['sites53242bld','sites430183laf','sites329231lou']

#loop through cities list and clip open space to each municipality
for i in cities:
    arcpy.analysis.Clip(openSpace,i+'jkaljekrjklfjkalsjdklajef.shp', \
    i+'asdrerefa_Open.shp')
    print 'open space clipped to',i,'city limits'

print 'analysis complete'

