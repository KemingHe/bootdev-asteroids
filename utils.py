import pygame


def get_triangle_coords(
        position: pygame.Vector2,
        radius: float,
        rotation: float,
    ) -> list[pygame.Vector2]:
    forward = pygame.Vector2(0, 1).rotate(rotation)
    right = pygame.Vector2(0, 1).rotate(rotation + 90) * radius / 1.5
    a = position + forward * radius
    b = position - forward * radius - right
    c = position - forward * radius + right
    return [a, b, c]
