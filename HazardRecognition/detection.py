##Interacts with the yolo model in order to detect hazards.

from ultralytics import YOLO ##the yolo machine learning model that will be used
import cv2 ##

model = YOLO("yolov8n.pt")