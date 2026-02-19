################################
### // Initilaise Imports // ###
################################

from image_to_model import *

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
run_image_to_model(target_image_path, resources_path, ilastik_path, model_path,
                   input_batch_processing_path, output_batch_processing_path, 
                   sub_volume=0.1, 
                   run_ilastik_batch_processing=False,
                   run_circ_autogen=False, 
                   bypass_network_gen_and_just_plot_binary_volume=False, 
                   plot_pls=False)

### Print filepaths to vessel_array and parameter_array
print("Wrote:", str(CA_root / Path("dale_experimental/resources/user_output/image_to_model_vessel_array.csv")))
print("Wrote:", str(CA_root / Path("dale_experimental/resources/user_output/image_to_model_parameters.csv")))