# function to create speed adjustment of video


def create_speed_adjustment():
    from moviepy.editor import VideoFileClip, concatenate
    video = VideoFileClip("car.mp4")
    video = video.subclip(3, 4)
    video = video.speedx(0.5)
    video.write_videofile("speed.mp4")

def create_high_low_speed():
    from moviepy.editor import VideoFileClip, concatenate
    video = VideoFileClip("car.mp4")
    video_high_speed = video.subclip(3, 4).speedx(2)  # High speed segment
    video_low_speed = video.subclip(4, 5).speedx(0.5)  # Low speed segment

    final_video = concatenate([video_high_speed, video_low_speed])
    final_video.write_videofile("high_low_speed.mp4")

create_high_low_speed()
    
create_speed_adjustment()