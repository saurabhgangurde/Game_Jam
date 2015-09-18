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
movedown = [0, 20]
moveup = [0, -20]
bush_moveleft = [-18, 0]
bird_moveleft = [-15, 0]
mouse_moveleft = [-13, 0]
arrow_moveleft = [-20,0]

black = 0, 0, 0

screen = pygame.display.set_mode(size)

eagle0 = pygame.image.load("resources/fly/1.png")
eagle1 = pygame.image.load("resources/fly/2.png")
eagle2 = pygame.image.load("resources/fly/3.png")
eagle3 = pygame.image.load("resources/fly/4.png")
bg = pygame.image.load("resources/bg.jpg")

eagle_walk1 = pygame.image.load("resources/walk/walk1.jpg")
eagle_walk2 = pygame.image.load("resources/walk/walk2.jpg")

attack_eagle = pygame.image.load("resources/attack_eagle2.gif")

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
heart = pygame.image.load("resources/heart/heart.png")
health_img = pygame.image.load("resources/health/health.png")

go = pygame.image.load("resources/gameover/gameover.jpg")
start = pygame.image.load("resources/start.jpg")

eaglerect = eagle1.get_rect()
eagle_walkrect = eagle1.get_rect()
bgrect = bg.get_rect()
bushrect = bush0.get_rect()
mouserect = mouse0.get_rect()
birdrect = bird0.get_rect()
attack_eaglerect = attack_eagle.get_rect()
arrowrect = arrow0.get_rect()
gorect = go.get_rect()
heartrect = heart.get_rect()
health_imgrect = health_img.get_rect()
startrect = start.get_rect()

bushrect.x = 600
bushrect.y = 579
mouserect.x = 600
mouserect.y = 638
birdrect.x = 600
birdrect.y = 100
eaglerect.y = 50
eagle_walkrect.y = 600
eagle_walkrect.x = 50
arrowrect.y = 250
arrowrect.x = 600
heartrect.y = 0
heartrect.x = 220
health_imgrect.y = 5
health_imgrect.x = 30

flying_eagle = classes.character("flying Eagle", screen, eagle0, eagle1, eagle2, eagle3, eaglerect)
walking_eagle = classes.character("walking Eagle", screen, eagle_walk1, eagle_walk2, eagle_walk1, eagle_walk2, eagle_walkrect)
attacking_eagle = classes.character("attacking Eagle", screen, attack_eagle, attack_eagle, attack_eagle, attack_eagle, eaglerect )
mouse = classes.character("mouse", screen, mouse0, mouse1, mouse2, mouse3, mouserect)
bush = classes.character("bush", screen, bush0, bush1, bush2, bush3, bushrect)
bird = classes.character("bird", screen, bird0, bird1, bird2, bird3, birdrect)
arrow = classes.character("arrow", screen, arrow0, arrow0, arrow0, arrow0, arrowrect)

flying_eagle_thread= classes.thread_character("flying eagle", flying_eagle)
walking_eagle_thread= classes.thread_character("walking eagle", walking_eagle)
attacking_eagle_thread= classes.thread_character("attacking eagle", attacking_eagle)
mouse_thread= classes.thread_character("mouse", mouse)
bush_thread= classes.thread_character("bush", bush)
bird_thread = classes.thread_character("bird", bird)
arrow_thread = classes.thread_character("arrow", arrow)


game_name = classes.thread_blit([490,10],screen)
life = classes.thread_blit([260,10],screen)
health_txt = classes.thread_blit([50,10],screen)
score_txt = classes.thread_blit([1000,10],screen)
font = pygame.font.Font(None, 36)

