################################
### // Initilaise Imports // ###
################################

from image_to_model import *
import matplotlib.pyplot as plt
import numpy as np

#########################################################################
### // Initialise this_dir, resources, CA_root, and src file paths // ###
#########################################################################

this_dir = Path(__file__).resolve() if "__file__" in globals() else Path.cwd().parent
CA_root = Path(__file__).resolve().parent.parent if "__file__" in globals() else Path.cwd().parent
resources_path = CA_root / Path("resources")

src_path = os.path.join(CA_root, "src")
if str(src_path) not in sys.path:
    sys.path.append(str(src_path))
    
#################################################
### // Initialise target image files paths // ###
#################################################

image_path_0 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_0_seg.h5") # Image 0
image_path_1 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_1_seg.h5") # Image 1
image_path_2 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_2_seg.h5") # Image 2
image_path_3 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_3_WKY_CB.h5") # Image 2
image_path_list = np.array([image_path_0, image_path_1, image_path_2, image_path_3])

################################################
### // Initialise file paths for pipeline // ###
################################################

ilastik_path = Path("/home/dsas627/Desktop/ilastik-1.4.1rc2-gpu-Linux/run_ilastik.sh") ### TODO: Delete/uncomment after docker integration is working
model_path = CA_root / Path("dale_experimental/resources/segmentation_model.ilp")
input_batch_processing_path = CA_root / Path("dale_experimental/resources/batch_process_input_folder")
output_batch_processing_path = CA_root / Path("dale_experimental/resources/batch_process_output_folder")

######################################
### // Verify Path(s) Existence // ###
######################################

# create a dictionary of variable_name : path_value
paths_to_check = {
    "this_dir": this_dir,
    "CA_root": CA_root,
    "resources_path": resources_path,
    "src_path": src_path,
    "image_path_0": image_path_0,
    "image_path_1": image_path_1,
    "image_path_2": image_path_2,
    "ilastik_path": ilastik_path,
    "model_path": model_path,
    "input_batch_processing_path": input_batch_processing_path,
    "output_batch_processing_path": output_batch_processing_path
}

missing_paths = []

for var_name, path_obj in paths_to_check.items():
    # cast to string to handle both pathlib.Path objects and standard strings
    if not os.path.exists(str(path_obj)):
        missing_paths.append(f"{var_name}: {path_obj}")

if not missing_paths:
    print("All Paths Set Successfully!")
else:
    print(f"Error: Non-existent file paths detected ({len(missing_paths)}):")
    for error in missing_paths:
        print(f" - {error}")

#####################################
### // Initialise image target // ###
#####################################

### TODO: User to edit image_selection_index depending on which image (Image 0, Image 1, or Image 2) they would like to process.
image_selection_index = 3 ### Change value to 0, 1, or 2 depending on which image you would like to input into the pipeline
target_image_path = image_path_list[image_selection_index]

##########################
### // Run pipeline // ###
##########################

### Run pipeline
network_construction_time, cellml_model_generation_time, num_vessels = run_image_to_model(target_image_path, resources_path, ilastik_path, model_path,
                                                                                          input_batch_processing_path, output_batch_processing_path, 
                                                                                          sub_volume=0.13, 
                                                                                          run_ilastik_batch_processing=False,
                                                                                          run_circ_autogen=True, 
                                                                                          bypass_network_gen_and_just_plot_binary_volume=False, 
                                                                                          plot_pls=False,
                                                                                          return_timing=True)

print("Image to model generation completed successfully!\n")

### Print network construction and cellml model generation timing(s)

print("Number of Vessels in Generated Network:", num_vessels)
print("Network Contruction Time:", network_construction_time)
print("CellML Model Generation Time:", cellml_model_generation_time, "\n")

# ##########################
# ### // Run pipeline // ###
# ##########################

# # Define the sub-volumes to test (0.10 to 0.15 in 0.01 intervals)
# # np.arange(0.10, 0.16, 0.01) creates the array: [0.10, 0.11, 0.12, 0.13, 0.14, 0.15]
# sub_volumes = np.arange(0.10, 0.16, 0.01)

# # Initialize empty lists to store the results of each loop
# num_vessels_list = []
# network_times_list = []
# cellml_times_list = []

# print("Starting batch analysis loop...")

# for sv in sub_volumes:
#     print(f"\n========================================")
#     print(f"Running pipeline for sub-volume: {sv:.2f}")
#     print(f"========================================")

#     # Make sure 'return_timing' is removed here if it's not defined in your image_to_model.py def signature
#     network_time, cellml_time, num_vessels = run_image_to_model(
#         target_image_path, 
#         resources_path, 
#         ilastik_path, 
#         model_path,
#         input_batch_processing_path, 
#         output_batch_processing_path, 
#         sub_volume=sv, 
#         run_ilastik_batch_processing=False,
#         run_circ_autogen=True, 
#         bypass_network_gen_and_just_plot_binary_volume=False, 
#         plot_pls=False,
#         return_timing=True
#     )

#     # Append the results of this iteration to our lists
#     num_vessels_list.append(num_vessels)
#     network_times_list.append(network_time)
#     cellml_times_list.append(cellml_time)

# print("\nImage to model batch generation completed successfully!\n")

# #########################################
# ### // Sort and Plot the Results // ###
# #########################################

# # It is good practice to sort the lists based on the X-axis (number of vessels) 
# # so the plotted lines connect smoothly from left to right.
# sorted_indices = np.argsort(num_vessels_list)
# sorted_vessels = np.array(num_vessels_list)[sorted_indices]
# sorted_network_times = np.array(network_times_list)[sorted_indices]
# sorted_cellml_times = np.array(cellml_times_list)[sorted_indices]

# # Set up the plot
# plt.figure(figsize=(10, 6))

# # Plot the two lines
# plt.plot(sorted_vessels, sorted_network_times, marker='o', color='blue', linewidth=2, label='Network Construction Time')
# plt.plot(sorted_vessels, sorted_cellml_times, marker='s', color='red', linewidth=2, linestyle='--', label='CellML Model Generation Time')

# # Add Labels, Title, and Grid
# plt.title('Run Time vs. Number of Vessels Generated', fontsize=14, fontweight='bold')
# plt.xlabel('Number of Vessels', fontsize=12)
# plt.ylabel('Run Time (seconds)', fontsize=12)
# plt.grid(True, linestyle=':', alpha=0.7)
# plt.legend(fontsize=11)

# # Save the plot as an image file in your current directory
# plt.savefig("runtime_vs_vessels_plot.png", dpi=300, bbox_inches='tight')
# print("Plot successfully saved as 'runtime_vs_vessels_plot.png'")

# # Display the plot in a pop-up window
# plt.show()
