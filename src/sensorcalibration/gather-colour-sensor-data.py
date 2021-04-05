from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait

# The number of degrees the motor must rotate to move the test rig by 1m
DEGREES_PER_METRE = 4822

TEST_DISTANCE_MM = 100
TEST_INCREMENT_MM = 5
DEGREES_PER_INCREMENT = round(DEGREES_PER_METRE * TEST_INCREMENT_MM / 1000)

motor = Motor(Port.D)
sensor = ColorDistanceSensor(Port.B)

results = {}
distanceFromTarget = 0

while distanceFromTarget <= TEST_DISTANCE_MM:
    wait(500)
    newReading = sensor.hsv()
    results[distanceFromTarget] = newReading
    motor.run_angle(100, -DEGREES_PER_INCREMENT, Stop.HOLD)
    distanceFromTarget += TEST_INCREMENT_MM
motor.run_angle(150, 0, Stop.COAST)
sortedResultKeys = sorted(results)
for key in sortedResultKeys:
    print("%s" % (results[key]))
print("Last reading was at %smm" % (sortedResultKeys[-1]))
