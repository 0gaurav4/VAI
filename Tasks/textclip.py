
# Function to create a video with text overlay
import os
def create_video_with_text(video_path="car.mp4", 
                           start_time=3, 
                           end_time=4, 
                           text="Video Editing AI",
                           fontsize=70,
                           position='center', # center | left | right
                           color='white',
                           duration=10,
                           ):
    save_path = f"static/results/edited_{os.path.basename(video_path)}"
    from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

    video = VideoFileClip(video_path).subclip(3, 4)

    # Make the text. Many more options are available.
    txt_clip = (TextClip(text, fontsize=fontsize, color=color)
                .set_position(position)
                .set_duration(duration))

    result = CompositeVideoClip([video, txt_clip])  # Overlay text on video
    result.write_videofile(f"edited.webm", fps=25)
    return save_path

if __name__ == "__main__":
    create_video_with_text()