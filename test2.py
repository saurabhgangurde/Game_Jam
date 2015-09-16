import pygame, OpenGL, math, numpy
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from PIL import Image #have Pillow instead of PIL

img = Image.open('1.png')
img_data = numpy.array(list(img.getdata()), numpy.int8)
im = glGenTextures(1,img)
glPixelStorei(GL_UNPACK_ALIGNMENT,4)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
glTexImage2D(GL_TEXTURE_2D, 5, GL_RGB, img.size[0], img.size[1], 0, GL_RGB, GL_UNSIGNED_BYTE, img_data)
gluBuild2DMipmaps( GL_TEXTURE_2D, 3, img.size[0], img.size[1], GL_RGB, GL_UNSIGNED_BYTE, img_data );
def wall(image): #I would like the image on this wall
    glColor((1,0,0))
    glBindTexture(GL_TEXTURE_2D,image) 
    glBegin(GL_QUADS)
    glTexCoord2f(0,0)
    glVertex3f(-4,-4,-8)
    glTexCoord2f(1,0)
    glVertex3f(-4,4,-8)
    glTexCoord2f(1,1)
    glVertex3f(4,4,-8)
    glTexCoord2f(0,1)
    glVertex3f(4,-4,-8)
    glEnd()

def main():
    pygame.init()
    display = (600,600)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    glLoadIdentity()
    gluPerspective(45, 1, 0.05, 100)
    glEnable(GL_TEXTURE_2D)

    glTranslatef(0,0,-5)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    wall(im)

    pygame.display.flip()
    pygame.time.wait(50)