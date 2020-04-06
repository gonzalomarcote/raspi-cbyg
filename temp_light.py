#!/usr/bin/env python

# Import libraries
import Adafruit_CharLCD as LCD
from gpiozero import LED
from gpiozero import MotionSensor, LED
from gpiozero import MCP3008
from signal import pause
from time import sleep


# Variables
pir = MotionSensor(4)
light = LED(16)
#adc = MCP3008(channel=0)
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD.
lcd_columns = 16
lcd_rows = 2

# Initialize LCD
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


# Functions
# Convert sensor temperature to celsius
def convert_temp(gen):
    for value in gen:
        yield (value * 3.3 - 0.5) * 100

# Get internal Raspberry CPU temperature
def cputemp():
    f = open("/sys/class/thermal/thermal_zone0/temp")
    CPUTemp = f.read()
    f.close()
    btemp = str(int(CPUTemp)/1000)
    return btemp


# Program:
lcd.message('  CBYG - RACK\n' + 'R:35  B:42  P:37')

while True:
    # Turn on/off led and lcd on pir motion
    pir.when_motion = light.on
    pir.when_no_motion = light.off
    #rtemp = convert_temp(adc.values)
    #print('The temperature is', rtemp, 'C')
    btemp = cputemp()
    if btemp >= 45:
        print('The raspberry pi temperature is high: ' + btemp)
    elif btemp < 45:
        print('The raspberry pi temperature is normal: ' + btemp)
    sleep(30)

pause()
