#This code will make a beach with different types of functions

from graphics import *

def draw_puff(pX, pY, pRad, pCol, pWin): #function for clouds
    puff = Circle(Point(pX, pY), pRad)
    puff.setFill(pCol)
    puff.setOutline(pCol)
    puff.draw(pWin)

#def draw_bird

bchW = 600
bchH = 600

kWin = GraphWin("Beach", bchW, bchH)
kWin.setCoords(0, 0, bchW, bchH)

#the whole background of the beach
back = Rectangle(Point(0, 0), Point(bchW, bchH))
back.setFill(color_rgb(254, 205, 159))
back.setOutline(color_rgb(254, 205, 159))
back.draw(kWin)

#first layer of sun
sun = Circle(Point(300, 250), 275)
sun.setFill(color_rgb(253,137,83))
sun.setOutline(color_rgb(253, 179, 109))
sun.draw(kWin)

#the center of the sun
sun = Circle(Point(300, 300), 200)
sun.setFill(color_rgb(253, 179, 109))
sun.setOutline(color_rgb(253, 179, 109))
sun.draw(kWin)

#first layer of the sand not touching water
wSand = Rectangle(Point(0, 0), Point(600, 100))
wSand.setFill(color_rgb(255, 255, 204))
wSand.setOutline(color_rgb(255, 255, 204))
wSand.draw(kWin)

#second layer of sand touching the water
bSand = Rectangle(Point(0, 100), Point(600, 200))
bSand.setFill(color_rgb(194, 178, 128))
bSand.setOutline(color_rgb(194, 178, 128))
bSand.draw(kWin)

#the ocean
ocean = Rectangle(Point(600, 200), Point(0, 400))
ocean.setFill(color_rgb(0, 119, 190))
ocean.setOutline(color_rgb(0, 119, 190))
ocean.draw(kWin)

#cloud
draw_puff(0, 570, 20, "white", kWin) #top layer pf clouds 
draw_puff(30, 575, 20, "white", kWin)
draw_puff(60, 570, 20, "white", kWin)
draw_puff(90, 575, 20, "white", kWin)
draw_puff(120, 570, 20, "white", kWin)
draw_puff(150, 560, 20, "white", kWin)
draw_puff(160, 540, 20, "white", kWin)
draw_puff(150, 520, 20, "white", kWin)
draw_puff(0, 520, 20, "white", kWin) # begining of bottom clouds 
draw_puff(30, 510, 20, "white", kWin)
draw_puff(60, 515, 20, "white", kWin)
draw_puff(90, 510, 20, "white", kWin)
draw_puff(120, 520, 20, "white", kWin)
draw_puff(10, 555, 20, "white", kWin) #filling of inside of cloud
draw_puff(30, 540, 20, "white", kWin)
draw_puff(50, 540, 20, "white", kWin)
draw_puff(60, 540, 20, "white", kWin)
draw_puff(70, 540, 20, "white", kWin)
draw_puff(80, 540, 20, "white", kWin)
draw_puff(90, 540, 20, "white", kWin)
draw_puff(120, 540, 20, "white", kWin)
draw_puff(90, 545, 20, "white", kWin)
#end of cloud

kWin.getMouse()
kWin.close()
