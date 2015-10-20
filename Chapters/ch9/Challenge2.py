"""Write a script that copies all the rasters in a workspace to a new file geodatabase.
You can use the rasters in Exercise 9 for the examples.
"""


#Lists all the rasters.

import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise09"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    print raster

#Copies all the rasters in the Exercise09 workspace and moves it to a new file geodatabase.

import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise09"
arcpy.RasterToGeodatabase_conversion("Elevation; landcover.tif; tm.img","P:/Python/Data/Exercise09/Results/New_file.mdb")
