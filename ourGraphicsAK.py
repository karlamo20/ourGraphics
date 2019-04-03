#This code will make a beach with different types of functions

from graphics import *

##def puff_draw (
    

kWin = GraphWin("Beach", 600, 600)
kWin.setCoords(0, 0, 600, 600)

back = Rectangle(Point(0, 0), Point(600,600))
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

puff = Circle(Point(0,560), 20)
puff.setFill(color_rgb(245, 245, 245))
puff.setOutline(Color_rgb(245, 245, 245))
puff.draw(kWin)





kWin.getMouse()
kWin.close()
