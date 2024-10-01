import pgzrun
WIDTH=725
HEIGHT=700
TITLE=('yuji')
r=223
g=225
b=101
yuji = Actor('yuji2.0')
yuji.pos = 300,300
message=''
def draw():
    screen.fill((r,g,b))
    yuji.draw()


pgzrun.go()