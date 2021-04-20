from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

sensor = ColorDistanceSensor(Port.B)
leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.C)
driveBase = DriveBase(leftMotor, rightMotor, 49.7, 156)

driveBase.settings(120, 200, 100, 150)
# driveBase.turn(-360)
driveBase.straight(1000)
