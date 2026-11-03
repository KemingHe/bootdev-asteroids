import pygame

from circleshape import CircleShape
from constants import (
    LINE_WIDTH,
    PLAYER_COLOR,
    PLAYER_RADIUS,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)
from utils import get_triangle_coords


class Player(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 180  # Init pointing upwards

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the player as a triangle on screen"""
        pygame.draw.polygon(
            screen,
            PLAYER_COLOR,
            get_triangle_coords(self.position, self.radius, self.rotation),
            LINE_WIDTH,
        )

    def __rotate(self, dt: float) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def __move(self, dt: float) -> None:
        unit_v2 = pygame.Vector2(0, 1)  # Init pointing straigh down
        rotated = unit_v2.rotate(self.rotation)
        rotated_with_speed = rotated * PLAYER_SPEED * dt
        self.position += rotated_with_speed
        
    def update(self, dt: float) -> None:
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
        
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:  # Counter-clock-wise
            self.__rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:  # Clock-wise
            self.__rotate(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.__move(-dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.__move(dt)
