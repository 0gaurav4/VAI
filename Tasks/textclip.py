
# Function to create a video with text overlay
def create_video_with_text():
    from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

    video = VideoFileClip("car.mp4").subclip(3, 4)

    # Make the text. Many more options are available.
    txt_clip = (TextClip("Video Editing AI", fontsize=70, color='white')
                .set_position('center')
                .set_duration(10))

    result = CompositeVideoClip([video, txt_clip])  # Overlay text on video
    result.write_videofile("edited.webm", fps=25)

    create_video_with_text()