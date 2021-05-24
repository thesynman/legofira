import pybricks
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import TechnicHub
from pybricks.tools import wait

import motion
import colour

print(pybricks.version)

hub = TechnicHub()
sensor = ColorDistanceSensor(Port.A)
colour.initColoursForSensor(sensor)
leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE, gears=[12,20])
rightMotor = Motor(Port.D, gears=[12,20])
driveBase = DriveBase(leftMotor, rightMotor, 49.7, 98.1)

motion = motion.Motion(sensor, driveBase)

try:
    print("Battery is %smV" % hub.battery.voltage())
    motion.seek()
    print("Found!")
    found = motion.identify()
    print("Identified: " + str(found))
    motion.takePosition(found)
    print("Took position")
    motion.capture()
    print("done!")
except Exception as ex:
    print(ex)
    wait(1000)
    raise ex

