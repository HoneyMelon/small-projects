import math
import pygame
from ball import Ball


class Cue:
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def calculate_new_cue_position(self, angle, ball_x, ball_y):
        sin = math.sin(angle)
        cos = math.cos(angle)

        ball_x -= self.x
        ball_y -= self.y

        xnew = ball_x * cos - ball_y * sin
        ynew = ball_x * sin + ball_y * cos

        ball_x = xnew + self.x
        ball_y = ynew + self.y
        return ball_x, ball_y


def draw_cue(screen, ball, end_x, end_y):
    end_x, end_y = ball.cue_position(end_x, end_y)
    pygame.draw.line(screen, (0, 0, 0), [ball.position[0], ball.position[1]], [end_x, end_y], 10)

