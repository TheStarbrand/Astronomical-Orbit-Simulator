import pygame
import math
pygame.init()

# window setup
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT)) # pygame surface, called window
pygame.display.set_caption("Orbit Simulation")

WHITE = (255, 255, 255)
BLUE = (100, 149, 237)
RED =   (188, 39, 50)
DARK_GREY = (80, 71, 88)

EARTH_SIZE = 16
SUN_SIZE = 30
MARS_SIZE = 12
MERCURY_SIZE = 8
VENUS_SIZE = 14


class aBody:
    AU = 149597870700  # au in meters
    G = 6.67430 * 10 ** -11  # gravitational constant
    SCALE = 230 / AU  # 1 AU = approx 100 pixels
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

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        x_distance = other_x - self.x
        y_distance = other_y - self.y
    

def main():
    run = True
    clock = pygame.time.Clock() # to control the speed of the game and regulate the framerate

    sun = aBody(0, 0, SUN_SIZE , (255, 255, 0), 1.989 * 10 ** 30)
    sun.isSun = True
    sun.isPlanet = False

    earth = aBody(1 * aBody.AU, 0, EARTH_SIZE, BLUE, 5.9742 * 10 ** 24 )
    mars = aBody(-1.524 * aBody.AU, 0, MARS_SIZE, RED, 6.4171 * 10 ** 23)
    mercury = aBody(0.387 * aBody.AU, 0, MERCURY_SIZE, DARK_GREY, 3.285 * 10 ** 23)
    venus = aBody(-0.723 * aBody.AU, 0, VENUS_SIZE, WHITE, 4.8685 * 10 ** 24)

    bodies = [sun, earth, mars, mercury, venus]

    while run:
        clock.tick(60) # maximum framerate of 60 frames per second
        # WIN.fill(WHITE) # puts a white background in 
        #pygame.display.update() # updates the display every loop

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #if the user clicks the x button
                run = False

        for body in bodies:
            body.draw(WIN)
            pygame.display.update()

    pygame.quit()


main()