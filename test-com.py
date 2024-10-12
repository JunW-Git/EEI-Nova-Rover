# This code is just used to test communicating with the arduino through serial port
# Note the arduino will always respond one input late

import serial
import time

com = input("COM: ")
baud = 9600
arduino = serial.Serial(port=com, baudrate=9600, timeout=1)

output = ""
while True:
    msg = "\n" + input("Input: ")
    arduino.write(bytes(msg, encoding="utf-8"))
    time.sleep(0.05)
    output = arduino.readline().decode("utf-8").rstrip("\n")
    print(f"OUTPUT: {output}")
