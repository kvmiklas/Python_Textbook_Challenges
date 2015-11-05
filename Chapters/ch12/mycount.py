"""Challenge_1-Part1: Create a custom function called countstringfields that determines
the number of fields of type string in an input feature class. Create this function
in a seperate script (mycount.py) that you will call from another script
"""
import arcpy
def countstringfields( layer = "streets.shp"):
    arcpy.env.workspace = "P:/Python/Data/Exercise12"

    if layer == None:
        return None
    #Get the count for each field with the type "string"
    n = 0

    for field in arcpy.ListFields(layer):
        if field.type == "String":
            n += 1
    return n
