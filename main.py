import sys, pygame
import time
from sdl2 import *
import math
import classes

score=0;

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

black = 0, 0, 0

screen = pygame.display.set_mode(size)

eagle0 = pygame.image.load("resources/fly/1.gif")
eagle1 = pygame.image.load("resources/fly/2.gif")
eagle2 = pygame.image.load("resources/fly/3.gif")
eagle3 = pygame.image.load("resources/fly/4.gif")
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

eaglerect = eagle1.get_rect()
eagle_walkrect = eagle1.get_rect()
bgrect = bg.get_rect()
bushrect = bush0.get_rect()
mouserect = mouse0.get_rect()
birdrect = bird0.get_rect()
attack_eaglerect = attack_eagle.get_rect()

bushrect.x = 600
bushrect.y = 579
mouserect.x = 600
mouserect.y = 638
birdrect.x = 600
birdrect.y = 100
eagle_walkrect.y = 600
eagle_walkrect.x = 50

flying_eagle = classes.character("flying Eagle", screen, eagle0, eagle1, eagle2, eagle3, eaglerect)
walking_eagle = classes.character("walking Eagle", screen, eagle_walk1, eagle_walk2, eagle_walk1, eagle_walk2, eagle_walkrect)
attacking_eagle = classes.character("attacking Eagle", screen, attack_eagle, attack_eagle, attack_eagle, attack_eagle, eaglerect )
mouse = classes.character("mouse", screen, mouse0, mouse1, mouse2, mouse3, mouserect)
bush = classes.character("bush", screen, bush0, bush1, bush2, bush3, bushrect)
bird = classes.character("bird", screen, bird0, bird1, bird2, bird3, birdrect)
i=0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if flying_eagle.imagerect.centery >= (eaglerect.height/2):
                flying_eagle.imagerect = flying_eagle.imagerect.move(moveup)

        if event.key == pygame.K_DOWN:
            if flying_eagle.imagerect.centery <= 760-(flying_eagle.imagerect.height/2):
                flying_eagle.imagerect = flying_eagle.imagerect.move(movedown)

    attacking_eagle.imagerect = flying_eagle.imagerect
    bush.velocity(bush_moveleft)
    mouse.velocity(mouse_moveleft)
    bird.velocity(bird_moveleft)

    image_delay=10
    screen.blit(bg, bgrect)
    bush.movement( i, image_delay)

    if flying_eagle.is_attacking(mouse):
        attacking_eagle.movement(i,image_delay)
        bird.movement(i, image_delay)
        mouserect.x = 600
        mouserect.y = 638
        print "attacking mouse"
    elif flying_eagle.is_attacking(bird):
        attacking_eagle.movement(i,image_delay)
        mouse.movement(i, image_delay)
        birdrect.x = 600
        birdrect.y = 100
        print "attacking bird"
    elif is_eagle_flying(flying_eagle.imagerect):
        flying_eagle.movement(i,image_delay)
        bird.movement(i, image_delay)
        mouse.movement(i, image_delay)
        birdrect.x = 600
        birdrect.y = 100
        print "flying"
        print score
        score=score+2;
    else:
        print " walking"
        bird.movement(i, image_delay)
        mouse.movement(i, image_delay)
        print score
        score=score+1;
        walking_eagle.movement(i,image_delay)

    if bush.imagerect.x + bush.imagerect.width < 0:
        bush.imagerect.x = 1280
    if mouse.imagerect.x + mouse.imagerect.width < 0:
        mouse.imagerect.x = 1280
    if bird.imagerect.x + bird.imagerect.width < 0:
        bird.imagerect.x = 1280
    i += 1