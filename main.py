import sys, pygame
import time
from sdl2 import *
import math
import classes
import random

score=0;
health=1000;

def is_eagle_flying(eaglerect):
    if eaglerect.y<=500:
        return True
    else:
        return False


def is_eagle_walking(eaglerect):
    if eaglerect.y>500:
        return True
    else:
        return False


def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)



pygame.init()
size = width, height = 1280, 760
movedown = [0, 10]
moveup = [0, -10]
bush_moveleft = [-8, 0]
bird_moveleft = [-5, 0]
mouse_moveleft = [-3, 0]
arrow_moveleft = [-10,0]

black = 0, 0, 0

screen = pygame.display.set_mode(size)

eagle0 = pygame.image.load("resources/fly/1.png")
eagle1 = pygame.image.load("resources/fly/2.png")
eagle2 = pygame.image.load("resources/fly/3.png")
eagle3 = pygame.image.load("resources/fly/4.png")
bg = pygame.image.load("resources/bg.jpg")

eagle_walk1 = pygame.image.load("resources/walk/walk1.jpg")
eagle_walk2 = pygame.image.load("resources/walk/walk2.jpg")

attack_eagle = pygame.image.load("resources/attack_eagle.gif")

bush0 = pygame.image.load("resources/bush/0.png")
bush1 = pygame.image.load("resources/bush/1.png")
bush2 = pygame.image.load("resources/bush/2.png")
bush3 = pygame.image.load("resources/bush/3.png")


mouse0 = pygame.image.load("resources/mouse/0.gif")
mouse1 = pygame.image.load("resources/mouse/1.gif")
mouse2 = pygame.image.load("resources/mouse/2.gif")
mouse3 = pygame.image.load("resources/mouse/3.gif")

bird0 = pygame.image.load("resources/bird_food/0.png")
bird1 = pygame.image.load("resources/bird_food/1.png")
bird2 = pygame.image.load("resources/bird_food/2.png")
bird3 = pygame.image.load("resources/bird_food/3.png")

arrow0 = pygame.image.load("resources/arrow/arrow.png")

go = pygame.image.load("resources/gameover/go.gif")

eaglerect = eagle1.get_rect()
eagle_walkrect = eagle1.get_rect()
bgrect = bg.get_rect()
bushrect = bush0.get_rect()
mouserect = mouse0.get_rect()
birdrect = bird0.get_rect()
attack_eaglerect = attack_eagle.get_rect()
arrowrect = arrow0.get_rect()
gorect= go.get_rect()

bushrect.x = 600
bushrect.y = 579
mouserect.x = 600
mouserect.y = 638
birdrect.x = 600
birdrect.y = 100
eaglerect.y = 50
eagle_walkrect.y = 600
eagle_walkrect.x = 50
arrowrect.y=250
arrowrect.x=600

flying_eagle = classes.character("flying Eagle", screen, eagle0, eagle1, eagle2, eagle3, eaglerect)
walking_eagle = classes.character("walking Eagle", screen, eagle_walk1, eagle_walk2, eagle_walk1, eagle_walk2, eagle_walkrect)
attacking_eagle = classes.character("attacking Eagle", screen, attack_eagle, attack_eagle, attack_eagle, attack_eagle, eaglerect )
mouse = classes.character("mouse", screen, mouse0, mouse1, mouse2, mouse3, mouserect)
bush = classes.character("bush", screen, bush0, bush1, bush2, bush3, bushrect)
bird = classes.character("bird", screen, bird0, bird1, bird2, bird3, birdrect)
arrow = classes.character("arrow",screen,arrow0,arrow0,arrow0,arrow0,arrowrect)
i=0
firsthit=0
firsthitarrow=0

while (health>10):
    print health
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if flying_eagle.imagerect.centery >= 50+(eaglerect.height/2):
                flying_eagle.imagerect = flying_eagle.imagerect.move(moveup)

        if event.key == pygame.K_DOWN:
            if flying_eagle.imagerect.centery <= 760-(flying_eagle.imagerect.height/2):
                flying_eagle.imagerect = flying_eagle.imagerect.move(movedown)

    attacking_eagle.imagerect = flying_eagle.imagerect
    bush.velocity(bush_moveleft)
    mouse.velocity(mouse_moveleft)
    bird.velocity(bird_moveleft)
    arrow.velocity(arrow_moveleft)

    image_delay=10
    screen.blit(bg, bgrect)
    bush.movement( i, image_delay)

    if flying_eagle.is_attacking(mouse):
        attacking_eagle.movement(i,image_delay)
        bird.movement(i, image_delay)
        arrow.movement(i,image_delay)
        firsthit=0
        firsthitarrow=0
        health=min(1000,health+50)
        print "attacking mouse"
    elif flying_eagle.is_attacking(bird):
        attacking_eagle.movement(i,image_delay)
        mouse.movement(i, image_delay)
        arrow.movement(i,image_delay)
        firsthit=0
        firsthitarrow=0
        health=min(1000,health+85)
        print "attacking bird"
    elif flying_eagle.is_hit(bush):
        attacking_eagle.movement(i,image_delay)
        bird.movement(i, image_delay)
        mouse.movement(i, image_delay)
        arrow.movement(i,image_delay)
        print "hit"
        firsthit+=1
        if firsthit==1:
            health=min(1000,health-70)
    elif flying_eagle.is_attacking(arrow):
        attacking_eagle.movement(i,image_delay)
        bird.movement(i, image_delay)
        mouse.movement(i, image_delay)
        print "hit by arrow"
        firsthitarrow+=1
        if firsthitarrow==1:
            health=min(1000,health-50)
    elif is_eagle_flying(flying_eagle.imagerect):
        health=health-2;
        flying_eagle.movement(i,image_delay)
        bird.movement(i, image_delay)
        mouse.movement(i, image_delay)
        arrow.movement(i,image_delay)
        firsthit=0
        firsthitarrow=0
        print "flying"
        print score
        score=score+2;
    else:
        print " walking"
        health=health-1;
        bird.movement(i, image_delay)
        mouse.movement(i, image_delay)
        arrow.movement(i,image_delay)
        firsthit=0;
        firsthitarrow=0;
        print score
        score=score+1;
        walking_eagle.movement(i,image_delay)
    #r=random.randint(1,4)
    if arrow.imagerect.x + arrow.imagerect.width < 0:
        arrow.imagerect.x= 1280
    if bush.imagerect.x + bush.imagerect.width < 0:
        bush.imagerect.x = 1280
    if mouse.imagerect.x + mouse.imagerect.width < 0:
        mouse.imagerect.x = 1280
    if bird.imagerect.x + bird.imagerect.width < 0:
        bird.imagerect.x = 1280
    i += 1

print "Game Over"