from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE, gears=[12,20])
rightMotor = Motor(Port.D, gears=[12,20])
driveBase = DriveBase(leftMotor, rightMotor, 49.7, 98.1)

driveBase.settings(120, 200, 100, 150)
driveBase.turn(-360)
# driveBase.straight(1000)
