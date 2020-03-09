import pygame


def draw_field():
    pygame.init()
    screen = pygame.display.set_mode((650, 600))
    distance = 305 / 4

    pygame.event.pump()

    # bande
    pygame.draw.rect(screen, (80, 63, 38), pygame.Rect(0, 125, 650, 350))
    # loch
    # pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(310, 450, 30, 25))
    # field
    pygame.draw.rect(screen, (57, 110, 44), pygame.Rect(25, 150, 600, 300))
    # markers
    for i in range(20, 630, int(distance)):
        pygame.draw.circle(screen, (255, 255, 255), (i, 140), 2)
        pygame.draw.circle(screen, (255, 255, 255), (i, 460), 2)
    for i in range(145, 455, int(distance)):
        pygame.draw.circle(screen, (255, 255, 255), (15, i), 2)
        pygame.draw.circle(screen, (255, 255, 255), (635, i), 2)
    # lock kreis
    pygame.draw.circle(screen, (0, 0, 0), (325, 145), 15)   # oben
    pygame.draw.circle(screen, (0, 0, 0), (325, 455), 15)   # unten
    # ecken
    pygame.draw.circle(screen, (0, 0, 0), (25, 150), 15)    # links oben
    pygame.draw.circle(screen, (0, 0, 0), (625, 150), 15)   # rechts oben
    pygame.draw.circle(screen, (0, 0, 0), (25, 450), 15)    # links unten
    pygame.draw.circle(screen, (0, 0, 0), (625, 450), 15)   # recht unten

    return screen


def main():
    draw_field()
    pygame.display.flip()


if __name__ == '__main__':
    main()


