import pygame,sys

from pygame.locals import QUIT
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Shapes')

pygame.display.update()
screen.fill(('red'))
pygame.display.update()

class arc():
    def __init__(self,  color, rect, start_angle, stop_angle):
        self.arc_surface = screen
        self.arc_rect = rect
        self.arc_color = color
        self.arc_start_angle = start_angle
        self.arc_stop_angle = stop_angle

    def draw(self):
        self.Draw_arc = pygame.draw.arc(self.arc_surface, self.arc_rect, self.arc_color, self.arc_start_angle, self.arc_stop_angle)

arc=arc(green,250,100,250,400)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



            
