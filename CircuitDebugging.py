from gpiozero import Buzzer, Button, LED
from gpiozero import PWMOutputDevice
from time import sleep

def playTone(frequency, duration):
    buzzer.frequency = frequency
    buzzer.value = 0.5

    sleep(duration)

    buzzer.value = 0

def testFunction():
    global ledOn
    ledOn = not ledOn

    if ledOn:
        testLED.on()
    else:
        testLED.off()

    playTone(1000, 1)


# Declare button
greenButton = Button(17)
greenButton.when_pressed = testFunction

# Declare led
testLED = LED(22)
ledOn = True

# Buzzer Stuff
buzzer = PWMOutputDevice(19)

while True:
    x = 5