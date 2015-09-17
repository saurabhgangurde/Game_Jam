import sys, pygame
import time
from sdl2 import *



def eagle_fly(eagle1, eagle2, eagle3, eagle4, eaglerect, t, image_delay):
    i = t % (4*image_delay)
    if i<image_delay:
        screen.blit(eagle1, eaglerect)
        pygame.display.flip()
    elif (i>image_delay-1 and i<2*image_delay):
        screen.blit(eagle2, eaglerect)
        pygame.display.flip()
    elif (i>2*image_delay-1 and i< 3*image_delay):
        screen.blit(eagle3, eaglerect)
        pygame.display.flip()
    elif (i>3*image_delay-1 and i<4*image_delay):
        screen.blit(eagle4, eaglerect)
        pygame.display.flip()


def eagle_walk(eagle1, eagle2, eaglerect, t, image_delay):
    i = t % (4*image_delay)
    if i<image_delay:
        screen.blit(eagle1, eaglerect)
        pygame.display.flip()
    elif (i>image_delay-1 and i<2*image_delay):
        screen.blit(eagle2, eaglerect)
        pygame.display.flip()


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
    return sqrt((x1-x2)**2+(y1-y2)**2)










def bush_movement(bush0, bush1, bush2, bush3, bushrect, t, image_delay):
    i = t % (4*image_delay)
    if i<image_delay:
        screen.blit(bush0, bushrect)
        pygame.display.flip()
    elif i>image_delay-1 and i<2*image_delay:
        screen.blit(bush1, bushrect)
        pygame.display.flip()
    elif i>2*image_delay-1 and i< 3*image_delay:
        screen.blit(bush2, bushrect)
        pygame.display.flip()
    elif i>3*image_delay-1 and i<4*image_delay:
        screen.blit(bush3, bushrect)
        pygame.display.flip()


def mouse_movement(mouse0, mouse1, mouse2, mouse3, mouserect, t, image_delay):
    i = t % (4*image_delay)
    if i<image_delay:
        screen.blit(mouse0, mouserect)
        pygame.display.flip()
    elif i>image_delay-1 and i<2*image_delay:
        screen.blit(mouse1,mouserect)
        pygame.display.flip()
    elif i>2*image_delay-1 and i< 3*image_delay:
        screen.blit(mouse2, mouserect)
        pygame.display.flip()
    elif i>3*image_delay-1 and i< 4*image_delay:
        screen.blit(mouse3, mouserect)
        pygame.display.flip()


def bird_movement(bird0, bird1, bird2, bird3, birdrect, t, image_delay):
    i = t % (4*image_delay)
    if i<image_delay:
        screen.blit(bird0, birdrect)
        pygame.display.flip()
    elif i>image_delay-1 and i<2*image_delay:
        screen.blit(bird1,birdrect)
        pygame.display.flip()
    elif i>2*image_delay-1 and i< 3*image_delay:
        screen.blit(bird2, birdrect)
        pygame.display.flip()
    elif i>3*image_delay-1 and i< 4*image_delay:
        screen.blit(bird3, birdrect)
        pygame.display.flip()

pygame.init()
size = width, height = 1280, 760
movedown = [0, 10]
moveup = [0, -10]
bush_moveleft = [-10, 0]
bird_moveleft = [-5, 0]
mouse_moveleft = [-5, 0]

black = 0, 0, 0

screen = pygame.display.set_mode(size)

eagle1 = pygame.image.load("resources/fly/1.gif")
eagle2 = pygame.image.load("resources/fly/2.gif")
eagle3 = pygame.image.load("resources/fly/3.gif")
eagle4 = pygame.image.load("resources/fly/4.gif")
bg = pygame.image.load("resources/bg.jpg")
eagle_walk1 = pygame.image.load("resources/walk/walk1.jpg")
eagle_walk2 = pygame.image.load("resources/walk/walk2.jpg")

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
bgrect = bg.get_rect()
bushrect = bush0.get_rect()
mouserect = mouse0.get_rect()
birdrect = bird0.get_rect()

bushrect.x = 600
bushrect.y = 100
mouserect.x = 600
mouserect.y = 100
birdrect.x = 600
birdrect.y = 100

i=0
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if eaglerect.centery>=(eaglerect.height/2):
                eaglerect = eaglerect.move(moveup)
        if event.key == pygame.K_DOWN:
            if eaglerect.centery <= 760-(eaglerect.height):
                eaglerect = eaglerect.move(movedown)
    bushrect = bushrect.move(bush_moveleft)
    mouserect = mouserect.move(mouse_moveleft)
    birdrect = birdrect.move(mouse_moveleft)

    image_delay=10
    screen.blit(bg, bgrect)
    bush_movement(bush0, bush1, bush2, bush3, bushrect, i, image_delay)
    mouse_movement(mouse0, mouse1, mouse2, mouse3, mouserect, i, image_delay)
    bird_movement(bird0, bird1, bird2, bird3, birdrect, i, image_delay)

    if is_eagle_flying(eaglerect):
        eagle_fly(eagle1, eagle2, eagle3, eagle4, eaglerect,  i, image_delay)
    elif is_eagle_walking(eaglerect):
        eagle_walk(eagle_walk1, eagle_walk2, eaglerect,  i, image_delay)

    if bushrect.x < 0:
        bushrect.x = 1280
    if mouserect.x < 0:
        mouserect.x = 1280
    if birdrect.x < 0:
        birdrect.x = 1280
    i += 1