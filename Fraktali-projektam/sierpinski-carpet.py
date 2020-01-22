import pyglet

width = 829
height = 829
window = pyglet.window.Window(width,height,"square")

def whitebackground():
    for i in range(-1,width + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (i, -1, i, height + 1))
        ,("c3B",(255,255,255,255,255,255))
        )

def frame(edgelength, bottomcornerx, bottomcornery): #nesvarīgs, tikai arējam rāmim
    if edgelength < 3:
        return

    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (bottomcornerx, bottomcornery - 1, bottomcornerx, bottomcornery + edgelength))
        ,("c3B",(0,0,0,0,0,0))
    )
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (bottomcornerx, bottomcornery, bottomcornerx + edgelength, bottomcornery))
        ,("c3B",(0,0,0,0,0,0))
    )
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (bottomcornerx + edgelength, bottomcornery, bottomcornerx + edgelength, bottomcornery + edgelength))
        ,("c3B",(0,0,0,0,0,0))
    )
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (bottomcornerx, bottomcornery + edgelength, bottomcornerx + edgelength, bottomcornery + edgelength))
        ,("c3B",(0,0,0,0,0,0))
    )

def carpet(edgelength, bottomcornerx, bottomcornery):
    if edgelength < 3:
        return

    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (bottomcornerx, bottomcornery - 1, bottomcornerx, bottomcornery + edgelength))
        ,("c3B",(0,0,0,0,0,0))
    )
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (bottomcornerx, bottomcornery, bottomcornerx + edgelength, bottomcornery))
        ,("c3B",(0,0,0,0,0,0))
    )
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (bottomcornerx + edgelength, bottomcornery, bottomcornerx + edgelength, bottomcornery + edgelength))
        ,("c3B",(0,0,0,0,0,0))
    )
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (bottomcornerx, bottomcornery + edgelength, bottomcornerx + edgelength, bottomcornery + edgelength))
        ,("c3B",(0,0,0,0,0,0))
    )

    carpet(int(round(edgelength/3)),bottomcornerx - int(round(2 * edgelength/3)), bottomcornery + int(round(edgelength/3)))
    carpet(int(round(edgelength/3)),bottomcornerx - int(round(2 * edgelength/3)), bottomcornery + int(round(4 * edgelength/3)))
    carpet(int(round(edgelength/3)),bottomcornerx - int(round(2 * edgelength/3)), bottomcornery - int(round(2 * edgelength/3)))

    carpet(int(round(edgelength/3)),bottomcornerx + int(round(edgelength/3)), bottomcornery + int(round(4 * edgelength/3)))
    carpet(int(round(edgelength/3)),bottomcornerx + int(round(edgelength/3)), bottomcornery - int(round(2 * edgelength/3)))

    carpet(int(round(edgelength/3)),bottomcornerx + int(round(4 * edgelength/3)), bottomcornery + int(round(edgelength/3)))
    carpet(int(round(edgelength/3)),bottomcornerx + int(round(4 * edgelength/3)), bottomcornery + int(round(4 * edgelength/3)))
    carpet(int(round(edgelength/3)),bottomcornerx + int(round(4 * edgelength/3)), bottomcornery - int(round(2 * edgelength/3)))
    




@window.event
def on_draw():
    window.clear()
    whitebackground()
    frame(width - 100,50,50)
    carpet(int(round((width-100)/3)),int(round((width-100)/3)) + 50,int(round((width-100)/3)) + 50)

pyglet.app.run()