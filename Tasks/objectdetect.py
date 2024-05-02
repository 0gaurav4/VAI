import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import colors, Annotator

def process_video(input_video_path, output_video_path, model_path="yolov8n.pt", center_point=(-10, 480)):
    # Load YOLO model
    model = YOLO(model_path)
    names = model.model.names
    
    # Open video capture
    cap = cv2.VideoCapture(input_video_path)
    w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
    
    # Define video writer
    out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*'MJPG'), fps, (w, h))
    
    while True:
        ret, im0 = cap.read()
        if not ret:
            print("Video frame is empty or video processing has been successfully completed.")
            break

        # Predict using YOLO model
        results = model.predict(im0)
        boxes = results[0].boxes.xyxy.cpu()
        clss = results[0].boxes.cls.cpu().tolist()

        annotator = Annotator(im0, line_width=2)

        for box, cls in zip(boxes, clss):
            annotator.box_label(box, label=names[int(cls)], color=colors(int(cls)))
            annotator.visioneye(box, center_point)

        # Write annotated frame to output video
        out.write(im0)
        cv2.imshow("visioneye-pinpoint", im0)

        # Check for user input to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    out.release()
    cap.release()
    cv2.destroyAllWindows()

# Example usage:
process_video("car.mp4", "visioneye-pinpoint.avi")
