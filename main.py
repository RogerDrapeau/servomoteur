Angle = 0
servos.P0.set_range(10, 170)

def on_forever():
    global Angle
    for index in range(17):
        Angle = index * 10 + 10
        servos.P0.set_angle(Angle)
        basic.pause(200)
basic.forever(on_forever)
