import os
import shutil

def rename_and_move_videos(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List all files in the input folder
    for filename in os.listdir(input_folder):
        # Check if the file is a video file
        if filename.lower().endswith(('.mp4', '.avi', '.mov', '.mkv', '.flv')):
            # Construct the new filename
            parts = filename.split('_', 2)
            if len(parts) >= 3:
                new_filename = f"{parts[1]}_{parts[2]}"
                old_file_path = os.path.join(input_folder, filename)
                new_file_path = os.path.join(output_folder, new_filename)

                # Move and rename the file
                shutil.move(old_file_path, new_file_path)
                print(f"Renamed and moved: {filename} -> {new_filename}")

if __name__ == "__main__":
    # Define your input and output folder paths
    input_folder = "E:/editedVideos/2020"
    output_folder = "E:/editedVideos/2020"

    # Call the function to rename and move videos
    rename_and_move_videos(input_folder, output_folder)
