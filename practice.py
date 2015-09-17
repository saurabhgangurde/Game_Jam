import sys, pygame
import time
from sdl2 import *

pygame.init()
size = width, height = 1280, 760
movedown = [0, 10]
moveup = [0, -10]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

eagle1 = pygame.image.load("resources/1.gif")
eagle2 = pygame.image.load("resources/2.gif")
eagle3 = pygame.image.load("resources/3.gif")
eagle4 = pygame.image.load("resources/4.gif")
bg = pygame.image.load("resources/bg.jpg")

eaglerect = eagle1.get_rect()
bg_rect = bg.get_rect()
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



    i=i+1
    image_delay=10
    
    screen.fill(black)
    screen.blit(bg,bg_rect)
    if i<image_delay:
        screen.blit(eagle1, eaglerect)
        pygame.display.flip()
    if (i>image_delay-1 and i<2*image_delay):
        screen.blit(eagle2, eaglerect)
        pygame.display.flip()
    if (i>2*image_delay-1 and i< 3*image_delay):
        screen.blit(eagle3, eaglerect)
        pygame.display.flip()
    if (i>3*image_delay-1 and i<4*image_delay):
        screen.blit(eagle4, eaglerect)
        pygame.display.flip()
        if i==4*image_delay-1:
            i=0