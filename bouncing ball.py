import random
import stddraw
import color
import keyboard
import math

maxRadius = 0.3
minRadius = 0.1
width = 10
height = 10


def init_stddraw():
    stddraw.setPenRadius(0.02)
    stddraw.setXscale(0, width)
    stddraw.setYscale(0, height)
    stddraw.clear(color.DARK_GRAY)


def init_values():
    randx = random.randint(2, 9)
    randy = random.randint(2, 9)
    speedx = random.randint(5, 15) / 300
    speedy = random.randint(5, 15) / 300
    return randx, randy, speedx, speedy


def bouncing(x, y, speedx, speedy):
    points = []
    position = [x, y]
    speed = [speedx, speedy]
    print(position, speed)
    slowmo = False
    while True:
        stddraw.clear(color.DARK_GRAY)
        position[0] += speed[0]
        position[1] += speed[1]
        points.append([position[0], position[1]])
        if len(points) > 50:
            points.pop(0)
        for i in range(len(points)):
            rainbowrray = [color.RED, color.ORANGE, color.YELLOW, color.GREEN, color.BLUE, color.PURPLE]
            colorPosition = math.floor((i / len(points)) * 6)
            stddraw.setPenColor(rainbowrray[colorPosition])
            circleRadius = maxRadius * (i / len(points))
            circleRadius = circleRadius if circleRadius > minRadius else minRadius
            stddraw.filledCircle(points[i][0], points[i][1], circleRadius)
        stddraw.show(16 if slowmo else 5)
        # Left Wall
        if position[0] - maxRadius <= 0:
            position[0] = 0 + maxRadius
            speed[0] = abs(speed[0])
        # Right Wall
        if position[0] + maxRadius >= width:
            position[0] = width - maxRadius
            speed[0] = -abs(speed[0])
        # Upper Wall
        if position[1] + maxRadius >= height:
            position[1] = height - maxRadius
            speed[1] = -abs(speed[1])
        # Bottom Wall
        if position[1] - maxRadius <= 0:
            position[1] = 0 + maxRadius
            speed[1] = abs(speed[1] * 0.9)

        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            slowmo = True
        else:
            slowmo = False

        # GRAVIIITYYYY
        if keyboard.is_pressed('w'):
            speed[1] += 0.001
        else:
            speed[1] -= 0.001


balls = []

init_stddraw()
x, y, speedx, speedy = init_values()
bouncing(x, y, speedx, speedy)



