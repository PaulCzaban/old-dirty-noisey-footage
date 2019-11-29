# Restoring old, dirty, noisey footage

Dedicated to restoring a badly captured 8mm film video file.



## Extracting Frames

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


## Cleaning

### Removing debris

I needed to do this step first as the source video was very dirty. Removing some of these artifacts will help later in the process.
This step involved running the source frames through an avisynth script. This method was chosen as it intelligently removes debris based on previous and next frames. 
The script was already written and it is by far the best, least intrusive option I could find (or create myself).
It can be found [here](https://forum.doom9.org/showthread.php?t=144271)

I recommend installing AviSynth_260.exe and AvsPmod_v2.5.1 (tested on win 10). This will allow you to open avs scripts.
I modifed the original script to import and export frames in PNG format. An analysis run of the script will start the export.
A copy of my avs script is located [here](https://github.com/PaulCzaban/old-dirty-noisey-footage/tree/master/scripts/avisynth_cleaning.avs).

**Cleaning Result**

![](https://github.com/PaulCzaban/old-dirty-noisey-footage/blob/master/docs/1_Clean_Compare.png?raw=true)
> Before and after debris cleaning.


### Removing projector noise

You'll notice that this source video is a recording of a projection rather than a telecine scan. This technique has introduced a lot of noise around the edges of the film and a bright spot in the middle.
Fortunately there is a segment during the recording where a white field is visible. I took and average of the white field to yeild correction image we could devide by the source frames.

**Average projector noise**

![](https://github.com/PaulCzaban/old-dirty-noisey-footage/blob/master/docs/2_Projector_Average.png?raw=true)
> Average projector noise before and after smoothing.

