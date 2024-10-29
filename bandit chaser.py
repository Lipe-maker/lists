import pgzrun
from random import randint
WIDTH=700
HEIGHT=450
TITLE=('Bandit Chaser')
bandit=Actor('bandit')
safe=Actor('safe')
bandit.pos=100,50
safe.pos=10,10


def draw():
    screen.blit("wildwest",(0,0))
    bandit.draw()
    safe.draw()

























pgzrun.go()