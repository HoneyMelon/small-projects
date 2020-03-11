import pygame
import math


class Tisch:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((650, 600), 0, 32)

    def get_screen(self):
        return self.screen

    def draw_field(self):
        distance = 305 / 4
        self.screen.fill((200, 200, 200))
    
        pygame.event.pump()
    
        # bande
        pygame.draw.rect(self.screen, (80, 63, 38), pygame.Rect(0, 125, 650, 350))
        # loch
        # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(310, 450, 30, 25))
        # field
        pygame.draw.rect(self.screen, (57, 110, 44), pygame.Rect(25, 150, 600, 300))
        # markers
        for i in range(20, 630, int(distance)):
            pygame.draw.circle(self.screen, (255, 255, 255), (i, 140), 2)
            pygame.draw.circle(self.screen, (255, 255, 255), (i, 460), 2)
        for i in range(145, 455, int(distance)):
            pygame.draw.circle(self.screen, (255, 255, 255), (15, i), 2)
            pygame.draw.circle(self.screen, (255, 255, 255), (635, i), 2)
        # lock kreis
        pygame.draw.circle(self.screen, (0, 0, 0), (325, 145), 20)   # oben
        pygame.draw.circle(self.screen, (0, 0, 0), (325, 455), 20)   # unten
        # ecken
        pygame.draw.circle(self.screen, (0, 0, 0), (25, 150), 20)    # links oben
        pygame.draw.circle(self.screen, (0, 0, 0), (625, 150), 20)   # rechts oben
        pygame.draw.circle(self.screen, (0, 0, 0), (25, 450), 20)    # links unten
        pygame.draw.circle(self.screen, (0, 0, 0), (625, 450), 20)   # recht unten
    
    def check_rebound(self, ball, x, y):
        """
        @param x: float
        @param y: float
        @param ball: ball object
        @return:
        """
        absorption = 0.03
        # left wall
        if x - ball.radius <= 25:
            ball.position[0] = 25 + ball.radius
            ball.direction[0] = abs(ball.direction[0])
            if ball.speed > 0:
                ball.speed -= absorption
    
        # right wall
        elif x + ball.radius >= 625:
            ball.position[0] = 625 - ball.radius
            ball.direction[0] = -abs(ball.direction[0])
            if ball.speed > 0:
                ball.speed -= absorption
    
        # upper wall
        elif y - ball.radius <= 150:
            ball.position[1] = 150 + ball.radius
            ball.direction[1] = abs(ball.direction[1])
            if ball.speed > 0:
                ball.speed -= absorption
    
        # lower wall
        elif y + ball.radius >= 450:
            ball.position[1] = 450 - ball.radius
            ball.direction[1] = -abs(ball.direction[1])
            if ball.speed > 0:
                ball.speed -= absorption
        else:
            ball.position[0] = x
            ball.position[1] = y

    def calculate_points_of_arc(self):
        """
        @return: list of tuples of ints
        """
        point_list = []
        middle = (25, 150)
        radius = 15
        x = middle[0]
        y = middle[1] - radius
        for i in range(90):
            x += 1
            y -= 1
            point_list.append((x, y))
        return point_list
    
    def is_in_hole(self, ball):
        lochs = [(25, 150), (625, 150), (25, 450), (625, 450), (325, 145), (325, 455)]
        for loch in lochs:
            x = ball.position[0] - loch[0]
            y = ball.position[1] - loch[1]
            distance = math.sqrt(x**2 + y**2)
            if distance <= 20:
                ball.on_field = False
                ball.position[0] = 20
                ball.position[1] = 110
                ball.speed = 0
                return True
        return False

    def _start_position_of_balls(self, number_of_balls, x_start, y_start, distance, position_list):
        if number_of_balls <= 1:
            position_list.append([x_start, y_start])
            return position_list
        position_list.append([x_start, y_start])
        new_y = y_start
        for i in range(number_of_balls - 1):
            position_list.append([x_start, new_y + distance])
            new_y += distance
        return self._start_position_of_balls(number_of_balls - 1, x_start + distance,
                                             y_start + distance / 2, distance, position_list)

    def start_position_of_balls(self, number_of_balls, x_start, y_start, distance):
        return self._start_position_of_balls(number_of_balls, x_start, y_start, distance, [])


