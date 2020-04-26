import pygame


class Cue:
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width


def draw_cue(screen, ball, end_x, end_y):
    end_x, end_y = ball.cue_position(end_x, end_y)
    pygame.draw.line(screen, (0, 0, 0), [ball.position[0], ball.position[1]], [end_x, end_y], 10)

