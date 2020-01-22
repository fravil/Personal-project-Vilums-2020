import pyglet
from math import sin
from math import cos
from math import radians


width = 900
height = 900
window = pyglet.window.Window(width,height,"3-zaru-koks")

def whitebackground():
    for i in range(-1,width + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (i, -1, i, height + 1))
        ,("c3B",(255,255,255,255,255,255))
        )

def paparde(x,y,startsize,angle):
    if startsize < 3:
        return

    x2 = round(startsize * cos(radians(angle)))
    y2 = round(startsize * sin(radians(angle)))

    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (x, y, x + x2, y + y2))
        ,("c3B",(0,0,0,0,0,0))
    )

    paparde(x + x2, y + y2, round(1/2 * startsize), angle)
    paparde(x + x2, y + y2, round(1/2 * startsize), angle + 45)
    paparde(x + x2, y + y2, round(1/2 * startsize), angle - 45)

@window.event
def on_draw():
    window.clear()
    whitebackground()
    paparde(int(width/2), 100, 400, 90)
    
pyglet.app.run()