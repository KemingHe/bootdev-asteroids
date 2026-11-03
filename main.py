import pygame

from constants import MAX_FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT),
    )
    clock = pygame.time.Clock()  # Decouple game speed from hardware speed
    dt: float = 0.0  

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle close window -> end game
                return
        screen.fill("black")
        pygame.display.flip()  # Refresh screen
        dt = clock.tick(MAX_FPS) / 1000  # ms -> s
        print(f"delta time={dt}s")


if __name__ == "__main__":
    main()
