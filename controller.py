#
# This software is released under the MIT License, see LICENSE
#
# Copyright (c) 2020 chimo
#

import RPi.GPIO as GPIO
import time
import os
import threading
import Queue as queue

# pin name
SPICLK = 11
SPIMOSI = 10
SPIMISO = 9
SPICS = 8
GPIO17 = 17  # pin11
GPIO27 = 27  # pin13
vol_old = 0

def pwm(q,event):
    print('pwm()')
    global pwm1

    try:
        while True:
            event.wait()
            dc = q.get()
            pwm1.ChangeDutyCycle(dc)
            print('ChangeDutyCycle',dc)

    except KeyboardInterrupt:
        pass

def volume(q,event):
    print('volume()')
    # pin name
    global SPICLK
    global SPIMOSI
    global SPIMISO
    global SPICS
    global vol_old

    try:
        while True:
            inputVal0 = readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS)
            vol = "{0}".format(int(inputVal0*100/1023)) #1023
            if vol_old != vol:
                print('Yes',vol,vol_old)
                vol_old = vol
                q.put(vol)
                event.set()
            else:
                print('No',vol)
            time.sleep(0.2)

    except KeyboardInterrupt:
        pass

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    print('readadc() start')
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
    print('readadc() end')
    return adcout

def main():
    #initialize
    GPIO.setmode(GPIO.BCM)

    # pin name
    global SPICLK
    global SPIMOSI
    global SPIMISO
    global SPICS
    global GPIO17  # pin11
    global GPIO27  # pin13

    global pwm1
    global pwm2

    # SPI
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICS, GPIO.OUT)

    #pwm
    GPIO.setup(GPIO17, GPIO.OUT)
    GPIO.setup(GPIO27, GPIO.OUT)
    pwm1 = GPIO.PWM(GPIO17, 100) # frequency 100Hz
    pwm2 = GPIO.PWM(GPIO27, 100) # frequency 100Hz
    pwm1.start(0)
    pwm2.start(0)
    print('main() initialize done')

    try:
        q = queue.Queue()
        event = threading.Event()
        t1 = threading.Thread(target=volume, args=(q,event))
        t2 = threading.Thread(target=pwm, args=(q,event))
        t1.start()
        t2.start()
        while True:
            time.sleep(0.1)

    except KeyboardInterrupt:
        pass

    pwm1.stop()
    pwm2.stop()

    GPIO.cleanup()

if __name__ == '__main__':
    main()
