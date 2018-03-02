#! /usr/bin/env python
import RPi.GPIO as gpio
import time
from gpios import gpio5

# Initialize wheels
def wheels_init():
    gpio.setmode(gpio.BOARD)

print gpio5
print "Welcome"
