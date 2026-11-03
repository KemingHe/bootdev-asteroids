import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, PLAYER_COLOR, PLAYER_RADIUS
from utils import get_triangle_coords


class Player(CircleShape):

    def __init__(self, x: float, y: float) -> None:
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation: float = 0

    def draw(self, screen: pygame.Surface) -> None:
        """Draws the player as a triangle on screen"""
        pygame.draw.polygon(
            screen,
            PLAYER_COLOR,
            get_triangle_coords(self.position, self.radius, self.rotation),
            LINE_WIDTH,
        )
