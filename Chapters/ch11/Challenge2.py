"""Incorrect Script. Find all errors to run script properly.
import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data\Exercise09"
raster = "landcover.tiff"
desc = arcpy.describe(raster)
x = desc.MeanCellHeight
y = desc.MeanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print "Cells are" + str(x) + " by " + str(y) + " " + units + "."

"""

#Error_1: AttributeError: 'module' object has no attribute 'describe'. The 'describe' needs to be capitalized as 'Describe'.
#Error_2: IOError: "landcover.tiff" does not exist. The format needs to written exactly like it is in the folder, which is "landcover.tif".
#Error_3: IOError: Make sure the pathway for the workspace is correctly written. Correct pathway to get to the "landcover.tif".
#Error_4: IOError: The backslash in the pathway needs to be correspondent to the others, in order to get the correct workspace. 

#Correct Script

import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise09"
raster = "landcover.tif"
desc = arcpy.Describe(raster)
x = desc.MeanCellHeight
y = desc.MeanCellWidth
spatialref = desc.spatialReference
units = spatialref.linearUnitName
print "Cells are" + str(x) + " by " + str(y) + " " + units + "."
