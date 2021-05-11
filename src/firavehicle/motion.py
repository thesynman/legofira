import coordinate


class Motion:
    def __init__(self, cd_sensor, drive_base):
        self.heading = 0
        self.position = coordinate.Coordinate(0, 0)
        self.peek_angle = 30
        self.cd_sensor = cd_sensor
        self.drive_base = drive_base
        self.normalSpeed()

    def normalSpeed(self):
        self.drive_base.settings(100, 150, 70, 100)

    def slowSpeed(self):
        self.drive_base.settings(20, 20, 20, 20)

    def seek(self):
        while True:
            if self.cd_sensor.distance() != 100:
                break
            self.drive_base.straight(100)
            self.position.ahead(self.heading, 100)
            if self.cd_sensor.distance() == 100:
                # nothing directly ahead - look to the side
                self.drive_base.turn(self.peek_angle)
                self.heading += self.peek_angle
                if self.cd_sensor.distance() == 100:
                    # nothing there - look the other side
                    self.drive_base.turn(-self.peek_angle * 2)
                    self.heading -= self.peek_angle * 2
                    if self.cd_sensor.distance() == 100:
                        # still nothing - so straighten up and go again
                        self.drive_base.turn(self.peek_angle)
                        self.heading += self.peek_angle
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
        while True:
            self.drive_base.straight(10)
            self.position.ahead(self.heading, 10)
            new_distance = self.cd_sensor.distance()
            if new_distance > distance:
                self._realign(new_distance)
                new_distance = self.cd_sensor.distance()
            elif new_distance == 10:
                return self._senseColour()
            distance = new_distance

    def _realign(self, current_distance):
        # angle = 10
        # while (new_distance := self.cd_sensor.distance()) > current_distance:
        #     self.drive_base.turn(angle)
        #     self.heading += angle
        # pass
        raise ValueError('realign not expected')

    def _senseColour(self):
        pass