i=0
firsthit=0
firsthitarrow=0
lives = 3
while 1:

    screen.blit(start, startrect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            break


while (lives>0):
    print health
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if flying_eagle.imagerect.centery >= 50+(eaglerect.height/2):
                flying_eagle.imagerect = flying_eagle.imagerect.move(moveup)

        if event.key == pygame.K_DOWN:
            if flying_eagle.imagerect.centery <= 760-(flying_eagle.imagerect.height/2):
                flying_eagle.imagerect = flying_eagle.imagerect.move(movedown)
        if event.key == pygame.K_ESCAPE:
            lives = 0

    attacking_eagle.imagerect = flying_eagle.imagerect
    bush.velocity(bush_moveleft)
    mouse.velocity(mouse_moveleft)
    bird.velocity(bird_moveleft)
    arrow.velocity(arrow_moveleft)

    image_delay=5
    screen.blit(bg, bgrect)
    screen.blit(heart, heartrect)
    screen.blit(health_img, health_imgrect)

    bush.movement(i, image_delay)
    if flying_eagle.is_attacking(mouse):
        attacking_eagle_thread.run(i,image_delay)
        bird_thread.run(i, image_delay)
        arrow_thread.run(i,image_delay)
        firsthit = 0
        firsthitarrow = 0
        health=min(1000, health+50)
        print "attacking mouse"
    elif flying_eagle.is_attacking(bird):
        attacking_eagle_thread.run(i,image_delay)
        mouse_thread.run(i, image_delay)
        arrow_thread.run(i,image_delay)
        firsthit = 0
        firsthitarrow = 0
        health=min(1000,health+85)
        print "attacking bird"
    elif flying_eagle.is_hit(bush):
        attacking_eagle_thread.run(i,image_delay)
        bird_thread.run(i, image_delay)
        mouse_thread.run(i, image_delay)
        arrow_thread.run(i,image_delay)
        print "hit"
        firsthit+=1
        if firsthit==1:
            health=min(1000,health-70)
    elif flying_eagle.is_attacking(arrow):
        attacking_eagle_thread.run(i,image_delay)
        bird_thread.run(i, image_delay)
        mouse_thread.run(i, image_delay)
        print "hit by arrow"
        firsthitarrow+=1
        if firsthitarrow==1:
            health=min(1000,health-50)
    elif is_eagle_flying(flying_eagle.imagerect):
        health=health-2
        flying_eagle_thread.run(i,image_delay)
        bird_thread.run(i, image_delay)
        mouse_thread.run(i, image_delay)
        arrow_thread.run(i,image_delay)
        firsthit=0
        firsthitarrow=0
        print "flying"
        print score
        score=score+2
    else:
        print " walking"
        health=health-1
        bird_thread.run(i, image_delay)
        mouse_thread.run(i, image_delay)
        arrow_thread.run(i, image_delay)
        firsthit = 0
        firsthitarrow = 0
        print score
        score += 1
        walking_eagle_thread.run(i, image_delay)

    if arrow.imagerect.x + arrow.imagerect.width < 0 or flying_eagle.is_attacking(arrow):
        del arrow
        del arrow_thread
        arrow = classes.character("arrow", screen, arrow0, arrow0, arrow0, arrow0, arrowrect)
        arrow_thread = classes.thread_character("arrow", arrow)
        arrow.imagerect.x = 1280
        arrow.imagerect.y = random.randint(50, 500)

    if bush.imagerect.x + bush.imagerect.width < 0 :
        del bush
        del bush_thread
        bush = classes.character("bush", screen, bush0, bush1, bush2, bush3, bushrect)
        bush_thread= classes.thread_character("bush", bush)
        bush.imagerect.x = 1280
        bush.imagerect.y = 579
    if mouse.imagerect.x + mouse.imagerect.width< 0 or flying_eagle.is_attacking(mouse) :
        del mouse
        del mouse_thread
        mouse = classes.character("mouse", screen, mouse0, mouse1, mouse2, mouse3, mouserect)
        mouse_thread= classes.thread_character("mouse", mouse)
        mouse.imagerect.x = 1280
        mouse.imagerect.y = 630
    if bird.imagerect.x + bird.imagerect.width < 0 or flying_eagle.is_attacking(bird):
        del bird
        del bird_thread
        bird = classes.character("bird", screen, bird0, bird1, bird2, bird3, birdrect)
        bird_thread = classes.thread_character("bird", bird)
        bird.imagerect.x = 1280
        bird.imagerect.y = random.randint(50, 500)
    i += 1

    if health < 0:
        health = 1000
        lives -= 1
    text = font.render(str(health), 1, (0, 0, 0))
    health_txt.run(text)
    text = font.render( str(lives), 1, (0, 0, 0))
    life.run(text)
    text = font.render("The Eagle", 1, (0, 0, 0))
    game_name.run(text)
    text = font.render("score " + str(score), 1, (0, 0, 0))
    score_txt.run(text)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.blit(go, gorect)
    pygame.display.flip()

print "Game Over"