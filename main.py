import turtle
import math

########### Your Code here #############
def drawSineCurve(turtle=None):
  for xValue in range(720):
    yValue = math.sin(math.radians(xValue-360))
    turtle.goto(xValue-360, yValue)
    turtle.down()
  turtle.up()

def drawCosineCurve(turtle=None):
  for xValue in range(720):
    yValue = math.cos(math.radians(xValue-360))
    turtle.goto(xValue-360, yValue) 
    turtle.down()
  turtle.up()

def drawTangentCurve(turtle=None):
  for xValue in range(720):
    if (xValue % 90 != 0):
      yValue = math.tan(math.radians(xValue-360))
      turtle.goto(xValue-360, yValue)
      turtle.down()
    else:
      turtle.up()
  turtle.up()

def setupWindow(wn=None):
  wn.setworldcoordinates(-360, -2, 360, 2)

def setupAxis(turtle=None):
  turtle.goto(0, -2)
  turtle.down()
  turtle.goto(0, 2)
  turtle.up()
  turtle.goto(360, 0)
  turtle.down()
  turtle.goto(-360, 0)
  turtle.up()

##########  Do Not Alter Any Code Past Here ########
def main():
    #Part A
    wn = turtle.Screen()
    wn.tracer(5)
    wn.setworldcoordinates(-10, -2, 20, 2)
    dart = turtle.Turtle()
    dart.speed(0)
    #drawSineCurve(dart)

    #Part B
    setupWindow(wn)
    setupAxis(dart)
    dart.speed(0)
    drawSineCurve(dart)
    drawCosineCurve(dart)
    drawTangentCurve(dart)
    wn.exitonclick()
main()