import os
import subprocess
import deflicker as deflicker
import cv2 as cv
import numpy as np

#The averaged white field
background_noise = cv.imread("E:\\Projector_white_field\\average.png")

# Batch processing - Get images to process
images = deflicker.find_images("E:\\1_Cleaned\\", ".png")

mod = 0.62

for img in images:

    frame = cv.imread(img)
    
    modded_background_noise = background_noise / (mod)

    new_image = (frame / modded_background_noise) * 255

    filename = img.split('\\')[len(img.split('\\'))-1]
    cv.imwrite(f'E:\\2_Projector_Corrected\\{filename}', new_image)










frames = []
images = deflicker.find_images("E:\\Projector_white_field\\", ".png")

imageTotal = len(images)

imgCount = 0

for img in images:

    frame = cv.imread(img)
    floatImage = np.float32(frame)

    if imgCount == 0:
        avg = floatImage
    else:
        cv.accumulateWeighted(floatImage,avg,0.001)
        res = cv.convertScaleAbs(avg)

    imgCount = imgCount + 1

cv.imwrite(f'E:\\Projector_white_field\\average.png', res)

h = 5
hColor = 10
templateWindowSize = 7
searchWindowSize = 21
background_noise = cv.fastNlMeansDenoisingColored(res,None,h,hColor,templateWindowSize,searchWindowSize)

cv.imwrite(f'E:\\Projector_white_field\\average_smoothed.png', background_noise)
