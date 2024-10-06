import pgzrun
from random import randint
import math

WIDTH = 800
HEIGHT = 700
TITLE = "Space Invaders"
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2

aliens = []
lasers = []
score = 0
player = Actor("player",(CENTER_X,700))
score = 0
move_sequence = 0
move_counter = 0
move_delay = 30

def draw():
    screen.blit("background",(0,0))
    screen.draw.text(str(score), (WIDTH-50, 10), fontsize = 40, owidth = 0.5, ocolor = (0,0,0))

    if len(aliens) == 0:
        draw_center_text("You won!\nPress Enter to re-play.")
    #if player.status >= 30:
    if player.lives == 0:
        draw_center_text("You lost!\nPress Enter to try again.")
    else:
        draw_center_text("You got hit!\nPress Enter to re-spawn.")



def draw_center_text(message):
    screen.draw.text(message, (CENTER_X,CENTER_Y), fontsize = 60, owidth = 0.5, ocolor = (0,0,0))

def draw_lives():
    for i in range(player.lives):
        screen.blit("life",((i*35),10))

def draw_aliens():
    pass

def draw_lasers():
    for laser in lasers:
        laser.draw()

def update():
    global move_counter, lasers 

def check_keys():
    global lasers
    if keyboard.left:
        if player.x > 30:
            player.x -= 5
    if keyboard.right:
        if player.x < 770:
            player.x += 5
    if keyboard.space:
        if player_laser_active == 1:
            player_laser_active = 0
            sounds.laser.play()
            clock.schedule(make_lasers_active, 1.0)
            l = len(lasers)
            lasers.append("laser1",(player.x, player.y-20))
            lasers[l].status = 0
            lasers[l].type = 1

def make_lasers_active():
    player_lasers_active = 1

def update_lasers():
    global lasers, aliens
    for laser in lasers:
        if laser.type == 0:
            alien_laser_hit(laser)
            laser.y += 2
            if laser.y > HEIGHT:
                laser.status = 1
        if laser.type == 1:
            player_laser_hit(laser)
            laser.y -= 2
            if laser.y < 5:
                laser.status = 1
    
    aliens = list_cleanup(aliens)
    lasers = list_cleanup(lasers)

def list_cleanup(l):
    new_list = []
    for i in range(len[l]):
        if l[i] == 0:
            new_list.append(l[i])
    return new_list

def player_laser_hit(laser):
    global score
    for alien in aliens:
        if alien.collidepoint(laser.x, laser.y):
            sounds.eep.play()
            laser.status = 1
            alien.status = 1
            score += 100

def alien_laser_hit(laser):
    if player.collidepoint(laser.x, laser.y):
        player.status = 1
        laser.status = 1
        sounds.explosion.play()


def init_aliens():
    pass

def update_aliens():
    global move_sequence, lasers
    move_x = 0
    move_y = 0
    if move_sequence < 10 or move_sequence > 30:
        move_x = -15
    if move_sequence == 10 or move_sequence == 30:
        move_y = 50
    if move_sequence > 10 or move_sequence < 30:
        move_x = 15
    
    for alien in aliens:
        animate(alien, pos = (alien.x + move_x, alien.y + move_y), duration = 0.5, tween = "linear")

        if randint(0,1) == 0:
            alien.image("alien1")
        else:
            alien.image("alien2")
            if randint(0,10) == 0:
                l = len(lasers)
                lasers.append("laser2",midtop = alien.midbotttom)
                lasers[l].status = 0
                lasers[l].type = 0
        
    move_sequence += 1
    if move_sequence == 40:
        move_sequence = 0


def init_game():
    pass

pgzrun.go()
