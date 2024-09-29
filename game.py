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
    pass

def list_cleanup():
    pass

def player_laser_hit(laser):
    global score
    for alien in aliens:
        if alien.collidepoint(laser.x, laser.y):
            sounds.eep.play()
            laser.status = 1
            alien.status = 1
            score += 100

def alien_laser_hit():
    pass

def init_aliens():
    pass

def update_aliens():
    pass

def init_game():
    pass

pgzrun.go()