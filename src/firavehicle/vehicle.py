import pybricks
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import TechnicHub

import motion

print(pybricks.version)

hub = TechnicHub()
sensor = ColorDistanceSensor(Port.A)
leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE, gears=[12,20])
rightMotor = Motor(Port.D, gears=[12,20])
driveBase = DriveBase(leftMotor, rightMotor, 49.7, 98.1)

battery = None

motion = motion.Motion(sensor, driveBase)

while True:
    newBattery = hub.battery.voltage()
    if battery != newBattery:
        battery = newBattery
        print("Battery is %smV" % battery)
    motion.seek()
    motion.identify()
