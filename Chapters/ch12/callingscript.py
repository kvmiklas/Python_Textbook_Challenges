"""Challenge_1/Part_2:Script where you call the other script called mycount.py
"""

import sys
sys.path.append(r"P:/Python/Python_Textbook_Challenges/Chapters/ch12")
import mycount

streetsLayer = arcpy.mapping.Layer("streets")
numberOfFieldsTypeString = mycount.countstringfields(streetsLayer)
del streetsLayer
print numberOfFieldsTypeString
#Runs but gives a ValueError: Layer is an invalid data source.
