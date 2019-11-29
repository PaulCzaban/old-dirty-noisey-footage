"""
Extracts each frame in the source video file
"""
import cv2 as cv

vidcap = cv.VideoCapture('E:\\Source_Video.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
    cv.imwrite(f"E:\\0_Source\\{count:06d}.png", image)
    success,image = vidcap.read()
    count = count + 1
