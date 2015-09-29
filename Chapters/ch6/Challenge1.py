Write a script that reads all the feature classes in a workspace and prints the name of each feature class and 
geometry type of that feature class in the following format.


>>>import arcpy
>>>from arcpy import env
>>>env.workspace = "P:/Python/Data/Exercise06"
>>>fclist = arcpy.ListFeatureClasses()
>>>print fclist

Prints list of .shp files

>>>import arcpy
>>>from arcpy import env
>>>env.overwriteOutput = True
>>>env.workspace = "P:/Python/Data/Exercise06"
>>>fieldlist = arcpy.ListFields("hospitals.shp", "","")
>>>for field in fieldlist:
	print field.name + " " + field.type


Prints the Field Name and Geometry


