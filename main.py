import pgzrun, time

HEIGHT = 600

WIDTH = 1200

TITLE = "galaga"
direction = 1
movedown = False
player = Actor('rocket')
player.pos = (WIDTH/2,HEIGHT-70)
bugs = []
player.dead = False
player.countdown = 90
for column in range(8):
    for row in range(4):
        bugs.append(Actor('insect'))
        bugs[-1].x=100+(50*column)
        bugs[-1].y=80+(50*row)
speed = 5
gameover = False
bullets = []
score = 0


def draw():
    global gameover
    screen.fill("black")
    if player.dead == False:
        player.draw()
    for bug in bugs:
        bug.draw()
    for bullet in bullets:
        bullet.draw()
    screen.draw.text("score:"+str(score),(50,50))
    if gameover:
        screen.draw.text("Gameover",(300,600))
        time.sleep(5)
        

def update():
    global direction, movedown, speed, score, gameover
    print(gameover)

    if player.dead == False:
        if keyboard.a:
            player.x-=speed
            if player.x<0:
                player.x=0
        if keyboard.d:
            player.x+=speed
            if player.x>WIDTH:
                player.x=WIDTH
    
    
    for bug in bugs:
        bug.x +=speed*direction
        for bullet in bullets:
            if bullet.colliderect(bug):
                score+=1
                bugs.remove(bug)
                bullets.remove(bullet)
        if bug.y>HEIGHT:
            bugs.remove(bug)
        if bug.colliderect(player):
            player.dead = True
    if player.dead:
        player.countdown-=1
        if player.countdown == 0:
            player.dead = False
            player.countdown = 90
    if len(bugs)==0:
        gameover = True
    if gameover == False:
        if len(bugs) >= 0 and bugs[0].x < 0 or bugs[-1].x > WIDTH-80:
            direction = direction*-1
            movedown = True
        if movedown:
            for bug in bugs:
                bug.y += 0.5
        for bullet in bullets:
            if bullet.y<0:
                bullets.remove(bullet)
            else:
                bullet.y-=10
    
def on_key_down():
    global bullets, player
    if keyboard.space:
        bullets.append(Actor("bullet"))
        bullets[-1].x=player.x
        bullets[-1].y=player.y



    


pgzrun.go()