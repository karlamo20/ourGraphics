
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

#clouds

cloud = Circle(Point(100,560), 20)
cloud.setFill(color_rgb(245, 245, 245))
cloud.draw(kWin)

clouds = Circle(Point(100,570), 20)
clouds.setFill(color_rgb(245, 245, 245))
clouds.draw(kWin)

cloudss = Circle(Point(110, 575), 20)
cloudss.setFill(color_rgb(245, 245, 245))
cloudss.draw(kWin)

cloudsss = Circle(Point(115, 575), 20)
cloudsss.setFill(color_rgb(245, 245, 245))
cloudsss.draw(kWin)

kWin.getMouse()
kWin.close()
