""" Write a script that determines the perimeter(in meters) and area (in square meters)
of each of the individual islands of the Hawaii.shp feature class. Recall that this
is a multipart feature class.
"""

import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise08"
fc = "Hawaii.shp"
for row in arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"]):
    print("Feature {0}:".format[0])
    partnum = 0
    for part in row[1]:
        poly = arcpy.Polygon(part)
        print("Part {0} area: {1}".format(partnum, poly.area))
        partnum += 1
