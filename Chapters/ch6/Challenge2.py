Write a script that reads all the feature classes in a personal or file geodatabase and copies only the polygon
feature classes to a new file geodatabase.


>>>import arcpy
>>>from arcpy import env
>>>arcpy.env.workspace = "P:/Python/Data/Exercise06"
>>>fclist = arcpy.ListFeatureClasses()
>>>print fclist


>>>import arcpy
>>>from arcpy import env
>>env.workspace = "P:/Python/Data/Exercise06"
>>>fclist = arcpy.ListFeatureClasses()
>>> for fc in fclist
	arcpy.CopyFeatures_management(fc, "P:/Python/Data/Exercise06", + fc)
