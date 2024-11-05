import pgzrun
from random import randint
WIDTH=500
HEIGHT=500
TITLE=('Bandit Chaser')
bandit=Actor('bandit')
safe=Actor('safe')
bandit.pos=100,50
safe.pos=10,10


score=0
game_over=False


def draw():
    screen.blit("wildwest",(0,0))
    bandit.draw()
    safe.draw()
    screen.draw.text('Score =' + str (score), color='red', topleft= (10,10))

    if game_over:
        screen.fill('blue')
        screen.draw.text('Times up !!! Your Final Score Was:' + str(score),midtop=(WIDTH/2,10),fontsize=30, color='orange')

def place_safe():
    safe.x = randint(70, (WIDTH-70))
    safe.y = randint(70, (WIDTH-70))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    
    if keyboard.left:
        bandit.x = bandit.x - 2
    if keyboard.right:
        bandit.x = bandit.x + 2
    if keyboard.up:
        bandit.y = bandit.y - 2
    if keyboard.down:
        bandit.y = bandit.y + 2

    safe_collected = bandit.colliderect(safe)

    if safe_collected:
        score = score + 100
        place_safe()

clock.schedule(time_up, 60.0)



































pgzrun.go()
