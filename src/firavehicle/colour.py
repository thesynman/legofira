from pybricks.parameters import Color


def initColoursForSensor(sensor):
    Color.GREENBALL = Color(h=133, s=96, v=37)
    Color.REDBALL = Color(h=3, s=98, v=22)
    Color.BLUEBALL = Color(h=216, s=97, v=53)
    Color.YELLOWBALL = Color(h=48, s=98, v=17)
    Color.ORANGEBALL = Color(h=19, s=96, v=32)
    Color.PURPLEBALL = Color(h=286, s=77, v=29)
    sensor.detectable_colors((
        Color.WHITE,
        Color.NONE,
        Color.GREENBALL,
        Color.REDBALL,
        Color.BLUEBALL,
        Color.YELLOWBALL,
        Color.ORANGEBALL,
        Color.PURPLEBALL
    ))


def getColourDistanceMap():
    return {
        Color.GREENBALL : (20, 0),
        Color.REDBALL : (20, 2),
        Color.BLUEBALL : (20, 4),
        Color.YELLOWBALL : (20, 18),
        Color.ORANGEBALL : (20, 0),
        Color.PURPLEBALL : (20, 0),
}