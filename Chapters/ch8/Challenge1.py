"""Write a script that creates a new polygon feature class containing a single(square)
polygon with the following coordinates:
[0, 0], [0, 1000], [1000,0], [1000,1000]
"""




import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise08"
coordlist = [[0,0],[0,1000],[1000,0],[1000,1000]]
pointlist = []
for x,y in coordlist:
    point = arcpy.Point(x,y)
    pointgeometry = arcpy.PointGeometry(point)
    pointlist.append(pointgeometry)
arcpy.Buffer_analysis(pointlist, "buffer.shp","10 METERS")
