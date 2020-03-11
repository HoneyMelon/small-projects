from tisch import Tisch
from ball import Ball
import pygame

pygame.font.init()
pygame.init()
done = False
pygame.event.pump()
font = pygame.font.SysFont('arialblack', 11)
YELLOW = (254, 211, 70)
BLUE = (89, 157, 222)
RED = (221, 88, 89)
PURPLE = (180, 110, 199)
ORANGE = (253, 157, 83)
GREEN = (157, 192, 124)
BROWN = (164, 84, 88)
BLACK = (59, 59, 59)



tisch = Tisch()

position_list = tisch.start_position_of_balls(5, 150, 260, 21)
print(position_list)

balll = Ball(10, [5, 1], position_list[0], 0, 1, YELLOW)
ball2 = Ball(10, [5, 1], position_list[1], 0, 2, BLUE)
ball3 = Ball(10, [2, 1], position_list[2], 0, 3, RED)
ball4 = Ball(10, [5, 1], position_list[3], 0, 4, PURPLE)
ball5 = Ball(10, [5, 1], position_list[4], 0, 5, ORANGE)
ball6 = Ball(10, [5, 1], position_list[5], 0, 6, GREEN)
ball7 = Ball(10, [5, 1], position_list[6], 0, 7, BROWN)
ball8 = Ball(10, [5, 1], position_list[10], 0, 8, BLACK)
ball9 = Ball(10, [5, 1], position_list[8], 0, 9, YELLOW, False)
ball10 = Ball(10, [5, 1], position_list[9], 0, 10, BLUE, False)
ball11 = Ball(10, [5, 1], position_list[7], 0, 11, RED, False)
ball12 = Ball(10, [5, 1], position_list[11], 0, 12, PURPLE, False)
ball13 = Ball(10, [5, 1], position_list[12], 0, 13, ORANGE, False)
ball14 = Ball(10, [5, 1], position_list[13], 0, 14, GREEN, False)
ball15 = Ball(10, [5, 1], position_list[14], 0, 15, BROWN, False)
white_ball = Ball(10, [5, 1], [500, 302], 0)
#balls = [white_ball, balll]
balls = [white_ball, balll, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10, ball11, ball12, ball13, ball14, ball15]
ball_out_counter = 0
x = 20
y = 110

while not done:
    tisch.draw_field()
    for i in range(len(balls)):
        for j in range(i + 1, len(balls)):
            balls[i].ball_collision(balls[j])
    for ball in balls:
        ball.next_position(tisch)
        ball.draw(tisch, font)
        hole = tisch.is_in_hole(ball)
        if hole:
            ball_out_counter += 1
            #ball.move_ball_to_position(x, y, tisch, font)
            x += 40
            print(ball_out_counter)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            white_ball.move_to_cursor(x, y)
