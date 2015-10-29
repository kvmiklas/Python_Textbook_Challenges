"""Incorrect Script. Find all errors to run script properly.

import arcpy
from arcpy import env
env.workspace = "C:/EsriPress/Python/Data/Exercise07"
FC = "airports.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
if fields.name == "NAME"
for row in rows:
print "Name = {0}".format(row.getValue(field.name))

"""

#Errors listed with format before running the script.

    #Error_1:expected an indented block on line #8. There needs to be an indented space before the if statement.
    #Error_2:invalid syntax on line #8. There needs to be a colon after "NAME".
    #Error_3:expected an indented block on line #9. There needs to be an indented space and a colon added after.
    #Error_4:expected an indented block on line #10. There needs to be an indented space.

#Errors listed while running the script.
    #Error_1: NameError: name 'fc' is not defined. The FC needs to be lowercase.
    #Error_2: IOError: "airports.shp" does not exist. Make sure the env.workspace is correct pathway to shp.file.
    #Error_3: AttributeError: 'list' object has no attribute 'name'. The field does not have an object called 'name'. Take off the .name in the if statement.
    #Error_4: Invalid Syntax: needs to a be a colon after the if statement.

#Correct Script

import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise07"
fc = "airports.shp"
rows = arcpy.SearchCursor(fc)
fields = arcpy.ListFields(fc)
for field in fields:
    if fields == "NAME":
        for row in rows:
            print "Name = {0}".format(row.getValue(field.name))            
