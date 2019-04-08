#ourGraphics.py w/ Karla and Aziza

from graphics import *

kWin = GraphWin("Beach", 600, 600)
kWin.setCoords(0, 0, 600, 600)

back = Rectangle(Point(0, 0), Point(600,600))
back.setFill(color_rgb(254, 205, 159))
back.draw(kWin)

sun = Circle(Point(300, 350), 150)
sun.setFill(color_rgb(253, 179, 109))
sun.draw(kWin)

wSand = Rectangle(Point(0, 0), Point(600, 100))
wSand.setFill(color_rgb(255, 255, 204))
wSand.draw(kWin)

bSand = Rectangle(Point(0, 100), Point(600, 200))
bSand.setFill(color_rgb(194, 178, 128))
bSand.draw(kWin)

ocean = Rectangle(Point(600, 200), Point(0, 400))
ocean.setFill(color_rgb(0, 119, 190))
ocean.draw(kWin)

#beginning UMBRELLA branch

blanket = Rectangle(Point(410, 45), Point(500, 10))
blanket.setFill(color_rgb(162, 200, 162))
blanket.setOutline(color_rgb(162, 200, 162))
blanket.draw(kWin)

stick = Rectangle(Point(450, 20), Point(460, 80))
stick.setFill(color_rgb(169, 169, 169))
stick.setOutline(color_rgb(169, 169, 169))
stick.draw(kWin)

pluie = Polygon(Point(410, 70), Point(500, 70), Point(455, 130))
pluie.setFill(color_rgb(200, 162, 200))
pluie.setOutline(color_rgb(200, 162, 200))
pluie.draw(kWin)
