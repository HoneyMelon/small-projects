import random
import stddraw
import color
import keyboard
import math
import time

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
    speedx = 0.05
    speedy = 0.05
    return randx, randy, speedx, speedy


def bouncing_game(x, y, speedx, speedy):
    starttime = time.time()
    timediff = 0
    points = []
    position = [x, y]
    foodPosition = [random.randint(2, 9), random.randint(2, 9)]
    foodCounter = 0
    speed = [speedx, speedy]
    slowmo = False
    while timediff < 60:
        stddraw.clear(color.DARK_GRAY)
        position[0] += speed[0]
        position[1] += speed[1]
        points.append([position[0], position[1]])
        stddraw.setPenColor(color.CYAN)

        timediff = time.time() - starttime
        timediffSeconds = 60 - math.floor(timediff)
        stddraw.text(9.5, 9.5, f'{foodCounter}')
        stddraw.text(0.5, 9.5, f'{timediffSeconds}')

        stddraw.filledCircle(foodPosition[0], foodPosition[1], 0.1)
        if len(points) > foodCounter * 5 + 10:
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

        squaredDistanceToFood = (position[0] - foodPosition[0]) ** 2 + (position[1] - foodPosition[1]) ** 2
        if squaredDistanceToFood < 0.1:
            foodPosition = [random.randint(2, 9), random.randint(2, 9)]
            foodCounter += 1



        if keyboard.is_pressed('q'):  # if key 'q' is pressed
            slowmo = True
        else:
            slowmo = False

        # GRAVIIITYYYY
        if keyboard.is_pressed('w'):
            speed[1] += 0.001
        else:
            speed[1] -= 0.001
    print("Game Over! Dein Highscore:", foodCounter)

balls = []

init_stddraw()
x, y, speedx, speedy = init_values()
bouncing_game(x, y, speedx, speedy)



