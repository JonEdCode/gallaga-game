import pgzrun
import random
WIDTH = 800
HEIGHT = 600
TITLE = "gallaga game!!!!!!!"
ship = Actor("ship")
ship.pos = (400,300)
bug = Actor("bug")
bug.pos = (random.randint(50,750),50)
score = 0
bullets = []
def draw():
   screen.blit("space backround 2",(0,0)) 
   ship.draw()
   screen.draw.text("score "+str(score),(100,40),fontsize = 20)
   bug.draw()
   for bullet in bullets:
       bullet.draw()
def on_key_down(key):
    if key == keys.SPACE:
        bullet = Actor("bullet") 
        bullet.pos = ship.pos
        bullets.append(bullet)
def update():
    global score
    if keyboard.right:
        ship.x = ship.x +4
    if keyboard.left:
        ship.x = ship.x -4
    bug.y = bug.y +2
    if bug.y > 600:
        bug.pos = random.randint(50,750),50

    for bullet in bullets:
        bullet.y = bullet.y -2 
        if bug.colliderect(bullet):
            bug.pos = (random.randint(50,750),50)
            bullets.remove(bullet)
            score = score +10
        
        
    
      






pgzrun.go()
