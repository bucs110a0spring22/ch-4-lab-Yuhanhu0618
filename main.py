import turtle
import math

########### Your Code here ##############
##default size is 400 wide 300 high
def drawSineCurve(t):

  for angle in range(360):
    y = math.sin(math.radians(angle))
    t.goto(angle,100 * y) 


def drawCosineCurve(t):
  t.up()
  t.goto(-360, math.cos(-360))
  t.down()
  for i in range(721):
    t.goto(i-360, math.cos(i-360))
  t.up()

def drawTangentCurve(t):
  t.up()
  t.goto(-360, math.tan(-360))
  t.down()
  for i in range(721):
    t.goto(i-360, math.tan(i-360))
  t.up()

def setupWindow(screen):
  screen.screensize()

def setupAxis(t):
  width = turtle.screensize()[0]/2
  height = turtle.screensize()[1]/2
  t.up()
  t.goto(-width, 0)
  t.down()
  t.goto(width, 0)
  t.up()
  t.goto(0, height)
  t.down()
  t.goto(0, -height)
  t.up()

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    wn.setworldcoordinates(-10, -2, 20, 2)
    dart = turtle.Turtle()
    dart.speed(0)
    drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()