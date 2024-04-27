# background removal

def create_video_background_removal():
    import cv2
    from moviepy.editor import VideoFileClip
    video = VideoFileClip("car.mp4")
    
    def remove_background(frame):
        bgr_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        gray_frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray_frame, 100, 255, cv2.THRESH_BINARY_INV)
        masked_frame = cv2.bitwise_and(bgr_frame, bgr_frame, mask=mask)
        return cv2.cvtColor(masked_frame, cv2.COLOR_BGR2RGB)
    
    modified_video = video.fl_image(remove_background)
    modified_video.write_videofile("remove_background.mp4", codec="libx264", audio_codec="aac", fps=video.fps)

create_video_background_removal()
