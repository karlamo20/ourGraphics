#This code will make a beach with different types of functions

from graphics import *

def draw_puff(pX, pY, pRad, pCol, pWin):
    puff = Circle(Point(pX, pY), pRad)
    puff.setFill(pCol)
    puff.setOutline(pCol)
    puff.draw(pWin)

bchW = 600
bchH = 600

kWin = GraphWin("Beach", bchW, bchH)
kWin.setCoords(0, 0, bchW, bchH)



back = Rectangle(Point(0, 0), Point(bchW, bchH))
back.setFill(color_rgb(254, 205, 159))
back.setOutline(color_rgb(254, 205, 159))
back.draw(kWin)

sun = Circle(Point(300, 350), 150)
sun.setFill(color_rgb(253, 179, 109))
sun.setOutline(color_rgb(253, 179, 109))
sun.draw(kWin)

wSand = Rectangle(Point(0, 0), Point(600, 100))
wSand.setFill(color_rgb(255, 255, 204))
wSand.setOutline(color_rgb(255, 255, 204))
wSand.draw(kWin)

bSand = Rectangle(Point(0, 100), Point(600, 200))
bSand.setFill(color_rgb(194, 178, 128))
bSand.setOutline(color_rgb(194, 178, 128))
bSand.draw(kWin)

ocean = Rectangle(Point(600, 200), Point(0, 400))
ocean.setFill(color_rgb(0, 119, 190))
ocean.setOutline(color_rgb(0, 119, 190))
ocean.draw(kWin)

#clouds

draw_puff(0, 560, 20, "white", kWin)
draw_puff(100, 560, 20, "white", kWin)
draw_puff(100, 570, 20, "white", kWin)
draw_puff(110, 575, 20, "white", kWin)
draw_puff(115, 575, 20, "white", kWin)



kWin.getMouse()
kWin.close()
