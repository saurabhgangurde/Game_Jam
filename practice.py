import sys, pygame
import time
pygame.init()
size = width, height = 1280, 760
speed = [10, 0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball1 = pygame.image.load("3.gif")
ball2 = pygame.image.load("4.gif")
ballrect1 = ball1.get_rect()
ballrect2 = ball2.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect1 = ballrect1.move(speed)
    ballrect2 = ballrect2.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball1, ballrect1)
    time.sleep(0.1)
    pygame.display.flip()
    screen.blit(ball2, ballrect2)
    time.sleep(0.1)
    pygame.display.flip()