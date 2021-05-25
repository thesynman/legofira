from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.pupdevices import ColorDistanceSensor

cdsensor = ColorDistanceSensor(Port.B)

lastReading = {}

print('Starting...')
cdsensor.light.off()
wait(5000)
while True:
    wait(100)
    newReading = cdsensor.ambient()
    if newReading != lastReading.get("AMB"):
        print('AMB is %s' % newReading)
        lastReading["AMB"] = newReading
