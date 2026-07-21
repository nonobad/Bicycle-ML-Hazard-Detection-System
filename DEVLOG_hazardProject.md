##05/22/2026
Ultralytics install pip command was pulling Nvidia CUDA dependencies, causing the Pi to run out of memory. Considering the pi has no dedicated GPU and is going to be running a pre-trained ML model, I will be opting to install the "simple" ultralytics model using this command:

pip install ultralytics --extra-index-url https://pypi.org/simple/ --no-deps

##05/25/2026
Going to test if ultralytics is installed properly. Will try testing object recognition.
Object recognition works as intended-- as of current, I have a Python script that will output in text what objects the system thinks it sees. 

##05/29/2026
The output that Ultralytics gives is a Python object which can be queried. I will focus on just detecting a person as a hazard for now, as the test case I have in mind is going to be set in a quiet, residential area with a lot of parked cars. I don't want the system to notify me every time it sees a parked, non-hazardous car. I will have a volunteer walk in front me while I ride through an intersection, the volunteer will be detected by the system, and it will set off a buzzer which will notify me of a person having been detected.

I should see if the Ultralytics model or another tool can differentiate between moving and stationary objects in the future, which will be very helpful in determining if a car is a hazard or not.

##07/06/2026
The program will have 5 different Python scripts. 

1) Main.py will have a while loop that runs while the program is truly running (will implement the ability to terminate using a number or letter as input later). It will call the other scripts as needed 

2) constants.py will have values that shouldn't be changed inside of it for quick reference.

3)buzzer.py is responsible for anything that involves the buzzer/speaker connected to the pi. If you need the computer to make a funny beeping sound, use the implementations provided in this script.

4) detection.py will access video feed and run the yolo ML model to detect any hazards. will need to also implement the bounding box/region of interest here. we assume that the cyclist will be on a road, so we can say that the only hazardous objects will be what are directly in front of the cyclist-- we don't want to get beeped at because the program sees a person on the sidewalk, just because it sees something on the road in front of the rider.

5) stream.py may be implemented to access a video feed, could be useful for debugging

##07/21/2026
Scripts have been implemented for the most part. Could certainly use improvement, but the constants.py file has a list of hazards like cars, people, and other bicycles. From my brief testing today, I found detection.py can detect at least people and bicycles. The buzzer script works, but I didn't correctly implement a condition for it to stop beeping when the hazard is no longer detected. 


