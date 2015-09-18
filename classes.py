import pygame, sys
import math
import random
import threading

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)


class character(object):
    def __init__(self, name, screen, image0, image1, image2, image3, imagerect):
        self.name = name
        self.screen = screen
        self.image0 = image0
        self.image1 = image1
        self.image2 = image2
        self.image3 = image3
        self.imagerect = imagerect

    def movement(self, t, image_delay):
        i = t % (4*image_delay)
        if i<image_delay:
            self.screen.blit(self.image0, self.imagerect)
            pygame.display.flip()
        elif i>image_delay-1 and i<2*image_delay:
            self.screen.blit(self.image1, self.imagerect)
            pygame.display.flip()
        elif i>2*image_delay-1 and i< 3*image_delay:
            self.screen.blit(self.image2, self.imagerect)
            pygame.display.flip()
        elif i>3*image_delay-1 and i<4*image_delay:
            self.screen.blit(self.image3, self.imagerect)
            pygame.display.flip()


    def velocity(self, velocity):
        self.imagerect = self.imagerect.move(velocity)

    def is_on_screen(self):
        if self.imagerect.centerx + self.imagerect.width/2<1280 and self.imagerect.centerx -self.imagerect.width/2>0:
            return True
        else:
            return False

    def is_attacking(self, objectarray):
        if self.imagerect.x+self.imagerect.width >= objectarray.imagerect.x and self.imagerect.y+self.imagerect.height >= objectarray.imagerect.y and self.imagerect.y <= objectarray.imagerect.y + objectarray.imagerect.height:
            return True
        else:
            return False

    def is_hit(self, objectarray):
        if self.imagerect.x+self.imagerect.width >= objectarray.imagerect.x and self.imagerect.y+self.imagerect.height >= objectarray.imagerect.y and self.imagerect.y <= objectarray.imagerect.y + objectarray.imagerect.height:
            return True
        else:
            return False

class thread_character(threading.Thread):
    def __init__(self, name, character_object):
        threading.Thread.__init__(self)
        self.name = name
        self.character_object = character_object

    def run(self, t, image_delay):
        movement(self.character_object, t, image_delay)


def movement(character_object, t , image_delay):
    character_object.movement(t, image_delay)


class thread_blit(threading.Thread):
    def __init__(self,textpos, screen):
        threading.Thread.__init__(self)
        self.textpos = textpos
        self.screen = screen

    def run(self, text):
        self.screen.blit(text, self.textpos)
        pygame.display.update()



