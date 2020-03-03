#!/usr/bin/env python

import time
from RPi import GPIO



GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, GPIO.LOW)

time.sleep(4)

GPIO.output(17, GPIO.HIGH)


GPIO.cleanup()

