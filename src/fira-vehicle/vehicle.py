import pybricks
from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Direction
from pybricks.robotics import DriveBase
from pybricks.hubs import TechnicHub

print(pybricks.version)

hub = TechnicHub()
sensor = ColorDistanceSensor(Port.A)
leftMotor = Motor(Port.C, Direction.COUNTERCLOCKWISE, gears=[12,20])
rightMotor = Motor(Port.D, gears=[12,20])
driveBase = DriveBase(leftMotor, rightMotor, 49.7, 98.1)

driveBase.settings(100, 150, 70, 100)
turn = 90
peek = 30

battery = None

while True:
    newBattery = hub.battery.voltage()
    if battery != newBattery:
        battery = newBattery
        print("Battery is %smV" % battery)
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
