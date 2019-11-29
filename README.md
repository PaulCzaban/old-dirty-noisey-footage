# Restoring old, dirty, noisey footage

Dedicated to restoring a badly captured 8mm film video file.



* Extracting Frames

I used the following python command to extract each frame. This is fps naive so you shouldn't get duplicate frames assuming the original source video has unique frames.

    import cv2 as cv
    
    vidcap = cv.VideoCapture('E:\\Source_Video.mp4')
    success,image = vidcap.read()
    count = 0
    success = True
    while success:
        cv.imwrite(f"E:\\0_Source\\{count:06d}.png", image)
        success,image = vidcap.read()
        count = count + 1


* Step 1 - Removing debris

I needed to do this step first as the source video was very dirty. Removing some of these artifacts will help later in the process.
This step involved running the source frames through an avisynth script. This method was chosen as it intelligently removes debris based on previous and next frames. 
The script was already written and it is by far the best, least intrusive option I could find (or create myself).
It can be found (here)[https://forum.doom9.org/showthread.php?t=144271]

I recommend installing AviSynth_260.exe and AvsPmod_v2.5.1 (tested on win 10). This will allow you to open avs scripts.

I 


https://github.com/PaulCzaban/old-dirty-noisey-footage/docs/1_Clean_Compare.png




To-do:
  Write a to-do list

To-do:
  Write a to-do list
