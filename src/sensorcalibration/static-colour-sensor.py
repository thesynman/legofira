from pybricks.iodevices import PUPDevice
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.pupdevices import ColorDistanceSensor

sensor = PUPDevice(Port.B)
cdsensor = ColorDistanceSensor(Port.B)

lastReading = {}

print('Starting...')
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
    for mode in (0,1,6,8,9,10):
        # print('Reading mode ' + str(mode))
        newReading = sensor.read(mode)
        # print('Read ' + str(newReading))
        if newReading != lastReading.get(mode):
            print('Mode %s is %s' % (mode, newReading))
            lastReading[mode] = newReading
