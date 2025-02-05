"""
1) Check if alarm sounds
2) Check if alarm is turned off
3) Check if it's 7AM or later
4) Check if it's a weekday
5) Check if it's 10AM or later
6) Check if it's a weekend
"""

# Functions for button and buzzer (1 and 2)
from gpiozero import Button, PWMOutputDevice
from time import sleep

# Functions for date and time (3-6)
from datetime import datetime

###################################
# 1) Check if the alarm is sounding
###################################

# Create global variable for if alarm is playing
alarmSounding = False

# Define the buzzer to play the alarm ringtone
buzzer = PWMOutputDevice(19)
        
# Function to play a note (from ChatGPT)
def play_note(frequency, duration):
    if frequency == 0:  # Rest note
        buzzer.value = 0
    else:
        buzzer.frequency = frequency
        buzzer.value = 0.5  # Set duty cycle to 50% for sound
    
    sleep(duration)  # Hold the note
    buzzer.value = 0  # Stop the sound
    sleep(0.05)  # Small delay between notes


# Define function to play Twinkle Twinkle Little Star on the alarm
def playAlarmMelody():
        
        # Code for Twinkle Twinkle Little Start modified from ChatGPT
        # Define note frequencies (in Hz)
        NOTE_C4 = 261
        NOTE_D4 = 294
        NOTE_E4 = 329
        NOTE_F4 = 349
        NOTE_G4 = 391
        NOTE_A4 = 440
        NOTE_B4 = 493
        NOTE_C5 = 523

        # Define the melody (Twinkle Twinkle Little Star)
        melody = [
        NOTE_C4, NOTE_C4, NOTE_G4, NOTE_G4, NOTE_A4, NOTE_A4, NOTE_G4,
        NOTE_F4, NOTE_F4, NOTE_E4, NOTE_E4, NOTE_D4, NOTE_D4, NOTE_C4
        ]

        # Define note durations (1 = whole note, 0.5 = half note, etc.)
        durations = [
        0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1,
        0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 1
        ]
        
        # Play the melody
        for note, duration in zip(melody, durations):
                play_note(note, duration)

        print("Melody finished!")        

# Define function to sound or quiet alarm
def toggleAlarm():
        # Toggle the alarmSounding variable each time the button is pushed
        global alarmSounding
        alarmSounding = not alarmSounding

        # if the song doesn't work, just turn the buzzer on or off        
        # buzzer = Buzzer(19)
        
        # If the alarm should be sounding, turn the buzzer on
        if alarmSounding:
                # buzzer.on()
                playAlarmMelody()
        # else:
        #         # buzzer.off()
                
# Declare button to turn the alarm on or off
soundAlarmButton = Button(18)
soundAlarmButton.when_pressed = toggleAlarm

###################################
# 2) Check if the alarm is turned off
###################################

# Declare global alarm turned off bool
alarmTurnedOff = False

# Define the function to be called when the button is pressed
def turnOffAlarm():
    global alarmTurnedOff
    alarmTurnedOff = True

# Declare the turnOff button on GPIO pin 17
turnOffAlarmButton = Button(17)

# Attach the function to the button press event
turnOffAlarmButton.when_pressed = turnOffAlarm

###################################
# Code for 3-6
###################################

# Find the current time
currentTime = datetime.now()

# Find the current hour
currentHour = currentTime.hour

# Find current day
currentDayName = currentTime.strftime("%A")

# Find day number of the week (1 = M, 7 = Sun)
currentDayNumber = currentTime.isoweekday()

###################################
# 3) Check if it's 7AM or later
###################################
if currentHour >= 7:
        weekdayTime = True
else:
        weekdayTime = False

###################################
# 4) Check if it's a weekday
# 6) Check if it's a weekend
###################################
if currentDayName <= 5:
        isWeekday = True
else:
        isWeekday = False

###################################
# 5) Check if it's 10AM or later
###################################
if currentHour >= 10:
        weekendTime = True
else:
        weekendTime = False
        
###################################
# 
###################################