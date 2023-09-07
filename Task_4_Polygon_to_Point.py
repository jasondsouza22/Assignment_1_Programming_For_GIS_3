import arcpy

arcpy.env.workspace = r"D:\Second Year\Sem 3\Programming_for_GIS_III\New folder\Assignment_1_Programming_For_GIS_3\ProProject_Practical_One\Practical_One.gdb"

#Input Feature
input_feature_class = "Wilson_Zoning"

#Output_Feature
output_feature_class = "Wilson_Zoning_PointFeature"


arcpy.management.FeatureToPoint(input_feature_class, output_feature_class, "CENTROID")

print("Process Completed")