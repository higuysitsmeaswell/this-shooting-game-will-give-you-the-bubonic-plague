import pgzrun

HEIGHT = 600

WIDTH = 1200

TITLE = "galaga"
direction = 1
movedown = False
player = Actor('rocket')
player.pos = (WIDTH/2,HEIGHT-70)
bugs = []
for column in range(8):
    for row in range(4):
        bugs.append(Actor('insect'))
        bugs[-1].x=100+50*column
        bugs[-1].y=80+50*row



def draw():
    screen.fill("black")
    player.draw()
    for bug in bugs:
        bug.draw()

def update():
    global direction, movedown
    
    if len(bugs) > 0 and bugs[0].x < 0 or bugs[-1].x > WIDTH-80:
        direction = direction*-1
        movedown = True
    for bug in bugs:
        bug.x +=4*direction
        if movedown:
            bug.y += 50
    


    


pgzrun.go()