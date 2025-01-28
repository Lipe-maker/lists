from pygame import *
import pygame,sys
from pygame.locals import QUIT
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Shapes')
screen.fill('dark blue')
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


pygame.display.update()
