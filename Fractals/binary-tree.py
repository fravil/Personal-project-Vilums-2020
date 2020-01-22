import pyglet
from math import sin
from math import cos
from math import radians

width = 900
height = 900
window = pyglet.window.Window(width,height,"koks")

def whitebackground():
    for i in range(-1,width + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (i, -1, i, height + 1))
        ,("c3B",(255,255,255,255,255,255))
        )

def tree(x,y,startsize,angle):
    if startsize < 2:
        return

    x2 = round(startsize * cos(radians(angle)))
    y2 = round(startsize * sin(radians(angle)))

    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (x, y, x + x2, y + y2))
        ,("c3B",(0,0,0,0,0,0))
    )

    tree(x + x2, y + y2, round(2/3 * startsize), angle + 30)
    tree(x + x2, y + y2, round(2/3 * startsize), angle - 30)


@window.event
def on_draw():
    window.clear()
    whitebackground()
    tree(int(width/2), 100, 250, 90)
    
pyglet.app.run()