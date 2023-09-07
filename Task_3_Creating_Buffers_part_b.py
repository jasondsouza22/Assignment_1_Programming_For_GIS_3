import arcpy

arcpy.env.workspace = r"D:\Second Year\Sem 3\Programming_for_GIS_III\New folder\Assignment_1_Programming_For_GIS_3\ProProject_Practical_One\Practical_One.gdb"

# Input Feature
input_feature_class = "Wilson_Schools"
output_feature_class = "Wilson_Schools_MultiRingBuffer"

#Buffer Distance
buffer_distance = [1000, 1200, 1400]

arcpy.analysis.MultipleRingBuffer(input_feature_class, output_feature_class,buffer_distance, "feet", "", "NONE")

print("Process Completed")