from pybricks.hubs import TechnicHub
from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

sensor = ColorDistanceSensor(Port.B)
led = TechnicHub().light

lastReading = None

while True:
    wait(100)
    newReading = sensor.distance()
    if newReading != lastReading:
        print(newReading)
        lastReading = newReading
    if newReading == 100:
        led.off()
    else:
        led.on(Color(newReading * 3))
