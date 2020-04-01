#!/usr/bin/env python

# Import libraries
from gpiozero import MotionSensor, LED
from gpiozero import MCP3008
from signal import pause
from time import sleep

# Variables
pir = MotionSensor(4)
light = LED(16)
#adc = MCP3008(channel=0)

# Functions
def convert_temp(gen):
    for value in gen:
        yield (value * 3.3 - 0.5) * 100

# Program
#while True:
pir.when_motion = light.on
pir.when_no_motion = light.off
    #temp = convert_temp(adc.values)
    #print('The temperature is', temp, 'C')
    #sleep(1)
pause()
