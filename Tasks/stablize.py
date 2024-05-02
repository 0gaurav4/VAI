# import cv2
# from stabilization_module import StabilizationPipeline
# def video_stablize(input_video, output_video, model="mobilenet_ssd", device='cuda'):
#     """
#     Perform video stabilization on a given video.

#     Parameters:
#     - input_video (str): Path to the input video.
#     - output_video (str): Path to save the stabilized video.
#     - model (str, optional): Name of the model to use for stabilization. Defaults to 'mobilenet_ssd'.
#     - device (str, optional): Device to perform computation on. Defaults to 'cuda'.

#     Returns:
#     - None
#     """

#     # Load the input video
#     video = cv2.VideoCapture(input_video)

#     # Get video properties
#     fps = video.get(cv2.CAP_PROP_FPS)
#     width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     # Create the output video writer
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#     output = cv2.VideoWriter(output_video, fourcc, fps, (width, height))

#     # Initialize the stabilization pipeline
#     pipeline = StabilizationPipeline(model=model, device=device)

#     # Process each frame of the video
#     success, frame = video.read()
#     while success:
#         # Perform stabilization on the frame
#         stabilized_frame = pipeline.process_frame(frame)

#         # Write the stabilized frame to the output video
#         output.write(stabilized_frame)

#         # Read the next frame
#         success, frame = video.read()

#     # Release the video capture and writer objects
#     video.release()
#     output.release()

#     # Print a success message
#     print("Video stabilization successful!")
