import pyglet #library that allows me to draw
width = 1000
height = 1000
window = pyglet.window.Window(width,height,"vicsek") #Draws the window

centerx = int(round(width/2))
centery = int(round(height/2)) #Calculate the centre of the window 

def whitebackground(): #This makes a white background
    for i in range(-1,width + 1):
        pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (i, -1, i, height + 1))
        ,("c3B",(255,255,255,255,255,255))
        )


def vicsek(startsize, x, y):
    if startsize < 3:
        return #This part stops the program if the cross is too small

    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (x - int(round(startsize/2)), y, x + int(round(startsize/2)) - 1, y))
        ,("c3B",(0,0,0,0,0,0))
    )
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (x, y - int(round(startsize/2)), x, y + int(round(startsize/2)) - 1))
        ,("c3B",(0,0,0,0,0,0))
    ) #These two draw the cross
    vicsek(int(round(startsize/3)), x + int(round((1/3)*startsize)), y)
    vicsek(int(round(startsize/3)), x - int(round((1/3)*startsize)), y)
    vicsek(int(round(startsize/3)), x, y + int(round((1/3)*startsize)))
    vicsek(int(round(startsize/3)), x, y - int(round((1/3)*startsize)))
    vicsek(int(round(startsize/3)), x, y) #These draw 5 smaller crosses on the corners and center of the cross.
    #on each of the smaller crosses 5 even smaller crosses until the crosses are 3 pixels large, at which point it stops the program

@window.event
def on_draw(): #tells what to draw
    window.clear()
    whitebackground() #Draws the white background
    vicsek(width - 50, centerx, centery) #draws the cross itself
    
pyglet.app.run()