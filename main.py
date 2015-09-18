import sys, pygame
import time
import classes
import random

score=0;
health=1000;
extra=False

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



pygame.init()
size = width, height = 1280, 760
movedown = [0, 20]
moveup = [0, -20]
bush_moveleft = [-18, 0]
bird_moveleft = [-15, 0]
mouse_moveleft = [-13, 0]
mouse1_moveleft = [-13,0]
arrow_moveleft = [-15,0]
newarrow_moveleft = [-15,0]
god_moveleft = [-10,0]
cloud_moveleft = [-10,0]

black = 0, 0, 0

screen = pygame.display.set_mode(size)

eagle0 = pygame.image.load("resources/fly/1.png")
eagle1 = pygame.image.load("resources/fly/2.png")
eagle2 = pygame.image.load("resources/fly/3.png")
eagle3 = pygame.image.load("resources/fly/4.png")
bg = pygame.image.load("resources/bg.jpg")

eagle_walk1 = pygame.image.load("resources/walk/1.png")
eagle_walk2 = pygame.image.load("resources/walk/2.png")

attack_eagle = pygame.image.load("resources/attack_eagle2.gif")

bush0 = pygame.image.load("resources/bush/0.png")
bush1 = pygame.image.load("resources/bush/1.png")
bush2 = pygame.image.load("resources/bush/2.png")
bush3 = pygame.image.load("resources/bush/3.png")


mouse0 = pygame.image.load("resources/mouse/0.gif")
mouse_1 = pygame.image.load("resources/mouse/1.gif")
mouse2 = pygame.image.load("resources/mouse/2.gif")
mouse3 = pygame.image.load("resources/mouse/3.gif")

bird0 = pygame.image.load("resources/bird_food/0.png")
bird1 = pygame.image.load("resources/bird_food/1.png")
bird2 = pygame.image.load("resources/bird_food/2.png")
bird3 = pygame.image.load("resources/bird_food/3.png")

newbird0 = pygame.image.load("resources/bird_food1/0.gif")
newbird1 = pygame.image.load("resources/bird_food1/1.gif")
newbird2 = pygame.image.load("resources/bird_food1/2.gif")
newbird3 = pygame.image.load("resources/bird_food1/3.gif")

arrow0 = pygame.image.load("resources/arrow/arrow.png")
arrow1 = pygame.image.load("resources/arrow/arrow.png")
heart = pygame.image.load("resources/heart/heart.png")
god1 = pygame.image.load("resources/heart/heart.png")
health_img = pygame.image.load("resources/health/health.png")

cloud0 = pygame.image.load("resources/cloud/cloud.png")

go = pygame.image.load("resources/gameover/gameover.jpg")
start = pygame.image.load("resources/start.jpg")

eaglerect = eagle1.get_rect()
eagle_walkrect = eagle1.get_rect()
bgrect = bg.get_rect()
bushrect = bush0.get_rect()
mouserect = mouse0.get_rect()
mouse1rect = mouse0.get_rect()
birdrect = bird0.get_rect()
newbirdrect = newbird0.get_rect()
attack_eaglerect = attack_eagle.get_rect()
arrowrect = arrow0.get_rect()
arrow1rect = arrow1.get_rect()
gorect = go.get_rect()
heartrect = heart.get_rect()
godrect=god1.get_rect()
health_imgrect = health_img.get_rect()
startrect = start.get_rect()
cloudrect = cloud0.get_rect()

bushrect.x = 600
bushrect.y = 579
mouserect.x = 600
mouserect.y = 638
birdrect.x = 600
birdrect.y = 100
eaglerect.y = 50
eagle_walkrect.y = 630
eagle_walkrect.x = 50
arrowrect.y = 250
arrowrect.x = 600
arrow1rect.y= 150
arrow1rect.x = 600
heartrect.y = 0
heartrect.x = 220
health_imgrect.y = 5
health_imgrect.x = 30
cloudrect.y = 200
cloudrect.x = 1280

