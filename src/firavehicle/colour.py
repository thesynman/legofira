from pybricks.parameters import Color


def initColoursForSensor(sensor):
    Color.GREENBALL = Color(h=133, s=96, v=37)
    Color.REDBALL = Color(h=358, s=97, v=55)
    Color.BLUEBALL = Color(h=216, s=97, v=53)
    Color.YELLOWBALL = Color(h=45, s=96, v=68)
    Color.ORANGEBALL = Color(h=11, s=97, v=52)
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
