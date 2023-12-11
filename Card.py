from graphics import *

win = GraphWin("Holidays!", 600, 400)

background = Rectangle(Point(0, 400), Point(600, 400))
win.setBackground("red")
background.draw(win)

ground = Polygon(Point(0, 400), Point(0, 340), Point(600, 340), Point(600, 400))
ground.setFill("white")
ground.draw(win)

trunk = Rectangle(Point(280, 300), Point(320, 375))
trunk.setFill("saddlebrown")
trunk.draw(win)

tree3 = Polygon(Point(300, 150), Point(200, 300), Point(400, 300))
tree3.setFill("green")
tree3.draw(win)

treemid = Polygon(Point(300, 100), Point(225, 225), Point(375, 225))
treemid.setFill("green")
treemid.draw(win)

treetop = Polygon(Point(300, 50), Point(250, 150), Point(350, 150))
treetop.setFill("green")
treetop.draw(win)

star = Polygon(Point(300, 40), Point(295, 50), Point(305, 50))
star.setFill("yellow")
star.draw(win)

greeting = Text(Point(300, 100), "Happy Holidays!")
greeting.setSize(35)
greeting.setTextColor("lightblue")
greeting.draw(win)
