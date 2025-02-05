"""
1) Check if alarm sounds
2) Check if alarm is turned off
3) Check if it's 7AM or later
4) Check if it's a weekday
5) Check if it's 10AM or later
6) Check if it's a weekend
"""

###################################
# 1) Check if the alarm is sounding
###################################

###################################
# 2) Check if the alarm is turned off
###################################

###################################
# Code for 3-6
###################################

# Functions for date and time (3-6)
from datetime import datetime

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