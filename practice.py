import sys, pygame
import time
pygame.init()
size = width, height = 1280, 760
speed = [10, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

eagle1 = pygame.image.load("resources/1.gif")
eagle2 = pygame.image.load("resources/2.gif")
eagle3 = pygame.image.load("resources/3.gif")
eagle4 = pygame.image.load("resources/4.gif")


eaglerect = eagle1.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    eaglerect = eaglerect.move(speed)
    


    screen.fill(black)
    screen.blit(eagle1, eaglerect)
    time.sleep(0.1)
    pygame.display.flip()
    screen.blit(eagle2, eaglerect)
    time.sleep(0.1)
    pygame.display.flip()
    screen.blit(eagle3, eaglerect)
    time.sleep(0.1)
    pygame.display.flip()
    screen.blit(eagle4, eaglerect)
    time.sleep(0.1)
    pygame.display.flip()