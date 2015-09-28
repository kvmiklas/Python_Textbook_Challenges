Write a script that determines whether the following extensions are available.

ArcGIS 3D Analyst
ArcGIS Network Analyst
ArcGIS Spatial Analyst



ArcGIS 3D Analyst

>>>arcpy.ArcGIS 3D Analyst("Exists")

>>>import arcpy
>>>from arcpy import env
>>>env.workspace = "P:/Python/Data"

if arcpy.CheckExtension("3D") == "Available":
	arcpy.CheckOutExtension("3D")
	arcpy.Slope_3d("dem", "slope", "DEGREES")
	arcpy.CheckInExtension("3D")
else:
	print "3D Analyst license is unavailable."



ArcGIS Network Analyst

>>>arcpy.ArcGIS Network Analyst("Exists")

>>>import arcpy
>>>from arcpy import env
>>>env.workspace = "P:/Python/Data"

if arcpy.CheckExtension("Network") == "Available":
	arcpy.CheckOutExtension("Network")
	arcpy.CheckInExtension("Network")
else:
	print "Network Analyst is unavailable."



ArcGIS Spatial Analyst

>>>arcpy.ArcGIS Spatial Analyst("Exists")

>>>import arcpy
>>>import arcpy import env
>>>env.workspace = "P:/Python/Data"

if arcpy.CheckExtension("Spatial") == "Available":
	arcpy.CheckOutExtension("Spatial")
	arcpy.CheckInExtension("Spatial")
else:
	print "Spatial Analyst is unavilable."