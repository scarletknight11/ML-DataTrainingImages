
import cv2
import numpy as np
import os

# we will save images in images folder
save_path="images"

list_videos=os.listdir("videos")
print(list_videos)
running_count=1

# loop through each videos
for i in range(len(list_videos)):
    # path of each video
    path="videos/"+list_videos[i]
    # then we will use video capture to read video
    cap=cv2.VideoCapture(path)
    # loop through each frame
    count=1
    while(cap.isOpened()):
        ret,frame=cap.read()
        # ret is false when frame is null
        # ret is true when frame is not null
        count=count+1
        if ret==True:
            # do process
            # now create a counter to save photo every 30 frames
            if(count%30==0):
                # save image
                # now we will create another counter which will increase
                # every 30 frames by 1
                cv2.imwrite(save_path+"/"+str(running_count)+".jpg",frame)
                running_count=running_count+1
                
        else:
            cap.release()

            
         
           
