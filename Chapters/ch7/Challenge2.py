"""Write a script that adds a text field to the roads.shp feature class called FERRY
and populates this field with YES and NO values, depending on the value of the
FEATURE field.
"""



import arcpy
fc = "P:/Python/Data/Exercise07/Results/roads.shp"
arcpy.AddField_management("roads", "FERRY","TEXT")


import arcpy
fc = "P:/Python/Data/Exercise07/roads.shp"
cursor =  arcpy.da.UpdateCursor(fc, ["FEATURE", "FERRY"])
for row in cursor:
    if row[0] == "Ferry Crossing":
        row[1] = "YES"
    else:
        row[1] = "NO"
    cursor.updateRow(row)
    del row
del cursor
    
