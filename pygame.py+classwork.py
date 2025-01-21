import pygame.display
import pygame
pygame.init()
screen = pygame.disply.set_mode(500,500)
pygame.display.set_caption('Shapes')
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

pygame.disply.update()

-----CLASSWORK.PY-----

class student:

    def __init__(self,age,grade,name):
       self.name = name
       self.age = age
       self.grade = grade

    def details(self):
        print('Hello, my name is ',self.name,'and i`m in ',self.grade)
        print('I`m ',self.name,'old')



p1 = student('13','6','Dan')
p2 = student ('Joseph','19','9')



print (p1.age)
