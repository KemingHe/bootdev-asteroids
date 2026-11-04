import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import BACKGROUND_COLOR, MAX_FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen: pygame.Surface = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT),
    )

    # Group game objs to manage them centrally
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    AsteroidField()

    Player.containers = (updatable, drawable)
    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # Init player

    clock = pygame.time.Clock()  # Decouple game speed from hardware speed
    dt: float = 0.0

    while True:
        # Step 0. Write logs
        log_state()

        # Step 1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Handle close window -> end game
                return

        # Step 2. Update game state
        updatable.update(dt)

        # Step 3. Render to screen
        screen.fill(BACKGROUND_COLOR)
        for memb in drawable:
            memb.draw(screen)
        pygame.display.flip()  # Refresh screen last

        # Step 4. Tick the clock to stablize FPS
        dt = clock.tick(MAX_FPS) / 1000  # ms -> s
        

if __name__ == "__main__":
    main()
