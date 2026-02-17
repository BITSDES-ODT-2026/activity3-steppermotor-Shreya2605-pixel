# Using a stepper motor and interfacing it with ESP32, clockwise and anti clockwise
from machine import Pin
import time
V = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
U = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]
in1 = Pin(5, Pin.OUT)
in2 = Pin(14, Pin.OUT)
in3 = Pin(15, Pin.OUT)
in4 = Pin(19, Pin.OUT)
while True:
    for k in range(500):
        for i in V:
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            time.sleep_ms(5)
     for x in range(500):
        for i in U:
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            time.sleep_ms(5)
