################################
### // Initilaise Imports // ###
################################

from image_to_model import *
import matplotlib
matplotlib.use('Agg')
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

output_plot_dir = CA_root / "dale_experimental" / "resources" / "user_output" / "generated_plots"
os.makedirs(output_plot_dir, exist_ok=True)

#################################################
### // Initialise target image files paths // ###
#################################################

image_path_0 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_0.tif") # Image 0
image_path_1 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_1_seg.h5") # Image 1
image_path_2 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_2_seg.h5") # Image 2
image_path_3 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_3_WKY_CB.h5") # Image 2
image_input_path_list = np.array([image_path_0, image_path_1, image_path_2, image_path_3])
    
#################################################
### // Initialise target image files paths // ###
#################################################

image_path_0 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_0_seg_ORIGINAL.h5") # Image 0
image_path_1 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_1_seg.h5") # Image 1
image_path_2 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_2_seg.h5") # Image 2
image_path_3 = CA_root / Path("dale_experimental/resources/batch_process_output_folder/image_3_WKY_CB.h5") # Image 2
image_output_path_list = np.array([image_path_0, image_path_1, image_path_2, image_path_3])

################################################
### // Initialise file paths for pipeline // ###
################################################

ilastik_path = Path("/home/dsas627/Desktop/ilastik-1.4.1rc2-gpu-Linux/run_ilastik.sh") ### TODO: Delete/uncomment after docker integration is working
model_path = CA_root / Path("dale_experimental/resources/CB_WKY_2x2x2.ilp")
input_batch_processing_path = CA_root / Path("dale_experimental/resources/batch_process_input_folder")
output_batch_processing_path = CA_root / Path("dale_experimental/resources/batch_process_output_folder")

######################################
### // Verify Path(s) Existence // ###
######################################

# # create a dictionary of variable_name : path_value
# paths_to_check = {
#     "this_dir": this_dir,
#     "CA_root": CA_root,
#     "resources_path": resources_path,
#     "src_path": src_path,
#     "image_path_0": image_path_0,
#     "image_path_1": image_path_1,
#     "image_path_2": image_path_2,
#     "ilastik_path": ilastik_path,
#     "model_path": model_path,
#     "input_batch_processing_path": input_batch_processing_path,
#     "output_batch_processing_path": output_batch_processing_path
# }

# missing_paths = []

# for var_name, path_obj in paths_to_check.items():
#     # cast to string to handle both pathlib.Path objects and standard strings
#     if not os.path.exists(str(path_obj)):
#         missing_paths.append(f"{var_name}: {path_obj}")

# if not missing_paths:
#     print("All Paths Set Successfully!")
# else:
#     print(f"Error: Non-existent file paths detected ({len(missing_paths)}):")
#     for error in missing_paths:
#         print(f" - {error}")

#####################################
### // Initialise image target // ###
#####################################

### TODO: User to edit image_selection_index depending on which image (Image 0, Image 1, or Image 2) they would like to process.
image_selection_index = 0 ### Change value to 0, 1, or 2 depending on which image you would like to input into the pipeline
target_input_image_path = image_input_path_list[image_selection_index]
target_output_image_path = image_output_path_list[image_selection_index]

#############################################
### // Configure Pipeline Benchmarking // ###
#############################################

run_pipeline_benchmarking = False

