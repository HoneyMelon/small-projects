import tisch
from ball import Ball
import pygame


def move_to_cursor(ball):
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        new_x = x - ball.position[0]
        new_y = y - ball.position[1]
        ball.direction = [new_x, new_y]
        if new_x > 0:
            ball.direction[0] = 1
        elif new_x < 0:
            ball.direction[0] = -1
        elif new_y > 0:
            ball.direction[1] = 1
        elif new_y < 0:
            ball.direction = -1


pygame.font.init()
pygame.init()
done = False
pygame.event.pump()
font = pygame.font.SysFont('arialblack', 20)
screen = tisch.draw_field()
test_ball = Ball(10, [5, 1], [120, 360], 0.5, 1)
test_ball.draw(screen, 10)
while not done:
    test_ball.next_position()
    test_ball.draw(screen, 10)
    test_ball.add_number(screen, font)
    tisch.is_in_hole(test_ball)
    #print(test_ball.on_field)
    #move_to_cursor(test_ball)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            new_x = x - test_ball.position[0]
            new_y = y - test_ball.position[1]
            if new_x > 0:
                test_ball.direction[0] = 1
            elif new_x < 0:
                test_ball.direction[0] = -1
            elif new_y > 0:
                test_ball.direction[1] = 1
            elif new_y < 0:
                test_ball.direction[1] = -1
