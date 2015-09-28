Write a script that runs the Add XY Features tool on the hospitals.shp.


>>>import arcpy
>>>from arcpy import env
>>>env.workspace = "P:/Python/Data/Exercise05"
>>>arcpy.Copy_managment("hospitals.shp", "hospitalsXYpts.shp")
>>>arcpy.AddXY_managment("hospitals.shp")

Runs Tool