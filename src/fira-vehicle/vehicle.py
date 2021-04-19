from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Stop, Direction
from pybricks.tools import wait
from pybricks.robotics import DriveBase

sensor = ColorDistanceSensor(Port.B)
leftMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightMotor = Motor(Port.C)
driveBase = DriveBase(leftMotor, rightMotor, 49.7, 156)

driveBase.settings(120, 200, 100, 150)
turn = 90
peek = 30

while True:
    driveBase.straight(100)
    if sensor.distance() == 100:
        driveBase.turn(peek)
        if sensor.distance() == 100:
            driveBase.turn(-peek*2)
            if sensor.distance() == 100:
                driveBase.turn(peek)
                peek = -peek
                continue
            else:
                driveBase.turn(peek)
        else:
            driveBase.turn(-peek)
    driveBase.turn(turn)
    if sensor.distance() == 100:
        driveBase.straight(150)
        driveBase.turn(turn)
    else:
        turn = -turn
        driveBase.turn(turn*2)
        if sensor.distance() == 100:
            driveBase.straight(150)
            driveBase.turn(turn)
        else:
            driveBase.stop()
            break
    turn = -turn
    peek = -peek
