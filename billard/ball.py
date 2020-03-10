import pygame
import math

class Ball:
    def __init__(self, radius, direction, position, speed, number=None, colour=(255, 255, 255), full=True, on_field=True):
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

    def draw_number(self, screen, font):
        if self.number:
            text = font.render(str(self.number), True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.position[0], self.position[1] - 1))
            screen.blit(text, text_rect)

    def draw(self, tisch, font):
        """
        @param radius: float
        @param color: tuple of ints
        """
        screen = tisch.get_screen()
        ball_rectangle = pygame.Rect(self.position[0] - self.radius, self.position[1] - self.radius,
                                     self.radius * 2, self.radius * 2)
        pygame.draw.ellipse(screen, self.colour, ball_rectangle)
        if not self.full:
            self.draw_white_border(screen)
        self.draw_number(screen, font)

    def apply_friction(self):
        friction = 0.003
        if self.speed < 0:
            self.speed = 0
        if self.speed > 0:
            self.speed -= friction

    def next_position(self, tisch):
        self.normalize_direction()
        x = self.position[0]
        y = self.position[1]
        # print(self.direction)
        x += self.direction[0] * self.speed
        y += self.direction[1] * self.speed
        tisch.check_rebound(self, x, y)
        self.apply_friction()

    def normalize_direction(self):
        direction_length = math.sqrt(self.direction[0] ** 2 + self.direction[1] ** 2)
        self.direction[0] = self.direction[0] / direction_length
        self.direction[1] = self.direction[1] / direction_length

    def move_to_cursor(self, x, y):
        dx = x - self.position[0]
        dy = y - self.position[1]

        self.direction[0] = dx
        self.direction[1] = dy
        self.speed = 2

    def draw_white_border(self, screen):
        borders = self.get_white_border_polygons()
        pygame.draw.polygon(screen, (255, 255, 255), borders[0])
        pygame.draw.polygon(screen, (255, 255, 255), borders[1])

    def get_white_border_polygons(self):
        upper_border = []
        lower_border = []
        for i in range(45, 136):
            upper_border.append(self.get_point_on_border(i))
        for i in range(225, 316):
            lower_border.append(self.get_point_on_border(i))
        return upper_border, lower_border

    def get_point_on_border(self, degree):
        rad = math.radians(degree)
        dx = math.cos(rad) * self.radius
        dy = math.sin(rad) * self.radius
        return self.position[0] + dx, self.position[1] + dy


def main():
    test_ball = Ball(10, [1, 1], [300, 300], 0.5, 1)
    pygame.font.init()
    print(pygame.font.get_fonts())
    pygame.init()
    pygame.event.pump()


if __name__ == '__main__':
    main()
