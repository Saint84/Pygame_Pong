import pygame
import time

pygame.init()
window = pygame.display.set_mode([1280, 720])
title = pygame.display.set_caption('Game Pong - Inicializado.')
field = pygame.image.load("assets/field.png")

p1 = pygame.image.load("assets/player1.png")
p2 = pygame.image.load("assets/player2.png")
b = pygame.image.load("assets/ball.png")
score1_img = pygame.image.load("assets/score/0.png")
score2_img = pygame.image.load("assets/score/0.png")
win = pygame.image.load("assets/win.png")

score1 = 0
score2 = 0

p1_y = 310
p1_y_moveup = False
p1_y_movedown = False

p2_y = 310

pos_x = 617
pos_y = 337
pos_dir_x = -15
pos_dir_y = 10


def draw():
    if (score1 < 9) and (score2 < 9):
        window.blit(field, (0, 0))
        window.blit(p1, (50, p1_y))
        window.blit(p2, (1150, p2_y))
        window.blit(b, (pos_x, pos_y))
        window.blit(score1_img, (500, 40))
        window.blit(score2_img, (710, 40))
        move_ball()
        move_p1()
        move_p2()
    else:
        window.blit(win, (300, 330))


def move_ball():
    global pos_x
    global pos_y
    global pos_dir_x
    global pos_dir_y
    global score2
    global score1
    global score1_img
    global score2_img
    pos_x += pos_dir_x
    pos_y += pos_dir_y
    if pos_x < 125:
        if (p1_y <= pos_y + 23) and (p1_y + 146 >= pos_y):
            pos_dir_x *= -1
    if pos_x > 1100:
        if (p2_y <= pos_y + 23) and (p2_y + 146 >= pos_y):
            pos_dir_x *= -1
    if (pos_y >= 687) or (pos_y <= 10):
        pos_dir_y *= -1
    if pos_x < -80:
        time.sleep(1)
        pos_y = 337
        pos_x = 617
        pos_dir_x *= -1
        pos_dir_y *= -1
        score2 += 1
        score2_img = pygame.image.load(f"assets/score/" + str(score2) + ".png")
    if pos_x > 1320:
        time.sleep(1)
        pos_y = 337
        pos_x = 617
        pos_dir_x *= -1
        pos_dir_y *= -1
        score1 += 1
        score1_img = pygame.image.load(f"assets/score/" + str(score1) + ".png")


def move_p1():
    global p1_y
    if p1_y_moveup:
        if p1_y > 0:
            p1_y -= 10
        else:
            p1_y = 0
    elif p1_y_movedown:
        if p1_y < 575:
            p1_y += 10
        else:
            p1_y = 575


def move_p2():
    global pos_y
    global p2_y

    p2_y = pos_y


loop = True
while loop:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            loop = False
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_w:
                p1_y_moveup = True
            if events.key == pygame.K_s:
                p1_y_movedown = True
        elif events.type == pygame.KEYUP:
            if events.key == pygame.K_w:
                p1_y_moveup = False
            if events.key == pygame.K_s:
                p1_y_movedown = False
    draw()
    pygame.display.update()
