## My personal graphics library which adds less typing needed for objects
# graphicsExtended.py



from graphics import *
import random as rando


## Draw Win E code:
#
# Draws a window with added coordinates
#
def drawWindowE(title = "window", width = 200, height = 200, cordXMax = 100, cordYMax = 100, colorBG = "white"):
    # Instantiates the window
    win = GraphWin(title, width, height)

    # Sets the coordinates of the window
    win.setCoords(0.0, 0.0, cordXMax, cordYMax)

    # Sets the background of the window
    win.setBackground(colorBG)

    return win
## End DWE

    #----------------------------------------------------------------------

## Draw Line E code:
#
# Draws a line with added color and outline funcitonality for lines
#
def drawLineE(win, point1, point2, fill = "black"):
    # Instantiates the line at its two points
    line = Line(Point(point1.x, point1.y), Point(point2.x, point2.y))

    # Sets the outline of the line
    line.setFill(fill)

    # Sets the width of the line
    line.setWidth

    # Draws the line
    line.draw(win)

    return line
## End DLE

    #----------------------------------------------------------------------

## Draw Rectangle E code:
#
# Draws a rectangle with added color and outline funcitonality for rectangles
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
# Draws a circle with added color and outline funcitonality for circles
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

## Draw Ovl E code:
#
# Draws a oval with added color and outline funcitonality for ovals
#
def drawOvlE(win, point1, point2, fill = "white", outline = "black"):
    # Instantiates the oval at its two points
    ovl = Oval(Point(point1.x, point1.y), Point(point2.x, point2.y))

    # Sets the outline of the oval
    ovl.setFill(fill)

    # Sets the outline of the oval
    ovl.setOutline(outline)

    # Draws the oval
    ovl.draw(win)

    return ovl
## End DCE

    #----------------------------------------------------------------------

## Draw Poly E code:
#
# Draws a polygon with added color and outline funcitonality for polygons
#
def drawPolyE(win, pointList = [Point(0,0)], fill = "white", outline = "black"):
    # Instantiates the polygon at its two points
    poly = Polygon(pointList)

    # Sets the outline of the polygon
    poly.setFill(fill)

    # Sets the outline of the polygon
    poly.setOutline(outline)

    # Draws the polygon
    poly.draw(win)

    return poly
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

## Draw Entry E code:
#
# Draws an entry obj with added color and outline funcitonality
#
def drawEntryE(win, point, width, text = "Entry", fill = "white"):
    # Instantiates the entry at its point with the given words
    entry = Entry(point, width)

    # Sets the text for the entry
    entry.setText(text)

    # Sets the fill inside the entry
    entry.setFill(fill)

    # Draws the entry
    entry.draw(win)

    return entry
## End DEE

    #----------------------------------------------------------------------

## Draw Text Rect E code:
#
# Draws a text obj and bg with added color and outline funcitonality for static text and a bg
#
def drawTextRectE(win, rectpoint1, rectpoint2, text, textSize = 12, fillRect = "white", fillText = "black", outlineRect = "black"):
    

    rectObj = drawRectE(win, rectpoint1, rectpoint2, fillRect, outlineRect)
    textX = (rectpoint1.x + rectpoint2.x) / 2
    textY = (rectpoint1.y + rectpoint2.y) / 2
    textPoint = Point(textX, textY)
    textObj = drawTextE(win, textPoint, text, textSize, fillText)

    return rectObj, textObj
## End DTRE

    #----------------------------------------------------------------------

## Button code:
#
# Draws a text obj and bg with added color and outline funcitonality for a button
#
class Button():
    
    # Initialises the class
    def __init__(self, win, midpoint, width, height, text, textSize = 12, fillRect = "white", fillText = "black", outlineRect = "black"):
        # Sets the corners of the button
        rectpoint1 = Point(midpoint.x - (width / 2), midpoint.y - (height / 2))
        rectpoint2 = Point(midpoint.x + (width / 2), midpoint.y + (height / 2))

        # Pulls all of the corners of the button
        self.corners = [Point(rectpoint1.x, rectpoint1.y), Point(rectpoint2.x, rectpoint1.y), Point(rectpoint2.x, rectpoint2.y), Point(rectpoint1.x, rectpoint2.y)]

        # Finds the min and max values of the x and y
        # [Min x, Max x, Min y, Max y]
        self.maxMin = [rectpoint1.x, rectpoint1.x, rectpoint1.y, rectpoint1.y]

        for i in range(4):
            # Sets the min x
            if (self.corners[i].x < self.maxMin[i]):
                self.maxMin[0] = self.corners[i].x
            # Sets the max x
            if (self.corners[i].x > self.maxMin[i]):
                self.maxMin[1] = self.corners[i].x
            # Sets the min y
            if (self.corners[i].y < self.maxMin[i]):
                self.maxMin[2] = self.corners[i].y
            # Sets the max y
            if (self.corners[i].y > self.maxMin[i]):
                self.maxMin[3] = self.corners[i].y


        # Draws the button
        self.background, self.text = drawTextRectE(win, rectpoint1, rectpoint2, text, textSize, fillRect, fillText, outlineRect)
 

        return
    
    # Checks to see if the button has been pressed
    def checkButton(self, mousePos):
        pressed = False

        # Checks for the position the mouse was clicked and sets X and Y
        #mousePos = win.checkMouse()

        # Checks if the mouse has been clicked or not
        if (mousePos != None):

            # Makes the x and y simpler to type
            mPX = mousePos.x
            mPY = mousePos.y

            # Sees if the spot clicked was in the bounds of the button
            if (mPX > self.maxMin[0] and mPX < self.maxMin[1] and mPY > self.maxMin[2] and mPY < self.maxMin[3]):
                pressed = True

        return pressed
    
    # Draws the button
    def draw(self, win):
        self.background.draw(win)
        self.text.draw(win)

    # Undraws the button
    def undraw(self):
        self.background.undraw()
        self.text.undraw()



## End Button

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
def randoRGB():
    return color_rgb(rando.randint(0, 255), rando.randint(0, 255), rando.randint(0, 255))
## End RRGB

    #----------------------------------------------------------------------

## Hex to RGB code:
#
# Converts hex code to rgb values
#
def hexToRgb(hex = "#000000"):
    split = hex.split("#")
    hex = split[-1]

    # Setup for the conversion table
    # rgbVals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    hexVals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

    upHex = hex.upper()
    

    # Gets the index of the hex value and returns the single rgb val
        # Red
    rHexT = hexVals.index(upHex[0])
    rHexB = hexVals.index(upHex[1])

        # Green
    gHexT = hexVals.index(upHex[2])
    gHexB = hexVals.index(upHex[3])
    
        # Blue
    bHexT = hexVals.index(upHex[4])
    bHexB = hexVals.index(upHex[5])
    

    # Converts the hex rgb to [0:255] rgb
    r = (rHexT * 16) + rHexB
    g = (gHexT * 16) + gHexB
    b = (bHexT * 16) + bHexB

    rgb = [r, g, b]

    return rgb





## End HTR

    #----------------------------------------------------------------------