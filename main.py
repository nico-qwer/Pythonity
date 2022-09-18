import pygame
pygame.init()

# Other files
from rendering import rendering
from game_object import game_object

from Components.transform import transform

from Components.renderer import renderer

from Components.rigid_body import rigid_body
from Components.collider import circle_collider
from Components.collider import box_collider

# Variables
clock = pygame.time.Clock()
delta_time = 0

# Load Assets

logo = pygame.image.load("Images/PythonityLogo.png")
ball = pygame.image.load("Images/RedBall.png")

# Icon & Title
pygame.display.set_caption("Pythonity")
pygame.display.set_icon(logo)

# All game objects
all_GO = [
    game_object("ball", (
        transform((0, 0), 0, (1, 1)),
        renderer(ball, 0)
    ))

]

for object in all_GO:
    if "Renderer" in object.components:
        rendering.renderable[object.components["Renderer"].level] += (object, )
        # print("added " + object.name + " to render group " + str(object.components["Renderer"].level))

# pygame game loop
def game_loop():
    run = True

    while run:
        # Delta time
        delta_time = clock.tick(rendering.FPS) / 1000
        mouse = pygame.mouse.get_pos()

        # Events ================================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse is at " + str(mouse))

        # Rendering =============================
        all_GO[0].components["Transform"].rotation += 1

        rendering.render()

if __name__ == "__main__":
    game_loop()