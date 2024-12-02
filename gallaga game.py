import pgzrun
import random
WIDTH = 800
HEIGHT = 600
TITLE = "gallaga game!!!!!!!"
ship = Actor("ship")
ship.pos = (400,300)
bugs = Actor("bug")
bugs.pos = (random.randint(50,750),50)
score = 0
def draw():
   screen.blit("space backround 2",(0,0)) 
   ship.draw()
   screen.draw.text("score "+str(score),(100,40),fontsize = 20)
   bugs.draw()
def update():
    global score
    if keyboard.right:
        ship.x = ship.x +2
    if keyboard.left:
        ship.x = ship.x -2 
    bugs.y = bugs.y +2
    if bugs.y > 600:
        bugs.pos = random.randint(50,750),50
    
      






pgzrun.go()
