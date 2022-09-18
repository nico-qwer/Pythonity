import main
import pygame

# Make screen
WIDTH, HEIGHT = 960, 500
screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)

# Variables
FPS = 60

# Renderable objs
renderable = []

def render():
    screen.fill((50, 50, 50))
    pygame.draw.rect(screen, (75, 40, 40), pygame.Rect(10, 50, 100, 100))
    
    pygame.display.update()