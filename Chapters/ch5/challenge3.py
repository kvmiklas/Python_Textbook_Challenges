Write a script that runs Dissolve tool on the park.shp feature class using the PARK_TYPE field as the field for the aggregating features.

>>>import arcpy
>>>from arcpy import env
>>>env.workspace = "P:/Python/Data/Exercise05"
>>>arcpy.Dissolve_management("parks.shp", "Park_Type")

Runs Dissolve Tool