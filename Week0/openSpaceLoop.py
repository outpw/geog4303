# Example script
'''This script will clip the open space layer to the Boulder,
Lafayette and Louisville city limits'''

# Created 10-31-2010 by Galen Maclaurin, updated 2022 PW

# import arc license and set workspace
import arcpy
from arcpy import env


env.workspace = r'C:\Users\phwh9568\GEOG_4303\Week0\data' #change to your week0 data folder
env.overwriteOutput = 1

# say you wanted to know what files are in your workspace    
# print "listing feature classes in workspace:"
# print arcpy.ListFeatureClasses()


# Define variables
openSpace = 'boulderCountyOpen.shp'

# Create list of shapefile names
cities = ['boulder','lafayette','louisville']

# Loop through cities list and clip open space to each municipality 
# review arcgis clip help docs... 
for city in cities:
    arcpy.analysis.Clip(openSpace, city + '.shp', city + 'Open.shp')
    print 'open space clipped to ' + city + ' city limits'

print 'analysis complete'
