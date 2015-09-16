import sys
import sdl2.ext
import time

class Eagle(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=0, posy=0):
        self.sprite = sprite
        self.sprite.position = posx, posy

RESOURCES = sdl2.ext.Resources(__file__, "resources")
sdl2.ext.init()

window = sdl2.ext.Window("Eagle Warrior", size=(900, 760))
window.show()
factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
spriterenderer = factory.create_sprite_render_system(window)
running = True
i =1
posx=500
posy=200
while running:
    if i == 1: 
    	world = sdl2.ext.World()
    	sprite = factory.from_image(RESOURCES.get_path("1.gif"))
    	Eagle1 = Eagle(world, sprite,posx,posy)
    	window.refresh()
    	spriterenderer.render(sprite)	
    	i = i+1
    	posx = posx+1
    	posy = posy+1
    	print "1" 
    	time.sleep(0.1)  
    if i == 2:
    	world = sdl2.ext.World()
    	sprite = factory.from_image(RESOURCES.get_path("2.gif"))
    	Eagle2 = Eagle(world, sprite,posx,posy)
    	window.refresh()
    	spriterenderer.render(sprite)
    	posx = posx+1
    	posy = posy+1 
    	print "2"
    	i= i+1   
    	time.sleep(0.1)
    if i == 3: 
    	world = sdl2.ext.World()
    	sprite = factory.from_image(RESOURCES.get_path("3.gif"))
    	Eagle1 = Eagle(world, sprite,posx,posy)
    	window.refresh()
    	spriterenderer.render(sprite)	
    	i = i+1
    	posx = posx+1
    	posy = posy+1 
    	print "3"
    	time.sleep(0.1)  
    if i == 4:
    	world = sdl2.ext.World()
    	sprite = factory.from_image(RESOURCES.get_path("4.gif"))
    	Eagle2 = Eagle(world, sprite,posx,posy)
    	window.refresh()
    	spriterenderer.render(sprite)
    	posx = posx+1
    	posy = posy+1 
    	i= 1   
    	print "4"
    	time.sleep(0.1)

    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break
    window.refresh()
