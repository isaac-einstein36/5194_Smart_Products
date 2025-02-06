from gpiozero import Buzzer, Button, LED
from time import sleep

def testFunction():
    print("Hello World")

# Declare button
greenButton = Button(17)
greenButton.when_pressed = testFunction