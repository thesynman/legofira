import math


class Coordinate:
    """Represents a point on a 2-D space, plus a current heading.

    Relative to a heading of 0:
    positive x is a displacement to the right
    negative x is a displacement to the left
    positive y is a displacement forward
    negative y is a displacement backwards
    """

    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading

    def ahead(self, distance):
        self.x = int(round(self.x + (distance * math.sin(math.radians(self.heading)))))
        self.y = int(round(self.y + (distance * math.cos(math.radians(self.heading)))))

    def turn(self, angle):
        """Positive angle indicates clockwise turn"""
        self.heading = (self.heading + angle) % 360
        if self.heading < 0:
            self.heading = 360 - self.heading

    def copy(self):
        return Coordinate(self.x, self.y, self.heading)

    def __str__(self):
        return "Coordinate: " + str(self.x) + "," + str(self.y) + "," + str(self.heading)


class Terrain:

    def plotRouteFromTo(self, origin, destination):
        x_delta = destination.x - origin.x
        y_delta = destination.y - origin.y
        if y_delta == 0 and x_delta == 0:
            required_heading = origin.heading
            result = []
        else:
            if y_delta == 0:
                required_heading = 270 if x_delta < 0 else 90
            elif x_delta == 0:
                required_heading = 180 if y_delta < 0 else 0
            else:
                quadrant = 180 if y_delta < 0 else 0 if x_delta >= 0 else 360
                required_heading = quadrant + int(round(math.degrees(math.atan(x_delta / y_delta))))
            turn = -((360 - required_heading + origin.heading) % 360)
            distance = int(round(math.sqrt(x_delta * x_delta + y_delta * y_delta)))
            # TODO fix constant refs
            result = [RouteStep(1, turn),
                      RouteStep(0, distance)]
        if required_heading != destination.heading:
            final_turn = -((360 - destination.heading + required_heading) % 360)
            result.append(RouteStep(1, final_turn))
        return result


class RouteStep:
    DRIVE = 0
    TURN = 1

    def __init__(self, the_type, amount):
        self.type = the_type
        self.amount = amount

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.type == other.type and self.amount == other.amount
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return type(self).__name__ + ": " + str(self.type) + " " + str(self.amount)
