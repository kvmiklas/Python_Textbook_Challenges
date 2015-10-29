"""Research the AddLayer function of the ArcPy mapping module and use
it to write a script that adds the parks layer from the Parks data frame
in Austin_TX.mxd to the other two data frames in the same map document."""

def Challenge1():
    import arcpy
    mxd = r"P:/Python/Data/Exercise10/Austin_TX.mxd"
    mapdoc = arcpy.mapping.MapDocument(mxd)
    dfs = arcpy.mapping.ListDataFrames(mapdoc)
    lyrlist = arcpy.mapping.ListLayers(mapdoc)
    for lyr in lyrlist:
        if lyr.name == "parks":
            for df in dfs:
                if lyr in df == "parks":
                    print "Missed"
                else:
                    arcpy.mapping.AddLayer(df, lyr, "TOP")
    mapdoc.saveACopy("P:/Python/Data/Exercise10/Austin_TX.mxd")
    del mxd
