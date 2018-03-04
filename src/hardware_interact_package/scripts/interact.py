#! /usr/bin/env python
from gpiozero import LED, PWMOutputDevice
from time import sleep
from gpios import gpio40, gpio38, gpio37, gpio36

led = LED(gpio40)

while True:
    led.on()
    sleep(3)
    led.off()
    sleep(1)

# DC Motors/Wheels GPIO mapping
#dc_motor_IN1 = PWMOutputDevice(gpio36)
#dc_motor_IN2 = PWMOutputDevice(gpio37)
#dc_motor_IN3 = PWMOutputDevice(gpio38)
#dc_motor_IN4 = PWMOutputDevice(gpio40)


# Control robot using gpiozero lib
# Create Robot instance

'''robot = Robot(left=(gpio36,gpio37), right=(gpio38, gpio40))
robot.forward()
robot.backward()
robot.reverse()
robot.forward(0.5)
robot.right()
robot.left(0.5)
robot.stop()
'''

# Initialize Wheels
'''def wheels_init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(dc_motor_IN1, gpio.OUT)
    gpio.setup(dc_motor_IN2, gpio.OUT)
    gpio.setup(dc_motor_IN3, gpio.OUT)
    gpio.setup(dc_motor_IN4, gpio.OUT)

def go_forward():
    wheels_init()
    gpio.output(dc_motor_IN1, True)
    gpio.output(dc_motor_IN2, False)
    gpio.output(dc_motor_IN3, False)
    gpio.output(dc_motor_IN4, True)

def backward():
    wheels_init()
    gpio.output(dc_motor_IN1, False)
    gpio.output(dc_motor_IN2, True)
    gpio.output(dc_motor_IN3, True)
    gpio.output(dc_motor_IN4, False)

def right():
    wheels_init()
    gpio.output(dc_motor_IN1, True)
    gpio.output(dc_motor_IN2, False)
    gpio.output(dc_motor_IN3, False)
    gpio.output(dc_motor_IN4, False)

def left():
    wheels_init()
    gpio.output(dc_motor_IN1, False)
    gpio.output(dc_motor_IN2, False)
    gpio.output(dc_motor_IN3, False)
    gpio.output(dc_motor_IN4, True)

def pivot_right():
    wheels_init()
    gpio.output(dc_motor_IN1, True)
    gpio.output(dc_motor_IN2, False)
    gpio.output(dc_motor_IN3, True)
    gpio.output(dc_motor_IN4, False)

def stop():
    gpio.cleanup()'''
