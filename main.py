import pygame
import math
pygame.init()

# window setup
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # pygame surface, called window
pygame.display.set_caption("Orbit Simulation")

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if the user clicks the x button
                run = False

    pygame.quit()


main()