import cv2
import mediapipe as mp
import numpy as np

mp_selfie_segmentation = mp.solutions.selfie_segmentation

# Load the video file
VIDEO_FILE = "car.mp4"

# Output video file name
OUTPUT_FILE = "outputcar.mp4"

# Background color
BG_COLOR = (192, 192, 192) # gray

# Create a video capture object
cap = cv2.VideoCapture(VIDEO_FILE)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Define the codec and create VideoWriter object
out = cv2.VideoWriter(OUTPUT_FILE, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

# Initialize MediaPipe Selfie Segmentation
with mp_selfie_segmentation.SelfieSegmentation(model_selection=1) as selfie_segmentation:
    while cap.isOpened():
        # Read a frame from the video
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert the frame from BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame for selfie segmentation
        results = selfie_segmentation.process(frame_rgb)
        
        # Extract the segmentation mask
        segmentation_mask = results.segmentation_mask
        
        # Create a condition for the segmentation mask
        condition = np.stack((segmentation_mask,) * 3, axis=-1) > 0.1
        
        # Create a background image
        bg_image = np.zeros(frame.shape, dtype=np.uint8)
        bg_image[:] = BG_COLOR
        
        # Replace the background with the input frame based on the segmentation mask
        output_frame = np.where(condition, frame, bg_image)
        
        # Write the output frame to the output video
        out.write(output_frame)

        # Display the output frame
        cv2.imshow('Output Video', output_frame)
        
        # Check for the 'q' key to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()
