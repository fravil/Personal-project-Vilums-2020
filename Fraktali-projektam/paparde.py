import pyglet
from math import sin
from math import cos
from math import radians
from math import floor

width = 900
height = 900
window = pyglet.window.Window(width,height,"paparde")

def whitebackground():
    for i in range(-1,width + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (i, -1, i, height + 1))
        ,("c3B",(255,255,255,255,255,255))
        )

def paparde(x,y,startsize,angle):
    if startsize <= 1:
        return

    x2 = round(startsize * cos(radians(angle)))
    y2 = round(startsize * sin(radians(angle)))

    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (x, y, x + x2, y + y2))
        ,("c3B",(0,0,0,0,0,0))
    )

    paparde(x + x2, y + y2, floor(4/5 * startsize), angle - 12)
    paparde(x + round(3 * x2/5), y + round(3 * y2/5), floor(3/7 * startsize), angle - 12 + 60)
    paparde(x + round(4 * x2/5), y + round(4 * y2/5), floor(3/7 * startsize), angle - 12 - 25)

@window.event
def on_draw():
    window.clear()
    whitebackground()
    paparde(int(width/3), 60, 200, 90)
    
pyglet.app.run()