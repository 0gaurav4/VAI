# function to create clip extractor

def create_clip_extractor():
    from moviepy.editor import VideoFileClip

    video = VideoFileClip("car.mp4")
    clip = video.subclip(3, 4)
    clip.write_videofile("clip.mp4")


create_clip_extractor()
    