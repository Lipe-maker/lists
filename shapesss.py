import pygame,sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Shapes')
#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
#screen fill
screen.fill('dark blue')
pygame.display.update()


while True:
    #creating a rectangle class
    class Rect():
        def _init_(self,color,dimensions):
            self.rect_surf = screen
            self.rect_color = color
            self.rect_dimensions = dimensions

        def draw(self):
            self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

    
    #creating intances

    greenRect=Rect(green,(50,30,100,100))
    redRect=Rect(red,(150,200,150,150))
    blueRect=Rect(blue(300,400,200,200))
    #accessing methods
    greenRect.draw()
    redRect.draw()
    blueRect.draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

pygame.display.update()
