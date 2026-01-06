# Drawing
# Author: Karina
# Date: 01/05/26

import pygame


def game():
    pygame.init()

    # COLOURS - (R, G, B)
    # CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    GREY = (128, 128, 128)

    # CONSTANTS
    WIDTH = 1024
    HEIGHT = 768
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption(":)")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC

        # ------ DRAWING TO SCREEN
        screen.fill("pink")  # BG
        # Draw a rectangle in the middle of the screen
        # Make it red
        pygame.draw.rect(screen, RED, (WIDTH / 2 - 50, HEIGHT / 2 - 50, 100, 100))

        # Draw a circle on top of the rectangle
        pygame.draw.circle(screen, BLUE, (WIDTH / 2, HEIGHT / 2), 50)

        for i in range(4):
            pygame.draw.polygon(
                screen,
                "hotpink",
                [
                    (600 + i * 100, HEIGHT / 2 - i * 100),
                    (WIDTH / 2 + 100 + i * 100, HEIGHT / 2 + 100 - i * 100),
                    (520 + i * 100, HEIGHT / 2 - i * 100),
                    (500 + i * 100, HEIGHT / 2 + 30 - i * 100),
                    (WIDTH / 2.3 + 100 + i * 100, HEIGHT / 2 + 100 - i * 100),
                ],
            )
        pygame.draw.circle(screen, BLACK, (568, HEIGHT / 2 + 30), 7)
        pygame.draw.line(screen, BLACK, (568, HEIGHT / 2 + 30), (576, HEIGHT / 2 + 100))

        # for offset in range(7):
        #     pygame.draw.line(
        #         screen,
        #         GREEN,
        #         (WIDTH / 2 + 60, 20 + offset * 65),
        #         (WIDTH - 20, HEIGHT / 2 - 20 + offset * 65),
        #     )

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