flying_eagle = classes.character("flying Eagle", screen, eagle0, eagle1, eagle2, eagle3, eaglerect)
walking_eagle = classes.character("walking Eagle", screen, eagle_walk1, eagle_walk2, eagle_walk1, eagle_walk2, eagle_walkrect)
#attacking_eagle = classes.character("attacking Eagle", screen, attack_eagle, attack_eagle, attack_eagle, attack_eagle, eaglerect )
mouse = classes.character("mouse", screen, mouse0, mouse_1, mouse2, mouse3, mouserect)
mouse1 = classes.character("mouse1", screen, mouse0, mouse_1, mouse2, mouse3, mouse1rect)
bush = classes.character("bush", screen, bush0, bush1, bush2, bush3, bushrect)
bird = classes.character("bird", screen, bird0, bird1, bird2, bird3, birdrect)
newbird = classes.character("newbird", screen, newbird0, newbird1, newbird2, newbird3, newbirdrect)
arrow = classes.character("arrow", screen, arrow0, arrow0, arrow0, arrow0, arrowrect)
newarrow= classes.character("arrow", screen, arrow1, arrow1, arrow1, arrow1, arrowrect)
god = classes.character("Life",screen,god1,god1,god1,god1,godrect)
flying_eagle_thread= classes.thread_character("flying eagle", flying_eagle)
walking_eagle_thread= classes.thread_character("walking eagle", walking_eagle)
cloud = classes.character("cloud", screen, cloud0, cloud0, cloud0, cloud0, cloudrect)

#attacking_eagle_thread= classes.thread_character("attacking eagle", attacking_eagle)
god_thread = classes.thread_character("Life",god)
mouse_thread= classes.thread_character("mouse", mouse)
mouse1_thread= classes.thread_character("mouse1", mouse1)
bush_thread= classes.thread_character("bush", bush)
bird_thread = classes.thread_character("bird", bird)
newbird_thread = classes.thread_character("newbird", newbird)
arrow_thread = classes.thread_character("arrow", arrow)
newarrow_thread = classes.thread_character("arrow2", newarrow)
cloud_thread = classes.thread_character("cloud", cloud)

game_name = classes.thread_blit([490,10],screen)
life = classes.thread_blit([260,10],screen)
health_txt = classes.thread_blit([50,10],screen)
score_txt = classes.thread_blit([1000,10],screen)
hit_bush = classes.thread_blit([540,380],screen)
live_lost = classes.thread_blit([540,280],screen)
font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 72)

i=0
firsthit=0
firsthitarrow=0
firsthitnewarrow=0
lives = 3
image_delay=5
while 1:

    screen.blit(start, startrect)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            break


