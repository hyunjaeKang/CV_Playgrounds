import cv2
import os
import argparse


def extract_frames(video_path, output_folder, fps=10.0, flipcode=-2, img_rotate= 0):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    # Get the video's frame rate
    video_fps = video_capture.get(cv2.CAP_PROP_FPS)
    
    # Calculate the time interval between frames to match the desired fps
    time_interval = 1.0 / fps  # in seconds
    video_time_per_frame = 1.0 / video_fps  # in seconds
    
    current_time = 0.0
    saved_frame_count = 0
    frame_count = 0
    
    while True:
        ret, frame = video_capture.read()
        if flipcode in [-1, 0, 1]:
            frame = cv2.flip(frame, flipcode)
        if img_rotate in [1, 2, 3]:
            if img_rotate == 1:
                frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            elif img_rotate == 2:
                frame = cv2.rotate(frame, cv2.ROTATE_180)
            elif img_rotate == 3:
                frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        if not ret:
            break  # Exit if no frame is returned
        
        # Determine if the frame should be saved
        if current_time >= saved_frame_count * time_interval:
            frame_filename = os.path.join(output_folder, f"frame_{saved_frame_count:04d}.jpg")
            cv2.imwrite(frame_filename, frame)
            saved_frame_count += 1
        
        # Update the current time based on the video's frame rate
        current_time += video_time_per_frame
        frame_count += 1
    
    # Release the video capture object
    video_capture.release()
    print(f"Saved {saved_frame_count} frames at {fps} fps to '{output_folder}'.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_path", help="Path of the video file", required=True)
    parser.add_argument("--output_dir", help="Image output directory", required=True)
    parser.add_argument("--fps", type=float, help="Frames per second to extract", required=True)
    parser.add_argument("--flip", type=int, help="flip image 1, 0, -1", default=-2)
    parser.add_argument("--img_rotate", type=int, help="rotate 1 (90), 2 (180), 3 (270)", default=0)

    args = parser.parse_args()

    extract_frames(args.video_path, args.output_dir, fps=args.fps, flipcode=args.flip, img_rotate=args.img_rotate)