import pygame
pygame.init()

# Other files
import rendering

# Variables
clock = pygame.time.Clock()
delta_time = 0

# Load Assets

# Icon & Title
pygame.display.set_caption("Pythonity")
pygame.display.set_icon(pygame.image.load("Images/PythonityLogo.png"))

# pygame game loop
def game_loop():
    run = True

    while run:
        # Delta time
        delta_time = clock.tick(rendering.FPS) / 100
        mouse = pygame.mouse.get_pos()

        # Events ================================
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print("mouse is at " + str(mouse))

        # Rendering =============================
        rendering.render()

if __name__ == "__main__":
    game_loop()