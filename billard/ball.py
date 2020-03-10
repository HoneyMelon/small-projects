import tisch
import pygame


class Ball:
    def __init__(self, radius, direction, position, speed, number, colour=(255, 255, 255), full=True, on_field=True):
        """
        @param direction: list
        @param position: list
        @param speed: float
        @param number: int
        @param colour: tuple of ints
        @param full: boolean
        @param on_field: boolean
        """
        self.radius = radius
        self.position = position
        self.direction = direction
        self.speed = speed
        self.number = number
        self.colour = colour
        self.full = full
        self.on_field = on_field

    def add_number(self, screen, font):
        screen.blit(font.render(str(self.number), True, (0, 0, 0)), (self.position[0] - self.radius,
                                                                     (self.position[1] - self.radius) - 5))

    def draw(self, screen, radius):
        """
        @param radius: float
        @param color: tuple of ints
        """
        screen = tisch.draw_field()
        if self.on_field is True:
            pygame.draw.ellipse(screen, self.colour, pygame.Rect(self.position[0] - self.radius,
                                                                 self.position[1] - self.radius, radius * 2,
                                                                 radius * 2))
        else:
            self.position[0] = 20
            self.position[1] = 110

    def apply_friction(self):
        friction = 0.0001
        if self.speed < 0:
            self.speed = 0
        if self.speed > 0:
            self.speed -= friction

    def next_position(self):
        x = self.position[0]
        y = self.position[1]
        # print(self.direction)
        x += self.direction[0] * self.speed
        y += self.direction[1] * self.speed
        tisch.check_rebound(self, x, y)
        self.apply_friction()


def main():
    test_ball = Ball(10, [1, 1], [300, 300], 0.5, 1)
    pygame.font.init()
    print(pygame.font.get_fonts())
    pygame.init()
    pygame.event.pump()


if __name__ == '__main__':
    main()
