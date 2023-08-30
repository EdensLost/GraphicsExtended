## My personal graphics library which adds less typing needed for objects
# graphicsExtended.py

from graphics import *
import numpy as np


## Draw Line E code:
#
# Draws a line with added color and outline funcitonality for static lines
#
def drawLineE(win, point1, point2, fill = "black"):
    # Instantiates the line at its two points
    line = Line(Point(point1.x, point1.y), Point(point2.x, point2.y))

    # Sets the outline of the line
    line.setFill(fill)

    # Draws the line
    line.draw(win)

    return line
## End DLE

    #----------------------------------------------------------------------

## Draw Rectangle E code:
#
# Draws a rectangle with added color and outline funcitonality for static rectangles
#
def drawRectE(win, point1, point2, fill = "white", outline = "black"):
    # Instantiates the rect at its two points
    rect = Rectangle(Point(point1.x, point1.y), Point(point2.x, point2.y))

    # Sets the outline of the rect
    rect.setFill(fill)

    # Sets the outline of the rect
    rect.setOutline(outline)

    # Draws the rect
    rect.draw(win)

    return rect
## End DRE

    #----------------------------------------------------------------------

## Draw Cir E code:
#
# Draws a circle with added color and outline funcitonality for static circles
#
def drawCirE(win, point, radius, fill = "white", outline = "black"):
    # Instantiates the circle at its two points
    cir = Circle(Point(point.x, point.y), radius)

    # Sets the outline of the circle
    cir.setFill(fill)

    # Sets the outline of the circle
    cir.setOutline(outline)

    # Draws the circle
    cir.draw(win)

    return cir
## End DCE

    #----------------------------------------------------------------------

## Draw Text E code:
#
# Draws a text obj with added color and outline funcitonality
#
def drawTextE(win, point, words, size = 12, fill = "white"):
    # Instantiates the text at its point with the given words
    text = Text(point, words)

    # Sets the size of the text
    text.setSize(size)

    # Sets the outline of the text
    text.setTextColor(fill)

    # Draws the text
    text.draw(win)

    return text
## End DTE

    #----------------------------------------------------------------------

## Draw Text Rect E code:
#
# Draws a text obj and bg with added color and outline funcitonality for static text and a bg
#
def drawTextRectE(win, rectpoint1, rectpoint2, text, textSize = 12, fillRect = "white", fillText = "black", outlineRect = "black"):
    drawRectE(win, rectpoint1, rectpoint2, fillRect, outlineRect)
    textX = (rectpoint1.x + rectpoint2.x) / 2
    textY = (rectpoint1.y + rectpoint2.y) / 2
    textPoint = Point(textX, textY)
    drawTextE(win, textPoint, text, textSize, "white")
## End DTRE

    #----------------------------------------------------------------------

## Draw X code:
#
# Draws an X at the center of a point scaling based on given size
#
def drawX(win, point, size = 1, fill = "black"):
    width = size
    half = width / 2

    # Assigns all of the corners of the x
    tRCorner = Point(point.x + half, point.y + half)
    bRCorner = Point(point.x + half, point.y - half)
    bLCorner = Point(point.x - half, point.y - half)
    tLCorner = Point(point.x - half, point.y + half)

    # Draws the lines of the X
    line1 = Line(tLCorner, bRCorner)
    line1.setFill(fill)
    line1.draw(win)
    line2 = Line(tRCorner, bLCorner)
    line2.setFill(fill)
    line2.draw(win)
## End DX

    #----------------------------------------------------------------------

## Rando RGB code:
#
# Gives a random color code
#
## To Fix: nothing
#
def randoRGB():
    return color_rgb(np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
## End RRGB

    #----------------------------------------------------------------------

## {Name} code:
#
# {Description}
#
#def {name}():
    

## End {Abbriviation}

    #----------------------------------------------------------------------
