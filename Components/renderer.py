import pygame

class renderer:
    texture = pygame.surface
    level = 0

    name = "Renderer"

    def __init__(self, texture, level):
        self.texture = texture
        self.texture.set_colorkey((0, 0, 0))
        self.level = level