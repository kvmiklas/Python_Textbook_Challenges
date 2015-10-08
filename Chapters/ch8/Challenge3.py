""" Write a script that creates an envelope polygon feature class for the Hawaii.shp
feature class.
"""




import arcpy
from arcpy import env
env.workspace = "P:/Python/Data/Exercise08"
arcpy.MinimumBoundingGeometry_management("Hawaii.shp","P:/Python/Data/Exercise08","RECTANGLE_BY_AREA","ALL")

                                         
                                         
