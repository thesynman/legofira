from pybricks.iodevices import PUPDevice
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.pupdevices import ColorDistanceSensor

import firavehicle.colour as colour
import pybricks

sensor = PUPDevice(Port.A)
cdsensor = ColorDistanceSensor(Port.A)
colour.initColoursForSensor(cdsensor)

lastReading = {}

print('Starting...')
print(pybricks.version)

while True:
    wait(100)
    newReading = cdsensor.distance()
    if newReading != lastReading.get("CDD"):
        print('Mode %s is %s' % ("CDD", newReading))
        lastReading["CDD"] = newReading
    newReading = cdsensor.color()
    if newReading != lastReading.get("CDC"):
        print('Mode %s is %s' % ("CDC", newReading))
        lastReading["CDC"] = newReading
    newReading = cdsensor.hsv()
    if newReading != lastReading.get("HSV"):
        print('Mode %s is %s' % ("HSV", newReading))
        lastReading["HSV"] = newReading
    # for mode in (0,1,6,8,9,10):
    #     # print('Reading mode ' + str(mode))
    #     newReading = sensor.read(mode)
    #     # print('Read ' + str(newReading))
    #     if newReading != lastReading.get(mode):
    #         print('Mode %s is %s' % (mode, newReading))
    #         lastReading[mode] = newReading
