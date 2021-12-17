# Example script
'''This script will clip the open space layer to the Boulder,
Lafayette and Louisville city limits'''

# Created 10-31-2010 by Galen Maclaurin

# import arc license and set workspace
import arcpy
from arcpy import env
env.workspace = r'H:\GEOG4303\labs2012\lab0\data'
env.overwriteOutput = 1

# say you wanted to know what files are in your workspace    
print "listing feature classes in workspace:"
print arcpy.ListFeatureClasses()

# Define variables
openSpace = 'boulderCountyOpen.shp'

# Create list of shapefile names
cities = ['boulder','lafayette','louisville']

# Loop through cities list and clip open space to each municipality
for i in cities:
    arcpy.Clip_analysis(openSpace, i + '.shp', i + 'Open.shp')
    print 'open space clipped to ' + i + ' city limits'

print 'analysis complete'