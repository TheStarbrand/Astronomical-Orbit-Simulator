import pygame
import math
pygame.init()

# window setup
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # pygame surface, called window
pygame.display.set_caption("Orbit Simulation")
WHITE = (255, 255, 255)

class Planet:
    AU = 149597870700  # au in meters
    G = 6.67430 * 10 ** -11  # gravitational constant
    SCALE = 250 / AU  # 1 AU = approx 100 pixels
    TIMESTEP = 3600 * 24  # 1 day in seconds

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.x_vel = 0
        self.y_vel = 0

        self.sun = False # its not the sun
        self.distance_to_sun = 0
        self.orbit = [] # list of points that the planet has travelled along


def main():
    run = True
    clock = pygame.time.Clock() # to control the speed of the game and regulate the framerate

    while run:
        clock.tick(60) # maximum framerate of 60 frames per second
        # WIN.fill(WHITE) # puts a white background in 
        pygame.display.update() # updates the display every loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if the user clicks the x button
                run = False

    pygame.quit()


main()