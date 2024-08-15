from moviepy.editor import VideoFileClip
import os

def cut_video(input_path, output_path, cut_start, cut_end):
    """
    Cuts a portion from the start to cut_end and saves the remaining part.
    
    Parameters:
        input_path (str): Path to the input video file.
        output_path (str): Path to save the output video file.
        cut_start (float): Start time in seconds to begin cutting.
        cut_end (float): End time in seconds to stop cutting.
    """
    try:
        # Load the video
        video = VideoFileClip(input_path)
        
        # Check if the cut_end is within the video's duration
        if cut_end > video.duration:
            cut_end = video.duration
        
        # Define the remaining portion
        remaining_video = video.subclip(cut_end, video.duration)
        
        # Write the result to the output file
        remaining_video.write_videofile(output_path, codec="libx264")
        print(f"Processed {input_path} and saved to {output_path}")
        
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def process_videos(input_folder, output_folder, cut_start, cut_end):
    """
    Processes all video files in the given directory, cutting the specified portion.
    
    Parameters:
        input_folder (str): Directory containing video files.
        output_folder (str): Directory to save the processed video files.
        cut_start (float): Start time in seconds to begin cutting.
        cut_end (float): End time in seconds to stop cutting.
    """
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.mp4', '.avi', '.mov')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, f"processed_{filename}")
            cut_video(input_path, output_path, cut_start, cut_end)

# Define parameters
input_folder = 'G:/EDITED\Math/2022'
output_folder = 'E:/savedVideo/2022'
cut_start = 0      # Start time of the portion to cut (in seconds)
cut_end = 4.2      # End time of the portion to cut (in seconds)

# Process the videos
process_videos(input_folder, output_folder, cut_start, cut_end)
