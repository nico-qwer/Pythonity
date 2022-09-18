import pygame
from Components.camera import camera
from operations import *

class rendering:
    # Make screen
    WIDTH, HEIGHT = 960, 500
    screen = pygame.display.set_mode([WIDTH, HEIGHT], pygame.RESIZABLE)

    # Variables
    FPS = 60

    # objs
    renderable = [()]

    def render():
        rendering.screen.fill(camera.fill)
        
        for layer in rendering.renderable:
            for object in layer:
                texture_to_render = object.components["Renderer"].texture

                texture_to_render = pygame.transform.scale(
                    texture_to_render, 
                    multiply_tuples(object.components["Transform"].scale, texture_to_render.get_size())
                )
                
                texture_to_render = pygame.transform.rotate(texture_to_render, -object.components["Transform"].rotation)
                texture_to_render = texture_to_render.convert()

                pygame_pos = object.components["Transform"].position

                pygame_pos = add_tuples(pygame_pos, multiply_tuple(camera.position, -1, True))

                pygame_pos = (
                    pygame_pos[0] + int(rendering.screen.get_width() / 2), 
                    -pygame_pos[1] + int(rendering.screen.get_height() / 2)
                )

                corner_pos = add_tuples(
                    pygame_pos, 
                    multiply_tuples(
                        texture_to_render.get_size(),
                        (-0.5, -0.5),
                        True
                    )
                )

                rendering.screen.blit(texture_to_render, corner_pos)
    
        pygame.display.update()