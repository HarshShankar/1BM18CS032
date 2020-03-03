import serial
import time 

phone = serial.Serial("/dev/ttyAMA0", baudrate=9600, timeout=1.0)
phone.write('AT\r')


phone.write('AT+CPIN=0000\r')


phone.write('AT+CMGF=1\r')


phone.write('AT+CMGS="+919611969907"\r')

