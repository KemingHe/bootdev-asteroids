import random

import pygame

from circleshape import CircleShape
from constants import (
    ASTEROID_COLOR,
    ASTEROID_MIN_RADIUS,
    ASTEROID_SPLIT_MAX_ANGLE,
    ASTEROID_SPLIT_MIN_ANGLE,
    ASTEROID_SPLIT_VELOCITY_MULTIPLIER,
    LINE_WIDTH,
)
from logger import log_event


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

    def split(self) -> None:
        self.kill()
        # For S asteroids, simply disappear
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # For above S asteroids, split into two smaller in rand dir
        log_event("asteroid_split")
        rand_angle: float = random.uniform(
            ASTEROID_SPLIT_MIN_ANGLE,
            ASTEROID_SPLIT_MAX_ANGLE,
        )
        new_v1: pygame.Vector2 = (
            self.velocity.rotate(rand_angle) * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        )
        new_v2: pygame.Vector2 = (
            self.velocity.rotate(-rand_angle) * ASTEROID_SPLIT_VELOCITY_MULTIPLIER
        )
        new_r: float = self.radius - ASTEROID_MIN_RADIUS
        x, y = self.position

        smaller1, smaller2 = Asteroid(x, y, new_r), Asteroid(x, y, new_r)
        smaller1.velocity, smaller2.velocity = new_v1, new_v2
        