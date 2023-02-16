import cv2
import os
from natsort import natsorted
from time import sleep

from os.path import isfile, join
def convert_frames_to_video(pathIn, pathOut, fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
    files = natsorted(files) #

    #for sorting the file names properly
    print(len(files),"frames found in ", pathIn)
    sleep(1)
    print("Creating video...","[DO NOT TERMINATE THE PROGRAM]")
    for i in range(len(files)-1):
        filename = pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height,  width,  layers = img.shape
        size = (width, height)
        # print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
        
    out =  cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'mp4v'),  fps,  size)
    for i in range(len(frame_array)):
        #writing to a image  array
        out.write(frame_array[i])
    out.release()
    print("Video created successfully")
