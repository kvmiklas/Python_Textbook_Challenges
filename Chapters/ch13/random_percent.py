""" Challenge_1:Make a copy of the random_sample.py script and call it random_percent.py.
Modify the script so that the third parameter is a percentage of the number of input
records as integer between 1 and 100. Modify the script tool settings so that the
input for this parameter is validated on the tool dialog box."""

import arcpy
import random
from arcpy import env
env.overwriteoutput = True
inputfc = "P:/Python/Data/Exercise13/points.shp"
outputfc = "P:/Python/Data/Exercise13/Results/random1.shp"
outcount = 50
desc = arcpy.Describe(inputfc)
inlist = []
randomlist = []
fldname = desc.OIDFieldName
rows = arcpy.SearchCursor(inputfc)
row = rows.next()
x = 0
while row:
    id = row.getValue(fldname)
    inlist.append(id)
    row = rows.next()
while len(randomlist) < (outcount/ 100.0) * (len(inlist) + x):
    selitem = random.choice(inlist)
    randomlist.append(selitem)
    inlist.remove(selitem)
    x += 1
length = len(str(randomlist))
sqlexp = '"' + fldname + '"' + " in " + "(" + str(randomlist)[1:length - 1] + ")"
arcpy.MakeFeatureLayer_management(inputfc, "selection", sqlexp)
arcpy.CopyFeatures_management("selection", outputfc)
