# Création vidéo
import os

import cv2
import ffmpeg


# FPS = 60
# seconds = 15
# audio = ffmpeg.input('audio.mp3')


def makevideo():
    video_name = 'pouet.avi'
    frame = cv2.imread('test.jpeg')
    frameflip = cv2.flip(frame, 0)
    frameflip = cv2.putText(frameflip, "WHAT THE FUCK LES AMIS", (500,500), fontFace = cv2.FONT_HERSHEY_SIMPLEX, fontScale = 1, color = (255, 0, 0))
    height, width, layers = frame.shape
    video = cv2.VideoWriter(video_name, 0, 1, (width, height))
    
    for i in range(0, 10):
        if (i % 2) == 0:
            video.write(frameflip)
        else:
            video.write(frame)
    video.release()
    ffmpeg.concat(ffmpeg.input('pouet.avi'), ffmpeg.input('audio.mp3'), v=1, a=1).output('YAHO.mp4').overwrite_output()\
        .run()

    os.remove('test.jpeg')
    os.remove('pouet.avi')