while (lives>0):
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

    #attacking_eagle.imagerect = flying_eagle.imagerect
    bush.velocity(bush_moveleft)
    mouse.velocity(mouse_moveleft)
    mouse1.velocity(mouse1_moveleft)
    bird.velocity(bird_moveleft)
    newbird.velocity(bird_moveleft)
    arrow.velocity(arrow_moveleft)
    newarrow.velocity(newarrow_moveleft)
    cloud.velocity(cloud_moveleft)
    cloud_thread.run(i, image_delay)
    if extra :
        god_thread.run(i,image_delay)
        god.velocity(god_moveleft)
        if flying_eagle.is_attacking(god):
            extra=False
            lives+=1

    
    screen.blit(bg, bgrect)
    screen.blit(heart, heartrect)
    screen.blit(health_img, health_imgrect)

    bush.movement(i, image_delay)
    if flying_eagle.is_attacking(mouse):
        flying_eagle_thread.run(i,image_delay)
        bird_thread.run(i, image_delay)
        newbird_thread.run(i, image_delay)
        arrow_thread.run(i,image_delay)
        newarrow_thread.run(i,image_delay)
        mouse1_thread.run(i,image_delay)
        firsthit = 0
        firsthitarrow = 0
        firsthitnewarrow = 0
        health=min(1000, health+20)
    elif flying_eagle.is_attacking(mouse1):
        flying_eagle_thread.run(i,image_delay)
        bird_thread.run(i, image_delay)
        newbird_thread.run(i, image_delay)
        arrow_thread.run(i,image_delay)
        mouse_thread.run(i,image_delay)
        newarrow_thread.run(i,image_delay)
        firsthit = 0
        firsthitarrow = 0
        firsthitnewarrow = 0
        health=min(1000, health+20)
    elif flying_eagle.is_attacking(bird):
        newbird_thread.run(i, image_delay)
        flying_eagle_thread.run(i,image_delay)
        mouse_thread.run(i, image_delay)
        mouse1_thread.run(i, image_delay)
        newarrow_thread.run(i,image_delay)
        arrow_thread.run(i,image_delay)
        firsthit = 0
        firsthitarrow = 0
        firsthitnewarrow = 0
        health=min(1000,health+40)
    elif flying_eagle.is_attacking(newbird):
        bird_thread.run(i, image_delay)
        flying_eagle_thread.run(i,image_delay)
        mouse_thread.run(i, image_delay)
        mouse1_thread.run(i, image_delay)
        arrow_thread.run(i,image_delay)
        newarrow_thread.run(i,image_delay)
        firsthit = 0
        firsthitarrow = 0
        firsthitnewarrow = 0
        health=min(1000,health+60)
    elif flying_eagle.is_hit(bush):
        text = font.render("HIT BY BUSH", 1, (0, 0, 0))
        hit_bush.run(text)
        time.sleep(0.01)
        newbird_thread.run(i, image_delay)
        mouse1_thread.run(i, image_delay)
        mouse_thread.run(i, image_delay)
        newarrow_thread.run(i,image_delay)
        arrow_thread.run(i,image_delay)
        firsthitnewarrow = 0
        firsthit+=1
        if firsthit==1:
            health=min(1000,health-70)
    elif flying_eagle.is_attacking(arrow):
        flying_eagle_thread.run(i,image_delay)
        bird_thread.run(i, image_delay)
        newbird_thread.run(i, image_delay)
        newarrow_thread.run(i,image_delay)
        mouse1_thread.run(i, image_delay)
        mouse_thread.run(i, image_delay)
        firsthitnewarrow = 0
        firsthitarrow+=1
        if firsthitarrow==1:
            health=min(1000,health-50)
    elif flying_eagle.is_attacking(newarrow):
        flying_eagle_thread.run(i,image_delay)
        bird_thread.run(i, image_delay)
        newbird_thread.run(i, image_delay)
        arrow_thread.run(i,image_delay)
        mouse1_thread.run(i, image_delay)
        mouse_thread.run(i, image_delay)
        firsthitarrow = 0
        firsthitnewarrow+=1
        if firsthitnewarrow==1:
            health=min(1000,health-50)
    elif is_eagle_flying(flying_eagle.imagerect):
        health=health-2
        flying_eagle_thread.run(i,image_delay)
        bird_thread.run(i, image_delay)
        newbird_thread.run(i, image_delay)
        mouse1_thread.run(i, image_delay)
        mouse_thread.run(i, image_delay)
        newarrow_thread.run(i,image_delay)
        arrow_thread.run(i,image_delay)
        firsthit=0
        firsthitnewarrow = 0
        firsthitarrow=0
        score=score+2
    else:
        health=health-1
        bird_thread.run(i, image_delay)
        newbird_thread.run(i, image_delay)
        mouse1_thread.run(i, image_delay)
        mouse_thread.run(i, image_delay)
        newarrow_thread.run(i,image_delay)
        arrow_thread.run(i, image_delay)
        firsthit = 0
        firsthitarrow = 0
        firsthitnewarrow = 0
        score += 1
        walking_eagle_thread.run(i, image_delay)

    if arrow.imagerect.x + arrow.imagerect.width < 0 or flying_eagle.is_attacking(arrow):
        del arrow
        del arrow_thread
        arrow = classes.character("arrow", screen, arrow0, arrow0, arrow0, arrow0, arrowrect)
        arrow_thread = classes.thread_character("arrow", arrow)
        arrow.imagerect.x = 1280
        arrow.imagerect.y = random.randint(50, 650)
        if score<500:
            arrow_moveleft = [-15-random.randint(2,20), 0]
        elif score>=500 and score<1000:
            arrow_moveleft = [-20-random.randint(2,20), 0]
        elif score>=1000 and score<2000:
            arrow_moveleft = [-25-random.randint(2,20), 0]
        elif score>=2000 and score<3000:
            arrow_moveleft = [-35-random.randint(2,20), 0]
        elif score>=3000 and score<5000:
            arrow_moveleft = [-45-random.randint(2,20), 0]
        elif score>=5000 and score<7000:
            arrow_moveleft = [-55-random.randint(2,20), 0]
        elif score>=7000 :
            arrow_moveleft = [-65-random.randint(2,20), 0]        

    if newarrow.imagerect.x + newarrow.imagerect.width < 0 or flying_eagle.is_attacking(newarrow):
        del newarrow
        del newarrow_thread
        newarrow = classes.character("arrow", screen, arrow1, arrow1, arrow1, arrow1, arrow1rect)
        newarrow_thread = classes.thread_character("arrow", newarrow)
        newarrow.imagerect.x = 1280
        newarrow.imagerect.y = random.randint(50, 650)
        if score<500:
            newarrow_moveleft = [-15-random.randint(2,20), 0]
        elif score>=500 and score<1000:
            newarrow_moveleft = [-20-random.randint(2,20), 0]
        elif score>=1000 and score<2000:
            newarrow_moveleft = [-25-random.randint(2,20), 0]
        elif score>=2000 and score<3000:
            newarrow_moveleft = [-35-random.randint(2,20), 0]
        elif score>=3000 and score<5000:
            newarrow_moveleft = [-45-random.randint(2,20), 0]
        elif score>=5000 and score<7000:
            newarrow_moveleft = [-55-random.randint(2,20), 0]
        elif score>=7000 :
            newarrow_moveleft = [-65-random.randint(2,20), 0] 
    if lives==1 :
        extra=True
    if god.imagerect.x + god.imagerect.width < 0 and extra and random.randint(1,1000)>999:
        del god
        del god_thread
        god = classes.character("Life",screen,god1,god1,god1,god1,godrect)
        god_thread = classes.thread_character("Life",god)
        god.imagerect.x = 1280
        god.imagerect.y = random.randint(50, 600)
        god_moveleft = [-5-random.randint(2,10), 0]
    if cloud.imagerect.x + cloud.imagerect.width < 0 and  random.randint(1,1000)>800:
        del cloud_thread
        del cloud
        cloud = classes.character("cloud", screen, cloud0, cloud0, cloud0, cloud0, cloudrect)
        cloud_thread = classes.thread_character("cloud",cloud)
        god.imagerect.x = 1280
        god.imagerect.y = random.randint(50, 200)
        god_moveleft = [-5-random.randint(2,10), 0]
    if bush.imagerect.x + bush.imagerect.width < 0 :
        del bush
        del bush_thread
        bush = classes.character("bush", screen, bush0, bush1, bush2, bush3, bushrect)
        bush_thread= classes.thread_character("bush", bush)
        bush.imagerect.x = 1280
        bush.imagerect.y = 579
        bush_moveleft = [-15-random.randint(2,10), 0]
    if mouse.imagerect.x + mouse.imagerect.width< 0 or flying_eagle.is_attacking(mouse) :
        del mouse
        del mouse_thread
        mouse = classes.character("mouse", screen, mouse0, mouse_1, mouse2, mouse3, mouserect)
        mouse_thread= classes.thread_character("mouse", mouse)
        mouse.imagerect.x = 1280
        mouse.imagerect.y = 630
        mouse_moveleft = [-15-random.randint(2,10), 0]
    if mouse1.imagerect.x + mouse1.imagerect.width< 0 or flying_eagle.is_attacking(mouse1) :
        del mouse1
        del mouse1_thread
        mouse1 = classes.character("mouse1", screen, mouse0, mouse_1, mouse2, mouse3, mouse1rect)
        mouse1_thread= classes.thread_character("mouse1", mouse1)
        mouse1.imagerect.x = 1280
        mouse1.imagerect.y = 630
        mouse1_moveleft = [-20-random.randint(2,10), 0]
    if bird.imagerect.x + bird.imagerect.width < 0 or flying_eagle.is_attacking(bird):
        del bird
        del bird_thread
        bird = classes.character("bird", screen, bird0, bird1, bird2, bird3, birdrect)
        bird_thread = classes.thread_character("bird", bird)
        bird.imagerect.x = 1280
        bird.imagerect.y = random.randint(50, 500)
        bird_moveleft = [-15-random.randint(2,10), 0]
    if newbird.imagerect.x + newbird.imagerect.width < 0 or flying_eagle.is_attacking(newbird):
        del newbird
        del newbird_thread
        newbird = classes.character("newbird", screen, newbird0, newbird1, newbird2, newbird3, newbirdrect)
        newbird_thread = classes.thread_character("newbird", newbird)
        newbird.imagerect.x = 1280
        newbird.imagerect.y = random.randint(50, 500)
        newbird_moveleft = [-15-random.randint(2,10), 0]
    i += 1

    if health < 0:
        health = 1000
        lives -= 1
        text = font1.render("lives X"+str(lives), 1, (0,0,0))
        live_lost.run(text)
        time.sleep(1)
    text = font.render(str(health), 1, (0, 0, 0))
    health_txt.run(text)
    text = font.render(str(lives), 1, (0, 0, 0))
    life.run(text)
    text = font.render("The Eagle", 1, (0, 0, 0))
    game_name.run(text)
    text = font.render("score " + str(score), 1, (0, 0, 0))
    score_txt.run(text)

score_txt = classes.thread_blit([575,50],screen)
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    text = font1.render("score " + str(score), 1, (255, 255, 255))
    score_txt.run(text)
    screen.blit(go, gorect)
    pygame.display.flip()