if run_pipeline_benchmarking:


    ##########################
    ### // Run pipeline // ###
    ##########################

    # Define the sub-volumes to test (0.10 to 0.15 in 0.01 intervals)
    sub_volumes = np.arange(0.05, 0.1, 0.01)

    # Initialize empty lists to store the results of each loop
    num_vessels_list = []
    network_times_list = []
    cellml_times_list = []
    t_gen_files_list = []
    t_parse_list = []
    t_resolve_list = []
    t_flatten_list = []
    t_print_list = []
    t_analyser_list = []
    t_simulation_list = []

    print("Starting batch analysis loop...")

    for sv in sub_volumes:
        print(f"\n========================================")
        print(f"Running pipeline for sub-volume: {sv:.3f}")
        print(f"========================================")

        # NEW: Catch all the extra returned variables
        network_time, cellml_time, num_vessels, t_gen_files, t_parse, t_resolve, t_flatten, t_print, t_analyser, t_simulation = run_image_to_model(
            target_input_image_path, target_output_image_path, resources_path, ilastik_path, model_path,
            input_batch_processing_path, output_batch_processing_path, sub_volume=sv, 
            run_ilastik_batch_processing=False, run_circ_autogen=True, 
            bypass_network_gen_and_just_plot_binary_volume=False, plot_pls=False, return_timing=True,
            enable_giant_component_pruning=True,
            enable_topological_pruning=True,
            shannon_entropy_threshold=0.8,
            enable_morphological_closing=True,
            morphological_closing_size=3)
        # Append the results of this iteration to our lists
        num_vessels_list.append(num_vessels)
        network_times_list.append(network_time)
        cellml_times_list.append(cellml_time)
        t_gen_files_list.append(t_gen_files)
        t_parse_list.append(t_parse)
        t_resolve_list.append(t_resolve)
        t_flatten_list.append(t_flatten)
        t_print_list.append(t_print)
        t_analyser_list.append(t_analyser)
        t_simulation_list.append(t_simulation)

    print("\nImage to model batch generation completed successfully!\n")

    #########################################
    ### // Sort and Plot the Results // ###
    #########################################

    from scipy.optimize import curve_fit
    import csv

    # Sort lists based on the X-axis (number of vessels)
    sorted_indices = np.argsort(num_vessels_list)
    sorted_vessels = np.array(num_vessels_list)[sorted_indices]
    sorted_network_times = np.array(network_times_list)[sorted_indices]
    sorted_cellml_times = np.array(cellml_times_list)[sorted_indices]
    sorted_t_gen_files = np.array(t_gen_files_list)[sorted_indices]
    sorted_t_parse = np.array(t_parse_list)[sorted_indices]
    sorted_t_resolve = np.array(t_resolve_list)[sorted_indices]
    sorted_t_flatten = np.array(t_flatten_list)[sorted_indices]
    sorted_t_print = np.array(t_print_list)[sorted_indices]
    sorted_t_analyser = np.array(t_analyser_list)[sorted_indices]
    sorted_t_simulation = np.array(t_simulation_list)[sorted_indices]

    # ===============================================
    # NEW: Write Sorted Results to CSV
    # ===============================================
    csv_filename = "num_segments_vs_run_time.csv"
    print(f"Writing batch results to {csv_filename}...")

    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        # Write the expanded header row
        writer.writerow([
            'Number of Vessels', 'Network Construction Time (s)', 'Circ Autogen Time (s)', 
            'Generate Files Time (s)', 'Parse Model Time (s)', 'Resolve Imports Time (s)', 
            'Flatten Model Time (s)', 'Print Model Time (s)', 'Analyser Time (s)',
            'Model Simulation Time (s)'
        ])
        
        # Write the expanded data rows
        for v, net_t, cell_t, t_gen, t_par, t_res, t_fla, t_pri, t_ana, t_sim in zip(
            sorted_vessels, sorted_network_times, sorted_cellml_times,
            sorted_t_gen_files, sorted_t_parse, sorted_t_resolve,
            sorted_t_flatten, sorted_t_print, sorted_t_analyser,
            sorted_t_simulation
        ):
            writer.writerow([v, net_t, cell_t, t_gen, t_par, t_res, t_fla, t_pri, t_ana, t_sim])
            
    print("CSV successfully saved!\n")
    # ===============================================

    # ===============================================
    # FIGURE 1: Expanded Run Time vs. Vessels Plot
    # ===============================================
    # Increased figure width to accommodate the external legend
    plt.figure(figsize=(12, 7)) 

    # 1. Plot the Original Main Timers (Thicker lines for visibility)
    plt.plot(sorted_vessels, sorted_network_times, 'bo-', linewidth=2, label='Network Construction')
    plt.plot(sorted_vessels, sorted_cellml_times, 'ro-', linewidth=2, label='generate_with_new_architecture()')

    # 2. NEW: Plot the 7 Micro-Timers (Dashed lines with distinct markers)
    plt.plot(sorted_vessels, sorted_t_gen_files, linestyle='--', marker='s', label='generate_files() funcs')
    plt.plot(sorted_vessels, sorted_t_parse, linestyle='--', marker='^', label='parse_model()')
    plt.plot(sorted_vessels, sorted_t_resolve, linestyle='--', marker='v', label='resolve_imports')
    plt.plot(sorted_vessels, sorted_t_flatten, linestyle='--', marker='<', label='flatten_model()')
    plt.plot(sorted_vessels, sorted_t_print, linestyle='--', marker='>', label='print_model()')
    plt.plot(sorted_vessels, sorted_t_analyser, linestyle='--', marker='d', label='Analyser() Methods')
    plt.plot(sorted_vessels, sorted_t_simulation, linestyle='--', marker='X', label='Model Simulation')

    # Add Labels, Title, and Grid
    plt.title('Run Time vs. Number of Vessels Generated', fontsize=14, fontweight='bold')
    plt.xlabel('Number of Vessels', fontsize=12)
    plt.ylabel('Run Time (seconds)', fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.7)

    # FIXED: Move the massive legend outside of Figure 1!
    plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)
    plt.tight_layout() 

    # Save the plot as an image file in your current directory
    plt.savefig(output_plot_dir / "runtime_vs_vessels_plot.png", dpi=300, bbox_inches='tight')
    print(f"Plot successfully saved as '{output_plot_dir / 'runtime_vs_vessels_plot.png'}'")

    # ===============================================
    # FIGURE 2: Extrapolated Power Law Fit Plot
    # ===============================================

    # Define the power law function for curve fitting
    def power_func(x, a, b, c):
        return a * x**b + c

    try:
        print("\nFitting power law curves for extrapolation...")
        
        # Fit the main times
        # p0: initial guess [a, b, c] for a*x^b + c. Guessing b=2.0 (quadratic-ish) to start.
        popt_net, _ = curve_fit(power_func, sorted_vessels, sorted_network_times, p0=(0.01, 2.0, 0), maxfev=10000)
        popt_cellml, _ = curve_fit(power_func, sorted_vessels, sorted_cellml_times, p0=(0.01, 2.0, 0), maxfev=10000)

        # NEW: Safety fallback to prevent crashes if micro-timers are perfectly flat (0.0s)
        def robust_fit(y_data):
            try:
                popt, _ = curve_fit(power_func, sorted_vessels, y_data, p0=(0.01, 2.0, 0), maxfev=10000)
                return popt
            except:
                return [0, 1, 0] # Fallback to a linear line if it fails to converge

        # Fit the micro-timers
        popt_gen = robust_fit(sorted_t_gen_files)
        popt_parse = robust_fit(sorted_t_parse)
        popt_resolve = robust_fit(sorted_t_resolve)
        popt_flatten = robust_fit(sorted_t_flatten)
        popt_print = robust_fit(sorted_t_print)
        popt_analyser = robust_fit(sorted_t_analyser)
        popt_simulation = robust_fit(sorted_t_simulation)

        # --- NEW: Calculate R-squared (With safety for flat lines) ---
        def calculate_r_squared(y_true, y_pred):
            ss_tot = np.sum((y_true - np.mean(y_true))**2)
            if ss_tot == 0:  # Prevent division by zero
                return 0.0
            ss_res = np.sum((y_true - y_pred)**2)
            return 1 - (ss_res / ss_tot)

        # Calculate R-squared values for all 9 lines
        r2_net = calculate_r_squared(sorted_network_times, power_func(sorted_vessels, *popt_net))
        r2_cellml = calculate_r_squared(sorted_cellml_times, power_func(sorted_vessels, *popt_cellml))
        r2_gen = calculate_r_squared(sorted_t_gen_files, power_func(sorted_vessels, *popt_gen))
        r2_parse = calculate_r_squared(sorted_t_parse, power_func(sorted_vessels, *popt_parse))
        r2_resolve = calculate_r_squared(sorted_t_resolve, power_func(sorted_vessels, *popt_resolve))
        r2_flatten = calculate_r_squared(sorted_t_flatten, power_func(sorted_vessels, *popt_flatten))
        r2_print = calculate_r_squared(sorted_t_print, power_func(sorted_vessels, *popt_print))
        r2_analyser = calculate_r_squared(sorted_t_analyser, power_func(sorted_vessels, *popt_analyser))
        r2_simulation = calculate_r_squared(sorted_t_simulation, power_func(sorted_vessels, *popt_simulation))

        print(f"Network Construction Fit R-squared: {r2_net:.4f}")
        print(f"CellML Generation Fit R-squared: {r2_cellml:.4f}")
        print("Micro-timer fits successfully calculated.\n")
        # --------------------------------

        # ==========================================================
        # NEW: Limit the curve's domain to the actual data's max value
        # ==========================================================
        max_target = np.max(sorted_vessels)
        extrapolated_vessels = np.linspace(np.min(sorted_vessels), max_target, 100)

        # Set up the second figure (Expanded size to fit the external legend)
        plt.figure(figsize=(12, 7))

        # ==========================================================
        # Scatter the original recorded data points for reference
        # ==========================================================
        # Main Timers
        plt.scatter(sorted_vessels, sorted_network_times, color='blue', s=40, zorder=5)
        plt.scatter(sorted_vessels, sorted_cellml_times, color='red', s=40, marker='s', zorder=5)

        # NEW: Micro-Timers (Colors match their extrapolated lines)
        plt.scatter(sorted_vessels, sorted_t_gen_files, color='green', s=40, marker='^', zorder=5)
        plt.scatter(sorted_vessels, sorted_t_parse, color='orange', s=40, marker='v', zorder=5)
        plt.scatter(sorted_vessels, sorted_t_resolve, color='purple', s=40, marker='<', zorder=5)
        plt.scatter(sorted_vessels, sorted_t_flatten, color='brown', s=40, marker='>', zorder=5)
        plt.scatter(sorted_vessels, sorted_t_print, color='pink', s=40, marker='d', zorder=5)
        plt.scatter(sorted_vessels, sorted_t_analyser, color='gray', s=40, marker='P', zorder=5)
        plt.scatter(sorted_vessels, sorted_t_simulation, color='cyan', s=40, marker='X', zorder=5)

        # Plot the main extrapolated curves
        plt.plot(extrapolated_vessels, power_func(extrapolated_vessels, *popt_net), color='blue', linestyle='--', linewidth=2, alpha=0.8, label=f'Network Construction ($R^2$={r2_net:.3f})')
        plt.plot(extrapolated_vessels, power_func(extrapolated_vessels, *popt_cellml), color='red', linestyle='--', linewidth=2, alpha=0.8, label=f'generate_with_new_architecture() ($R^2$={r2_cellml:.3f})')
        
        # Plot the micro-timer extrapolated curves
        plt.plot(extrapolated_vessels, power_func(extrapolated_vessels, *popt_gen), linestyle=':', color='green', linewidth=2, label=f'generate_files() funcs ($R^2$={r2_gen:.3f})')
        plt.plot(extrapolated_vessels, power_func(extrapolated_vessels, *popt_parse), linestyle=':', color='orange', linewidth=2, label=f'parse_model() ($R^2$={r2_parse:.3f})')
        plt.plot(extrapolated_vessels, power_func(extrapolated_vessels, *popt_resolve), linestyle=':', color='purple', linewidth=2, label=f'resolve_imports() ($R^2$={r2_resolve:.3f})')
        plt.plot(extrapolated_vessels, power_func(extrapolated_vessels, *popt_flatten), linestyle=':', color='brown', linewidth=2, label=f'flatten_model() ($R^2$={r2_flatten:.3f})')
        plt.plot(extrapolated_vessels, power_func(extrapolated_vessels, *popt_print), linestyle=':', color='pink', linewidth=2, label=f'print_model() ($R^2$={r2_print:.3f})')
        plt.plot(extrapolated_vessels, power_func(extrapolated_vessels, *popt_analyser), linestyle=':', color='gray', linewidth=2, label=f'Analyser() Methods ($R^2$={r2_analyser:.3f})')
        plt.plot(extrapolated_vessels, power_func(extrapolated_vessels, *popt_simulation), linestyle=':', color='cyan', linewidth=2, label=f'Model Simulation ($R^2$={r2_simulation:.3f})')

        # Format the Graph
        # Dynamically update the title to show the maximum extrapolated target
        plt.title(f'Extrapolated Run Time vs. Number of Vessels (Up to {int(max_target)})', fontsize=14, fontweight='bold')
        plt.xlabel('Number of Vessels', fontsize=12)
        plt.ylabel('Run Time (seconds)', fontsize=12)
        plt.grid(True, which='both', linestyle=':', alpha=0.7)

        # ==========================================================
        # NEW: Automatically Scale X and Y Axes to Maximum Values
        # ==========================================================
        # 1. Scale X-axis from 0 to the maximum extrapolated target
        plt.xlim(0, max_target)

        # 2. Find the highest Y value across all 8 extrapolated curves
        max_y_values = [
            np.max(power_func(extrapolated_vessels, *popt_net)),
            np.max(power_func(extrapolated_vessels, *popt_cellml)),
            np.max(power_func(extrapolated_vessels, *popt_gen)),
            np.max(power_func(extrapolated_vessels, *popt_parse)),
            np.max(power_func(extrapolated_vessels, *popt_resolve)),
            np.max(power_func(extrapolated_vessels, *popt_flatten)),
            np.max(power_func(extrapolated_vessels, *popt_print)),
            np.max(power_func(extrapolated_vessels, *popt_analyser))
        ]
        absolute_max_y = max(max_y_values)

        # 3. Scale Y-axis from 0 to the absolute maximum Y value (+5% headroom so the curve doesn't hit the ceiling)
        plt.ylim(0, absolute_max_y * 1.05)
        # ==========================================================

        # Move the legend outside to avoid covering the 8 curve lines
        plt.legend(loc='upper left', bbox_to_anchor=(1.02, 1), borderaxespad=0.)
        plt.tight_layout()

        # Save the new extrapolated plot
        plt.savefig(output_plot_dir / "extrapolated_runtime_plot.png", dpi=300, bbox_inches='tight')
        print(f"Extrapolated plot successfully saved as '{output_plot_dir / 'extrapolated_runtime_plot.png'}'")

    except Exception as e:
        print(f"\nCould not fit the curves to the data: {e}")
        print("This can happen if the data isn't cleanly exponential or if the initial guesses are too far off.")

    # Display both plots in pop-up windows
    # plt.show()

