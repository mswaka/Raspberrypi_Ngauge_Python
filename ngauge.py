#
# This software is released under the MIT License, see LICENSE
#
# Copyright (c) 2020 chimo
#

import os, time
import RPi.GPIO as GPIO

#BCM mode
GPIO.setmode(GPIO.BCM)
# pin9 is GND
GPIO17 = 17  # pin11
GPIO27 = 27  # pin13
DUTY1 = 1
DUTY2 = -1
#OUT
GPIO.setup(GPIO17, GPIO.OUT)
GPIO.setup(GPIO27, GPIO.OUT)

#PWM sets
pwm1 = GPIO.PWM(GPIO17, 100) # frequency 100Hz
pwm2 = GPIO.PWM(GPIO27, 100) # frequency 100Hz
pwm1.start(0)
pwm2.start(0)

# run
for dc in range(0, 21, DUTY1):
    pwm1.ChangeDutyCycle(dc)
    # print(dc)
    time.sleep(1)
time.sleep(10)
for dc in range(20, -1, DUTY2):
    pwm1.ChangeDutyCycle(dc)
    # print(dc)
    time.sleep(1)

# stop
#time.sleep(10)

# opposite
#for dc in range(0, 60, DUTY1):
#    pwm2.ChangeDutyCycle(dc)
#    # print(dc)
#    time.sleep(1)
#time.sleep(5)
#for dc in range(60, -1, DUTY2):
#    pwm2.ChangeDutyCycle(dc)
#    # print(dc)
#    time.sleep(1)

pwm1.stop()
pwm2.stop()
GPIO.cleanup()
# print("end")
