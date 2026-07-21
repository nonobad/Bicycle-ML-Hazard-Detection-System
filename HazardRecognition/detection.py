##Interacts with the yolo model in order to detect hazards.

from ultralytics import YOLO ##the yolo machine learning model that will be used
import cv2 ##python module for opencv (vision library)
import constants

model = YOLO("yolov8n.pt") ##using yolo model version 8

def detect(frame):
    results = model(Frame, verbose = False)
    for result in results:
        for cls in result.boxes.cls:
            label = model.names[int(cls)]
            if label in constants.HAZARD_CLASSES:
                return True
    return False
    