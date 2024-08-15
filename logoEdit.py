import cv2
import numpy as np
import os
import time
from moviepy.editor import VideoFileClip

def process_video(input_path, output_path):
    start_time = time.time()
    
    # Open the video file
    cap = cv2.VideoCapture(input_path)
    if not cap.isOpened():
        print(f"Error opening video file {input_path}")
        return
    
    # Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    temp_video_path = 'temp_output.avi'
    out = cv2.VideoWriter(temp_video_path, fourcc, fps, (frame_width, frame_height))
    
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    current_frame = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Define the range of yellow color in HSV
        lower_yellow = np.array([20, 100, 100])
        upper_yellow = np.array([30, 255, 255])
        
        # Threshold the HSV image to get only yellow colors
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        
        # Find contours of the yellow regions
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for contour in contours:
            # Get the bounding box of the contour
            x, y, w, h = cv2.boundingRect(contour)
            # Replace yellow rectangle with white
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), -1)
        
        # Write the frame to the output video
        out.write(frame)
        
        # Update progress
        current_frame += 1
        elapsed_time = time.time() - start_time
        estimated_time = (elapsed_time / current_frame) * (frame_count - current_frame)
        print(f"Processed {current_frame}/{frame_count} frames - Estimated time remaining: {estimated_time:.2f} seconds", end='\r')
    
    # Release everything when done
    cap.release()
    out.release()
    cv2.destroyAllWindows()

    # Use moviepy to combine the processed video with the original audio
    video_clip = VideoFileClip(temp_video_path)
    audio_clip = VideoFileClip(input_path).audio
    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile(output_path, codec='libx264')

    # Remove temporary file
    os.remove(temp_video_path)

    print(f"Video processed and saved to {output_path}. Time taken: {time.time() - start_time:.2f} seconds")

def process_videos_in_folder(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    start_time = time.time()
    video_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.avi', '.mov'))]
    total_videos = len(video_files)
    
    for i, filename in enumerate(video_files):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        print(f"Processing video {i + 1}/{total_videos}: {input_path}...")
        process_video(input_path, output_path)
        print(f"Saved edited video to {output_path}")
    
    total_time = time.time() - start_time
    print(f"All videos processed. Total time taken: {total_time:.2f} seconds")

# Example usage:
input_folder = 'E:/savedVideo/2022'
output_folder = 'E:/editedVideos/2014'
process_videos_in_folder(input_folder, output_folder)
