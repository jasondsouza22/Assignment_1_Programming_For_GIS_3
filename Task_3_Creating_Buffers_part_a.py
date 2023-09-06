import arcpy

arcpy.env.workspace = r"D:\Second Year\Sem 3\Programming_for_GIS_III\New folder\Assignment_1_Programming_For_GIS_3\ProProject_Practical_One\Practical_One.gdb"

# Performing buffer operations
arcpy.analysis.Buffer("Wilson_Schools","Wilson_Schools_Buffer_500","500 meters")

print("Process Completed")
