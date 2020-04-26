from player import Player
import pygame
from ball import *
from tisch import Tisch
from ball import Ball
from cue import *


class Game:
    def __init__(self, finished):
        self.finished = finished
        self.players = self.initialise_players()

    def initialise_players(self):
        """
        @return: list of player objects
        """
        player1 = Player('Player 1', True, 1)
        player2 = Player('Player 2', False, 2)
        return player1, player2

    def init_balls(self):
        """
        @return: list of ball objects
        """
        tisch = Tisch()
        position_list = tisch.start_position_of_balls(5, 150, 260, 21)
        balll = Ball(10, [5, 1], position_list[0], 0, 1, get_colour('YELLOW'))
        ball2 = Ball(10, [5, 1], position_list[1], 0, 2, get_colour('BLUE'))
        ball3 = Ball(10, [2, 1], position_list[2], 0, 3, get_colour('RED'))
        ball4 = Ball(10, [5, 1], position_list[3], 0, 4, get_colour('PURPLE'))
        ball5 = Ball(10, [5, 1], position_list[4], 0, 5, get_colour('ORANGE'))
        ball6 = Ball(10, [5, 1], position_list[5], 0, 6, get_colour('GREEN'))
        ball7 = Ball(10, [5, 1], position_list[6], 0, 7, get_colour('BROWN'))
        ball8 = Ball(10, [5, 1], position_list[10], 0, 8, get_colour('BLACK'))
        ball9 = Ball(10, [5, 1], position_list[8], 0, 9, get_colour('YELLOW'), False)
        ball10 = Ball(10, [5, 1], position_list[9], 0, 10, get_colour('BLUE'), False)
        ball11 = Ball(10, [5, 1], position_list[7], 0, 11, get_colour('RED'), False)
        ball12 = Ball(10, [5, 1], position_list[11], 0, 12, get_colour('PURPLE'), False)
        ball13 = Ball(10, [5, 1], position_list[12], 0, 13, get_colour('ORANGE'), False)
        ball14 = Ball(10, [5, 1], position_list[13], 0, 14, get_colour('GREEN'), False)
        ball15 = Ball(10, [5, 1], position_list[14], 0, 15, get_colour('BROWN'), False)
        white_ball = Ball(10, [5, 1], [500, 302], 0)
        balls = [white_ball, balll, ball2, ball3, ball4, ball5, ball6, ball7, ball8, ball9, ball10, ball11, ball12,
                 ball13,
                 ball14, ball15]
        return balls

    def mainloop(self, balls):
        """
        mainloop and game procedure
        """
        done = False
        pygame.init()

        pygame.font.init()
        font = pygame.font.SysFont('arialblack', 11)

        white_ball = balls[0]
        ball_out_counter = 0
        tisch = Tisch()
        pygame.event.pump()

        shot = False
        correct_ball_scored = False
        other_or_white_scored = False
        not_allowed = False

        # self.enter_player_names(tisch)

        while not done:
            if shot and not balls_in_motion(balls):
                if not correct_ball_scored or other_or_white_scored:
                    for player in self.players:
                        # player switch
                        player.playing = not player.playing
                shot = False
                correct_ball_scored = False
                other_or_white_scored = False

            tisch.draw_field()
            self.draw_player_names(tisch)

            # check collision
            for i in range(len(balls)):
                for j in range(i + 1, len(balls)):
                    if balls[i].on_field and balls[j].on_field:
                        balls[i].ball_collision(balls[j])

            for ball in balls:
                ball.draw(tisch, font)
                ball.next_position(tisch)
                is_in_hole = tisch.is_in_hole(ball)
                not_allowed = False
                if is_in_hole:
                    if ball.number is None:
                        ball.on_field = False
                        ball.speed = 0
                        other_or_white_scored = True
                    else:
                        if ball_out_counter == 0:
                            self.get_active_player().full = ball.full
                            self.get_inactive_player().full = not ball.full

                        # win condition
                        if ball.number == 8:
                            if self.get_active_player().scored == 7:
                                print(self.get_active_player().name, 'hat alle Kugeln versenkt und gewonnen!')
                            else:
                                print(self.get_inactive_player().name,
                                      'hat gewonnen, die schwarze Kugel wurde zu früh versenkt!')
                            done = True

                        ball_out_counter += 1

                        # check if correct ball was scored
                        if self.get_active_player().full == ball.full:
                            scored_player = self.get_active_player()
                            correct_ball_scored = True
                        else:
                            scored_player = self.get_inactive_player()
                            other_or_white_scored = True

                        scored_player.scored_ball()

                        ball.position[0] = scored_player.get_x_position_for_ball()
                        ball.position[1] = 100
                        ball.speed = 0
                        ball.on_field = False

            # placing white ball back
            if not white_ball.on_field and not balls_in_motion(balls):
                pygame.draw.line(tisch.screen, (255, 255, 255), [500, 150], [500, 450])
                _, mouse_y = pygame.mouse.get_pos()
                if mouse_y < 150:
                    mouse_y = 150
                elif mouse_y > 450:
                    mouse_y = 450
                for ball in balls:
                    if ball.is_ball_at_position(500, mouse_y):
                        if ball.number is not None:
                            not_allowed = True
                white_ball.place_at_cursor(500, mouse_y)

            if white_ball.on_field and not balls_in_motion(balls):
                x, y = pygame.mouse.get_pos()

                distance = white_ball.distance_to_cursor(x, y)
                drawn_speed = distance / 45
                if drawn_speed > 5:
                    drawn_speed = 5

                draw_cue(tisch.screen, white_ball, x, y)
                tisch.draw_speed_meter(drawn_speed)

            # end loop or move white ball in cursor direction
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if not balls_in_motion(balls) and white_ball.on_field and event.type == pygame.MOUSEBUTTONDOWN \
                        and event.button == 1:
                    x, y = pygame.mouse.get_pos()
                    white_ball.move_to_cursor(x, y)
                    shot = True
                if not white_ball.on_field and not not_allowed and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    white_ball.on_field = True
                    white_ball.speed = 0

            pygame.display.flip()

    def draw_player_names(self, tisch):
        """
        draws player names
        """
        pygame.font.init()
        font = pygame.font.SysFont('arialblack', 20)
        if self.players[0].playing:
            background_colour1 = (82, 220, 86)
        else:
            background_colour1 = None
        if self.players[1].playing:
            background_colour2 = (82, 220, 86)
        else:
            background_colour2 = None
        screen = tisch.get_screen()

        player1 = font.render(str(self.players[0].name), True, (0, 0, 0), background_colour1)
        player1_rect = player1.get_rect(center=(100, 50))
        screen.blit(player1, player1_rect)

        player2 = font.render(str(self.players[1].name), True, (0, 0, 0), background_colour2)
        player2_rect = player2.get_rect(center=(500, 50))
        screen.blit(player2, player2_rect)

    def get_active_player(self):
        """
        @return: player object
        """
        for player in self.players:
            if player.playing:
                return player

    def get_inactive_player(self):
        """
        @return: player object
        """
        for player in self.players:
            if not player.playing:
                return player


def get_colour(colour):
    """
    @param colour: string
    @return: tuple
    returns rgb colours
    """
    if colour == 'YELLOW':
        return 254, 211, 70
    if colour == 'BLUE':
        return 89, 157, 222
    if colour == 'RED':
        return 221, 88, 89
    if colour == 'PURPLE':
        return 180, 110, 199
    if colour == 'ORANGE':
        return 253, 157, 83
    if colour == 'GREEN':
        return 157, 192, 124
    if colour == 'BROWN':
        return 164, 84, 88
    if colour == 'BLACK':
        return 59, 59, 59


def main():
    game = Game(False)
    balls = game.init_balls()
    game.mainloop(balls)


if __name__ == '__main__':
    main()
