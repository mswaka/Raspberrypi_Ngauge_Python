#
# This software is released under the MIT License, see LICENSE
#
# Copyright (c) 2020 chimo
#

import RPi.GPIO as GPIO
import time
import os

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if adcnum > 1 or adcnum < 0:
        return -1
    GPIO.output(cspin, GPIO.HIGH)       #CSON
    GPIO.output(clockpin, GPIO.LOW)     #SCSKON
    GPIO.output(cspin, GPIO.LOW)        #CSOFF

    #commandout = 0b01101000
    commandout = adcnum   #CH
    commandout |= 0x0d    #SGL/DEF=1MSB
    commandout <<= 3      #LSB8bit
    for i in range(4):
        # LSB8bit3bit
        if commandout & 0x80:
            GPIO.output(mosipin, GPIO.HIGH)
        else:
            GPIO.output(mosipin, GPIO.LOW)
        commandout <<= 1
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
    adcout = 0
    #11bit null
    for i in range(11):
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
        adcout <<= 1
        if i>0 and GPIO.input(misopin)==GPIO.HIGH:
            adcout |= 0x1
    GPIO.output(cspin, GPIO.HIGH)
    return adcout

GPIO.setmode(GPIO.BCM)

# pin name
SPICLK = 11
SPIMOSI = 10
SPIMISO = 9
SPICS = 8
GPIO17 = 17  # pin11
GPIO27 = 27  # pin13
#OUT
GPIO.setup(GPIO17, GPIO.OUT)
GPIO.setup(GPIO27, GPIO.OUT)


# SPI
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICS, GPIO.OUT)

#PWM sets
pwm1 = GPIO.PWM(GPIO17, 60) # frequency 60Hz
pwm2 = GPIO.PWM(GPIO27, 60) # frequency 60Hz
pwm1.start(0)
pwm2.start(0)

vol_old = 0

try:
    while True:
        inputVal0 = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
        vol = "{0}%".format(int(inputVal0*100/1023)) #1023
        print(vol)
        if int(vol[:-1]) != vol_old:
            vol_old = int(vol[:-1])
            pwm1.ChangeDutyCycle(vol_old)
        time.sleep(0.2)

except KeyboardInterrupt:
    pass

pwm1.stop()
pwm2.stop()
GPIO.cleanup()
