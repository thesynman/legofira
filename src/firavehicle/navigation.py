class Coordinate:
    def __init__(self, x, y, heading):
        self.x = x
        self.y = y
        self.heading = heading

    def ahead(self, distance):
        pass

    def turn(self, angle):
        pass


class Terrain:
    def plotRouteFromTo(self, position, destination):
        return []
