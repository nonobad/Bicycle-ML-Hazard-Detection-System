##Responsible for running the main loop of this program.abs, and for interacting with cameras to pass video frames as needed.

import cv2 ##python module for opencv (vision library)
import constants ##script to store constant values for this program.
import buzzer ##script responsible for buzzer interactions
import detection ##script that uses yolo to handle object detection
running = True ## boolean value set to true so that the loop can start. should the user properly terminate this program, set running to False.

##rough pseudocode of what main does

##tell opencv which camera to use 
##the pi will use an external camera, so be sure to set the argument passed to VideoCapture as 0 when running this program on the pi.
##currently set to 1 to avoid using built-in laptop webcam

##while the program runs,
    ##get a frame from the camera, read it          
    ##buzz/beep if needed
    ##if frame grab fails, skip it
        ##grab the next frame

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read() ##return frame if camera provides one
    if not ret:
        continue  ##if a frame is missed, continue to the next frame
    
    hazardDetected = detection.detect(frame) ## bool variable to store the hazard detection state
                                             ## passes the video frame to the detect function as an argument so the model can detect hazards

    if hazardDetected:  ## if hazardDetected is true
        buzzer.beep()  ## beep


    
