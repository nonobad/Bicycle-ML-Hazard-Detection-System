##05/22/2026
Ultralytics install pip command was pulling Nvidia CUDA dependencies, causing the Pi to run out of memory. Considering the pi has no dedicated GPU and is going to be running a pre-trained ML model, I will be opting to install the "simple" ultralytics model using this command:

pip install ultralytics --extra-index-url https://pypi.org/simple/ --no-deps

##05/25/2026
Going to test if ultralytics is installed properly. Will try testing object recognition.
Object recognition works as intended-- as of current, I have a Python script that will output in text what objects the system thinks it sees. 

##05/29/2026
The output that Ultralytics gives is a Python object which can be queried. I will focus on just detecting a person as a hazard for now, as the test case I have in mind is going to be set in a quiet, residential area with a lot of parked cars. I don't want the system to notify me every time it sees a parked, non-hazardous car. I will have a volunteer walk in front me while I ride through an intersection, the volunteer will be detected by the system, and it will set off a buzzer which will notify me of a person having been detected.

I should see if the Ultralytics model or another tool can differentiate between moving and stationary objects in the future, which will be very helpful in determining if a car is a hazard or not.


