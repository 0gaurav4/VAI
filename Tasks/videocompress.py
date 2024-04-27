# function to create video compression

def create_video_compression():
    from moviepy.editor import VideoFileClip

    video = VideoFileClip("car.mp4")
    video = video.subclip(3, 4)
    video = video.without_audio()
    video = video.resize(0.5)
    video = video.set_fps(30)
    video.write_videofile("compressed.mp4")
    
create_video_compression()