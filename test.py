import sys
import sdl2.ext
import time

class Eagle(sdl2.ext.Entity):
    def __init__(self, world, sprite, posx=0, posy=0):
        self.sprite = sprite
        self.sprite.position = posx, posy

RESOURCES = sdl2.ext.Resources(__file__, "resources")
sdl2.ext.init()

window = sdl2.ext.Window("Hello World!", size=(640, 480))
window.show()
factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
spriterenderer = factory.create_sprite_render_system(window)
running = True
i =1
while running:
    if i == 1: 
    	sprite = factory.from_image(RESOURCES.get_path("1.gif"))
    	sprite.position= 500,400
    	spriterenderer.render(sprite)
    	
    	i = i+1 
    	time.sleep(0.1)  
    if i == 2:
    	sprite = factory.from_image(RESOURCES.get_path("2.gif"))
    	sprite.position= 500,400
    	spriterenderer.render(sprite)
    	
    	i= 1   
    	time.sleep(0.1)
    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break
    window.refresh()
