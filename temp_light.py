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
    btemp = int(CPUTemp)/1000
    return btemp


while True:

    # Check temp
    btemp = cputemp()
    print('The raspberry pi temperature is: ' + str(btemp) + 'C')
    #rtemp = convert_temp(adc.values)
    #print('The external rack temperature is: ' + str(rtemp) + 'C')

    # Turn on/off led and lcd on pir motion for 30 seconds
    if pir.motion_detected:
        print('Door open')
        light.on()
        lcd.message('  CBYG - RACK\n' + 'R:35  B:' + str(int(round(btemp))) +  '  P:37')
        sleep(30)
    else:
        print('Door closed')
        light.off()
