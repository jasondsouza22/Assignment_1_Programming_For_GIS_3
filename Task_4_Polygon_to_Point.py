import arcpy

# path of wilson zoning
wilson_zoning_path = r"D:\Second Year\Sem 3\Programming_for_GIS_III\New folder\Assignment_1_Programming_For_GIS_3\ProProject_Practical_One\Practical_One.gdb\Wilson_Zoning"

# Converting wilson zone polygon to point feature
wilson_point = wilson_zoning_path + "_FeatureToPoint"

arcpy.management.FeatureToPoint(wilson_zoning_path, wilson_point)

print("Process Completed")