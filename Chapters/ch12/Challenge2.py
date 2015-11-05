"""Challenge_2-Part2: Given feature class called parcels.shp, which contains fields: FID,
Shape,Landuse, and Value. Modify the parceltax.py script so that it determines
the property tax for each parcel and stores these values in a list.
"""
import arcpy
import parcelclass
from arcpy import env
env.workspace = "P:/Python/Python_Textbook_Challenges/Chapters/ch12"
fc = "parcels.shp"
cursor = arcpy.da.SearchCursor(fc,["FID", "Landuse", "Vaule"])
for row in cursor:
    myparcel = parcelclass.Parcel(row[1],row[2])
    mytax = myparcel.assessment()
    print "{0}: {1}".format(row[0],mytax)

