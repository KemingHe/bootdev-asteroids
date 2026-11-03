import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT),
    )

    while True:
        log_state()
        for event in pygame.event.get():  # Process game events
            if event.type == pygame.QUIT:  # Handle close window -> end game
                return
        screen.fill("black")
        pygame.display.flip()  # Refreshes screen, called last per game loop
    


if __name__ == "__main__":
    main()
