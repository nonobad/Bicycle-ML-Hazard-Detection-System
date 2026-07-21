##Responsible for anything involving the buzzer/speaker connected to the pi.

from gpiozero import Buzzer ##use the buzzer script from gpiozero library for commands that turn on the buzzer

from time import sleep  ##use sleep script to simulate a pause in the beeping

buzzer = Buzzer(4)

def beep():
    buzzer.on()
    sleep(1)
    buzzer.off()
    sleep(1)    ##only beeping twice is defined for now, placeholder