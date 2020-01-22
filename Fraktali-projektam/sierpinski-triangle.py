import pyglet
from math import sqrt
width = 1000
height = 1000
window = pyglet.window.Window(width,height,"sierpinski")

def whitebackground():
    for i in range(-1,width + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (i, -1, i, height + 1))
        ,("c3B",(255,255,255,255,255,255))
        )

def triangle(x, y, len):
    centr = x + int(round(len/2))
    triangheight = int(round((len)*(sqrt(3)/2)) + 1)

    if (len < 3):
        return

    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (x, y, x + len + 1, y))
        ,("c3B",(0,0,0,0,0,0))
    )
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (x, y, centr, y + triangheight))
        ,("c3B",(0,0,0,0,0,0))
    )
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (centr, y + triangheight, x + len, y))
        ,("c3B",(0,0,0,0,0,0))
    )

    newlen = int(round(len/2))
    newheight = int(round(triangheight/2))

    triangle(x, y, newlen)
    triangle(x + newlen, y, newlen)
    triangle(x + int(round(newlen/2)), y + newheight, newlen)


@window.event
def on_draw():
    window.clear()
    whitebackground()
    triangle(5, 100, width - 20)
    
pyglet.app.run()