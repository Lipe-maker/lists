import pygame,sys

from pygame.locals import QUIT
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Shapes')
pygame.display.update()
r=(123,0,0)
g=(0,231,0)
b=(0,0,7)
screen.fill((g))
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

class circle():
    def __init__(surface,color,center,radius):
        self.circle_surf = surface

    pygame.display.update()
