import pgzrun
from random import randint
WIDTH=725
HEIGHT=500
TITLE=('yuji')
r=223
g=225
b=101
yuji = Actor('yuji')
yuji.pos = 300,300
message=''
def draw():
    screen.fill((r,g,b))
    yuji.draw()
    screen.draw.text(message, center = (300,50), fontsize=50)
def placeyuji():
    yuji.x=randint (250, WIDTH-250)
    yuji.y=randint (250, WIDTH-250)
def on_mouse_down(pos):
    global message
    if yuji.collidepoint(pos):
        message = "good shot"
        placeyuji()
    else:
        message = "you missed"
placeyuji()
pgzrun.go()