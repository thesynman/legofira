import coordinate
import colour

from pybricks.parameters import Color


class Motion:
    def __init__(self, cd_sensor, drive_base):
        self.heading = 0
        self.position = coordinate.Coordinate(0, 0)
        self.peek_angle = 30
        self.cd_sensor = cd_sensor
        self.drive_base = drive_base
        self.normalSpeed()

    def normalSpeed(self):
        print("setting normal speed")
        self.drive_base.stop()
        self.drive_base.settings(100, 150, 70, 100)

    def slowSpeed(self):
        self.drive_base.stop()
        self.drive_base.settings(20, 20, 20, 20)

    def seek(self):
        while True:
            if self.cd_sensor.distance() != 100:
                break
            self._drive(100)
            if self.cd_sensor.distance() == 100:
                # nothing directly ahead - look to the side
                self._turn(self.peek_angle)
                if self.cd_sensor.distance() == 100:
                    # nothing there - look the other side
                    self._turn(-self.peek_angle * 2)
                    if self.cd_sensor.distance() == 100:
                        # still nothing - so straighten up and go again
                        self._turn(self.peek_angle)
                        self.peek_angle = -self.peek_angle
                        continue
            self.peek_angle = -self.peek_angle
            break
        return self.cd_sensor.distance()

    def identify(self):
        if self.cd_sensor.distance() == 100:
            raise ValueError('Asked to identify, but nothing in range')
        # advance watching the delta on the sensor
        # stop and sniff the color when the sensor value gets to 10
        distance = self.cd_sensor.distance()
        self.slowSpeed()
        while self._senseColour() == Color.NONE:
            self._drive(10)
            new_distance = self.cd_sensor.distance()
            if new_distance > distance:
                self._realign(new_distance)
                new_distance = self.cd_sensor.distance()
            elif new_distance <= 10:
                raise ValueError("Close to target, but still can't identify it")
            distance = new_distance
        self.normalSpeed()
        return self._senseColour()

    def takePosition(self, colour_sensed):
        if colour_sensed == Color.NONE:
            raise ValueError("Asked to take position but no color is sensed")
        target_distance = colour.getColourDistanceMap()[colour_sensed]
        self.slowSpeed()
        current_distance = self.cd_sensor.distance()
        delta = 2
        while current_distance <= target_distance[0]:
            print(current_distance)
            self._drive(-delta)
            current_distance = self.cd_sensor.distance()
        while current_distance != target_distance[0]:
            print(current_distance)
            self._drive(delta)
            current_distance = self.cd_sensor.distance()
        self._drive(target_distance[1])
        self.normalSpeed()

    def capture(self):
        self.slowSpeed()
        self._drive(-70)
        self._turn(-180)

    def _realign(self, current_distance):
        # angle = 10
        # while (new_distance := self.cd_sensor.distance()) > current_distance:
        #     self.drive_base.turn(angle)
        #     self.heading += angle
        # pass
        raise ValueError('realign not expected')

    def _drive(self, delta):
        self.drive_base.straight(delta)
        self.position.ahead(self.heading, delta)

    def _turn(self, angle):
        self.drive_base.turn(angle)
        self.heading += angle

    def _senseColour(self):
        print(self.cd_sensor.hsv())
        return self.cd_sensor.color()
