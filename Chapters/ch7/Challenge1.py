"""Write a script that creates a 15,000 meter buffer around the features in the
airport.shp feature class, classified as an airport (based on the FEATURE field)
and a 7,500 meter buffer around the feature classified as a seaplane base. The
results should be two seperate feature classes, one for each airport type.
"""





import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise07"
fc = "airports.shp"
newfield = "BUFFER_DISTANCE"
fieldtype = "TEXT"
fieldname = arcpy.ValidateFieldName(newfield)
arcpy.AddField_management(fc, fieldname, fieldtype, "", "",12)
print "New Field" + "newfield" + "Created"
print "Updating Buffer Distances"
fields = ("FEATURE", "BUFFER_DIS")
with arcpy.da.UpdateCursor(fc,fields)as cursor:
    for row in cursor:
        if row[0]== "Airport":
            row[1]= "15000 METERS"
        else:
            row[1]= ""
        cursor.updateRow(row)
print "Airport BUFFER_DISTANCE field is updated"

arcpy.Buffer_analysis(fc, "airport_buffer", "BUFFER_DIS")

with arcpy.da.UpdateCursor(fc, fields) as cursor:
    for row in cursor:
        if row[0]== "Seaplane Base":
            row[1]= "7500 METERS"
        else:
            row[1]= ""
        cursor.updateRow(row)
print "Seaplane Buffer Distance updated"
