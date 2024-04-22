import pygame
import math
pygame.init()

# window setup
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # pygame surface, called window
pygame.display.set_caption("Orbit Simulation")
WHITE = (255, 255, 255)

class aBody:
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

        self.isSun = False # its not the sun
        self.isPlanet = True # it's a planet
        self.distance_to_sun = 0
        self.orbit = [] # list of points that the astronomical body has travelled along

def draw(self, win):
    x = self.x * self.SCALE + WIDTH / 2
    y = self.y * self.SCALE + HEIGHT / 2
    pygame.draw.circle(win, self.color, (x, y), self.radius)
    

def main():
    run = True
    clock = pygame.time.Clock() # to control the speed of the game and regulate the framerate

    sun = aBody(0, 0, 40 , (255, 255, 0), 1.989 * 10 ** 30)
    sun.isSun = True
    bodies = [sun]

    while run:
        clock.tick(60) # maximum framerate of 60 frames per second
        # WIN.fill(WHITE) # puts a white background in 
        pygame.display.update() # updates the display every loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if the user clicks the x button
                run = False

    pygame.quit()


main()