from pybricks.pupdevices import Motor, ColorDistanceSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait


class Buffer:
    def __init__(self, size):
        self.size = size
        self.store = []

    def push(self, item):
        self.store.append(item)
        if len(self.store) > self.size:
            self.store.pop(0)


# The number of degrees the motor must rotate to move the test rig by 1m
DEGREES_PER_METRE = 4822

TEST_DISTANCE_MM = 300
TEST_INCREMENT_MM = 5
DEGREES_PER_INCREMENT = round(DEGREES_PER_METRE * TEST_INCREMENT_MM / 1000)

motor = Motor(Port.D)
sensor = ColorDistanceSensor(Port.B)

results = {}
distanceFromTarget = 0
recent = Buffer(5)

while distanceFromTarget < TEST_DISTANCE_MM and sum(recent.store) < 500:
    wait(500)
    newReading = sensor.distance()
    results[distanceFromTarget] = newReading
    recent.push(newReading)
    motor.run_angle(100, -DEGREES_PER_INCREMENT, Stop.HOLD)
    distanceFromTarget += TEST_INCREMENT_MM
motor.run_angle(150, 0, Stop.COAST)
for key in sorted(results):
    print("%s: %s" % (key, results[key]))
