import sys
import sdl2.ext

RESOURCES = sdl2.ext.Resources(__file__, "resources")
sdl2.ext.init()

window = sdl2.ext.Window("Hello World!", size=(640, 480))
window.show()
factory = sdl2.ext.SpriteFactory(sdl2.ext.SOFTWARE)
running = True
i =1
while running:
    if i == 1: 
    	sprite = factory.from_image(RESOURCES.get_path("1.jpg"))
    	spriterenderer = factory.create_sprite_render_system(window)
    	spriterenderer.render(sprite)
    	i = i+1   
    if i == 2:
    	sprite = factory.from_image(RESOURCES.get_path("2.jpg"))
    	spriterenderer = factory.create_sprite_render_system(window)
    	spriterenderer.render(sprite)
    	i= 1   

    events = sdl2.ext.get_events()
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break
    window.refresh()
