import pgzrun
from random import randint
from time import time

WIDTH=800
LENGTH=600

satilite=Actor('satilite')




satilites = []
lines = []
next_satilite = 0


start_time = 0
total_time = 0
end_time = 0

number_of_satlite = 10

def create_satelite():
    global start_time
    for count in range(0,number_of_satlite):
        satilite = Actor('satilite')
        satilite.pos = randint(40,WIDTH-40), randint(40, LENGTH-40)
        satilites.append(satilite)
    start_time = time()


def draw():
    global total_time

    screen.blit('space bg',(0,0))
    number = 1
    
    for satlite in satilites:
        screen.draw.text(str(number), (satlite.pos[0], satlite.pos[1]+20))
        satlite.draw()
        number = number + 1

    for line in lines :
        screen.draw.line(line[0], line[1], (255,255,255))

    if next_satilite < number_of_satlite:
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)),(10,10), fontsize=30)
    else:
        screen.draw.text(str(round(total_time,1)),(10,10), fontsize=30)

def update():

    pass

def on_mouse_down(pos):
    global next_, lines

    if next_satilite < number_of_satlite:
        if satilite[next_satilite].collidepoint(pos):
            if next_satilite:
                lines.append((satilite[next_satilite-1].pos, satilite[next_satilite].pos))
        else:
            lines = []
            next_satilite = 0

create_satelite()

pgzrun.go()
