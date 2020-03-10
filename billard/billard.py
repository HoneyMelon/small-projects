from tisch import Tisch
from ball import Ball
import pygame

pygame.font.init()
pygame.init()
done = False
pygame.event.pump()
font = pygame.font.SysFont('arialblack', 11)

tisch = Tisch()
white_ball = Ball(10, [5, 1], [120, 360], 0)
balll = Ball(10, [5, 1], [120, 360], 2, 1, (200, 200, 0))
ball2 = Ball(10, [5, 1], [50, 360], 2, 2, (100, 100, 255))
ball3 = Ball(10, [2, 1], [50, 360], 2, 14, (255, 100, 100), False)
balls = [white_ball, balll, ball2, ball3]

while not done:
    tisch.draw_field()
    for ball in balls:
        ball.next_position(tisch)
        ball.draw(tisch, font)
        tisch.is_in_hole(ball)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            white_ball.move_to_cursor(x, y)
