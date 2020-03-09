import tisch
import pygame


class Ball:
    def __init__(self, radius, direction, position, speed):
        """
        @param direction: list
        @param position: list
        @param speed: float
        """
        self.radius = radius
        self.position = position
        self.direction = direction
        self.speed = speed

    def draw(self, radius, color=(255, 255, 255)):
        """
        @param radius: float
        @param color: tuple of ints
        """
        screen = tisch.draw_field()
        pygame.draw.ellipse(screen, color, pygame.Rect(self.position[0] - self.radius,
                                                       self.position[1] - self.radius, radius * 2, radius * 2))

    def next_position(self):
        friction = 0.0003
        x = self.position[0]
        y = self.position[1]
        x += self.direction[0] * self.speed
        y += self.direction[1] * self.speed

        # left wall
        if x - self.radius <= 25:
            self.position[0] = 25 + self.radius
            self.direction[0] = abs(self.direction[0])

        # right wall
        elif x + self.radius >= 625:
            self.position[0] = 625 - self.radius
            self.direction[0] = -abs(self.direction[0])

        # upper wall
        elif y - self.radius <= 150:
            self.position[1] = 150 + self.radius
            self.direction[1] = abs(self.direction[1])

        # lower wall
        elif y + self.radius >= 450:
            self.position[1] = 450 - self.radius
            self.direction[1] = -abs(self.direction[1])
        else:
            self.position[0] = x
            self.position[1] = y
        if self.speed > 0:
            self.speed -= friction


def main():
    pygame.init()
    done = False
    pygame.event.pump()

    test_ball = Ball(10, [2, 2], [300, 300], 0.5)
    test_ball.draw(10)
    while not done:
        test_ball.next_position()
        test_ball.draw(10)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True


if __name__ == '__main__':
    main()
