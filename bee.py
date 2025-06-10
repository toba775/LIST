import pgzrun
from random import randint
WIDTH = 400
HEIGHT = 400
points = 0
gameover = False
bee = Actor("bee")
bee.pos = 200,200
flow = Actor("flower")
flow.pos = 100,100
def draw():
    screen.blit("i2",(0,0))
    bee.draw()
    flow.draw()
    screen.draw.text("Points: "+ str(points),(20,20))
    if gameover == True:
        screen.fill("green")
        screen.draw.text("Times up, your score is: "+ str(points),(100,200))
    
def update():
    global points
    if keyboard.w:
        bee.y = bee.y - 2
    if keyboard.a:
        bee.x = bee.x - 2
    if keyboard.s:
        bee.y = bee.y + 2
    if keyboard.d:
        bee.x = bee.x + 2
    if bee.colliderect(flow):
        flow.x = randint(20,380)
        flow.y = randint(20,380)
        points = points + 1

def timer():
    global gameover
    gameover = True
clock.schedule(timer, 15.0)
pgzrun.go()

