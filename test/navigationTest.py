from firavehicle import navigation


def testThatPositiveTurnIsAppliedCorrectly():
    position = navigation.Coordinate(0, 0, 10)

    position.turn(41)

    assert position.heading == 51


def testThatBigPositiveTurnIsAppliedCorrectly():
    position = navigation.Coordinate(0, 0, 20)

    position.turn(345)

    assert position.heading == 5


def testThatVeryBigPositiveTurnIsAppliedCorrectly():
    position = navigation.Coordinate(0, 0, 20)

    position.turn(705)

    assert position.heading == 5


def testThatNegativeTurnIsAppliedCorrectly():
    position = navigation.Coordinate(0, 0, 60)

    position.turn(-20)

    assert position.heading == 40


def testThatNegativeTurnIsAppliedCorrectlyWhenHeadingSwingsToLeft():
    position = navigation.Coordinate(0, 0, 60)

    position.turn(-70)

    assert position.heading == 350


def testThatBigNegativeTurnIsAppliedCorrectly():
    position = navigation.Coordinate(0, 0, 60)

    position.turn(-400)

    assert position.heading == 20


def testThatVeryBigNegativeTurnIsAppliedCorrectly():
    position = navigation.Coordinate(0, 0, 60)

    position.turn(-760)

    assert position.heading == 20


def testThatMoveUpIsCalculatedCorrectly():
    position = navigation.Coordinate(0, 0, 0)

    position.ahead(50)

    assert position.x == 0
    assert position.y == 50


def testThatMoveDownIsCalculatedCorrectly():
    position = navigation.Coordinate(0, 0, 180)

    position.ahead(50)

    assert position.x == 0
    assert position.y == -50


def testThatMoveRightIsCalculatedCorrectly():
    position = navigation.Coordinate(0, 0, 90)

    position.ahead(50)

    assert position.x == 50
    assert position.y == 0


def testThatMoveLeftIsCalculatedCorrectly():
    position = navigation.Coordinate(0, 0, 270)

    position.ahead(50)

    assert position.x == -50
    assert position.y == 0


def testRouteFromEast():
    origin = navigation.Coordinate(50, 0, 30)
    destination = navigation.Coordinate(0, 0, 0)

    result = navigation.Terrain().plotRouteFromTo(origin, destination)

    assert len(result) == 3
    print(str(result[0]))
    assert result[0] == navigation.RouteStep(navigation.RouteStep.TURN, -120)
    assert result[1] == navigation.RouteStep(navigation.RouteStep.DRIVE, 50)
    assert result[2] == navigation.RouteStep(navigation.RouteStep.TURN, -270)


def testRouteFromWest():
    origin = navigation.Coordinate(-50, 0, 30)
    destination = navigation.Coordinate(0, 0, 0)

    result = navigation.Terrain().plotRouteFromTo(origin, destination)

    assert len(result) == 3
    print(str(result[0]))
    assert result[0] == navigation.RouteStep(navigation.RouteStep.TURN, -300)
    assert result[1] == navigation.RouteStep(navigation.RouteStep.DRIVE, 50)
    assert result[2] == navigation.RouteStep(navigation.RouteStep.TURN, -90)


def testRouteFromNorth():
    origin = navigation.Coordinate(0, 50, 30)
    destination = navigation.Coordinate(0, 0, 0)

    result = navigation.Terrain().plotRouteFromTo(origin, destination)

    assert len(result) == 3
    print(str(result[0]))
    assert result[0] == navigation.RouteStep(navigation.RouteStep.TURN, -210)
    assert result[1] == navigation.RouteStep(navigation.RouteStep.DRIVE, 50)
    assert result[2] == navigation.RouteStep(navigation.RouteStep.TURN, -180)


def testRouteFromSouth():
    origin = navigation.Coordinate(0, -50, 30)
    destination = navigation.Coordinate(0, 0, 0)

    result = navigation.Terrain().plotRouteFromTo(origin, destination)

    assert len(result) == 2
    assert result[0] == navigation.RouteStep(navigation.RouteStep.TURN, -30)
    assert result[1] == navigation.RouteStep(navigation.RouteStep.DRIVE, 50)


def testRouteNoDistance():
    origin = navigation.Coordinate(0, 0, 30)
    destination = navigation.Coordinate(0, 0, 0)

    result = navigation.Terrain().plotRouteFromTo(origin, destination)

    assert len(result) == 1
    assert result[0] == navigation.RouteStep(navigation.RouteStep.TURN, -30)


def testRouteNothingToDo():
    origin = navigation.Coordinate(0, 0, 30)
    destination = navigation.Coordinate(0, 0, 30)

    result = navigation.Terrain().plotRouteFromTo(origin, destination)

    assert len(result) == 0


def testRouteFromNorthWest():
    origin = navigation.Coordinate(-80, 60, 30)
    destination = navigation.Coordinate(-40, 30, 20)

    result = navigation.Terrain().plotRouteFromTo(origin, destination)

    assert len(result) == 3
    print(str(result[0]))
    assert result[0] == navigation.RouteStep(navigation.RouteStep.TURN, -263)
    assert result[1] == navigation.RouteStep(navigation.RouteStep.DRIVE, 50)
    assert result[2] == navigation.RouteStep(navigation.RouteStep.TURN, -107)


def testRouteFromNorthEast():
    origin = navigation.Coordinate(80, 60, 30)
    destination = navigation.Coordinate(40, 30, 20)

    result = navigation.Terrain().plotRouteFromTo(origin, destination)

    assert len(result) == 3
    print(str(result[0]))
    assert result[0] == navigation.RouteStep(navigation.RouteStep.TURN, -157)
    assert result[1] == navigation.RouteStep(navigation.RouteStep.DRIVE, 50)
    assert result[2] == navigation.RouteStep(navigation.RouteStep.TURN, -213)


def testRouteFromSouthEast():
    origin = navigation.Coordinate(70, -10, 30)
    destination = navigation.Coordinate(40, 30, 20)

    result = navigation.Terrain().plotRouteFromTo(origin, destination)

    assert len(result) == 3
    print(str(result[0]))
    assert result[0] == navigation.RouteStep(navigation.RouteStep.TURN, -67)
    assert result[1] == navigation.RouteStep(navigation.RouteStep.DRIVE, 50)
    assert result[2] == navigation.RouteStep(navigation.RouteStep.TURN, -303)


def testRouteFromSouthWest():
    origin = navigation.Coordinate(-10, -10, 30)
    destination = navigation.Coordinate(30, 20, 20)

    result = navigation.Terrain().plotRouteFromTo(origin, destination)

    assert len(result) == 3
    print(str(result[0]))
    assert result[0] == navigation.RouteStep(navigation.RouteStep.TURN, -337)
    assert result[1] == navigation.RouteStep(navigation.RouteStep.DRIVE, 50)
    assert result[2] == navigation.RouteStep(navigation.RouteStep.TURN, -33)
