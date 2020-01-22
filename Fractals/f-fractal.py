import pyglet
from math import sin
from math import cos
from math import radians

width = 700
height = 900
window = pyglet.window.Window(width,height,"f")
def whitebackground():
    for i in range(-1,width + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (i, -1, i, height + 1))
        ,("c3B",(255,255,255,255,255,255))
        )

def f(x,y,startsize,angle):
    if startsize < 2:
        return

    x2 = round(startsize * cos(radians(angle)))
    y2 = round(startsize * sin(radians(angle)))

    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (x, y, x + x2, y + y2))
        ,("c3B",(0,0,0,0,0,0))
    )

    f(x + x2, y + y2, round(2/3 * startsize), angle - 90)
    f(x + round(3 * x2/5), y + round(3 * y2/5), round(1/3 * startsize), angle - 90)


@window.event
def on_draw():
    window.clear()
    whitebackground()
    f(100, 100, 700, 90)
    
pyglet.app.run()