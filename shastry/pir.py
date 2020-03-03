import RPi.GPIO as GPIO
import using
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
print "calibrating sensor"
time.sleep(5)

while True:
	i=GPIO.input(11)
	if i==0:                 #When output from motion sensor is LOW
		print "Nobody present",i
		time.sleep(1)
	elif i==1:               #When output from motion sensor is HIGH
		print "Face detected",i
		time.sleep(10)
		execfile('using.py')
		time.sleep(1)