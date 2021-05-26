import pybricks
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import TechnicHub
from pybricks.tools import wait
from pybricks.parameters import Color as PBColor

import motion
import colour
import navigation

def _waitForController():
    distance = 100
    while distance >= 30:
        wait(100)
        new_distance = controller.distance()
        if new_distance != distance:
            distance = new_distance
#            print("Distance is " + str(distance))
    return

def _lightOff():
    hub.light.off()

def _lightBlink(colour):
    hub.light.blink(colour, [200, 200])

print(pybricks.version)

hub = TechnicHub()
sensor = ColorDistanceSensor(Port.A)
colour.initColoursForSensor(sensor)
controller = ColorDistanceSensor(Port.B)
leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE, gears=[12,20])
rightMotor = Motor(Port.D, gears=[12,20])
driveBase = DriveBase(leftMotor, rightMotor, 49.7, 98.1)

motion = motion.Motion(sensor, driveBase)
terrain = navigation.Terrain()

try:
    print("Battery is %smV" % hub.battery.voltage())
    _lightBlink(PBColor.WHITE)
    _waitForController()
    _lightOff()
    while True:
        try:
            motion.seek()
            print("Found!")
            found = motion.identify()
            print("Identified: " + str(found))
            _lightBlink(found)
            motion.takePosition(found)
            print("Took position")
            motion.capture()
            motion.driveTo(navigation.Coordinate(0, 0, 0), terrain)
        except ValueError as ve:
            print(ve)
        print("waiting...")
        _waitForController()
except Exception as ex:
    print(ex)
    wait(1000)
    raise ex