else:

    ##########################
    ### // Run pipeline // ###
    ##########################

    ### Run pipeline
    network_construction_time, cellml_model_generation_time, num_vessels, *rest = run_image_to_model(target_input_image_path, target_output_image_path, resources_path, ilastik_path, model_path,
                                                                                            input_batch_processing_path, output_batch_processing_path, 
                                                                                            sub_volume=1.0, 
                                                                                            run_ilastik_batch_processing=False,
                                                                                            run_circ_autogen=False, 
                                                                                            bypass_network_gen_and_just_plot_binary_volume=False, 
                                                                                            plot_pls=True,
                                                                                            return_timing=True,
                                                                                            enable_giant_component_pruning=True,
                                                                                            enable_topological_pruning=True,
                                                                                            shannon_entropy_threshold=1.0,
                                                                                            enable_morphological_closing=True,
                                                                                            morphological_closing_size=3,
                                                                                            ilastik_workflow="pixel classification")

    print("Image to model generation completed successfully!\n")

    ### Print network construction and cellml model generation timing(s)

    print("Number of Vessels in Generated Network:", num_vessels)
    print("Network Contruction Time:", network_construction_time)
    print("CellML Model Generation Time:", cellml_model_generation_time, "\n")

    ### // NOTES TO SELF FOR LATER // ###
    ### Add feature to configure disable largest connected component pruning
    ### Compare network skeletonisation output from this version to the old working version
    ### Ask Gemini to try recover my notes to self before I rolled back the commit