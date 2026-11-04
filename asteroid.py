import pygame

from circleshape import CircleShape
from constants import ASTEROID_COLOR, LINE_WIDTH


class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(
            screen,
            ASTEROID_COLOR,
            self.position,  # Center
            self.radius,
            LINE_WIDTH,
        )
        
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
