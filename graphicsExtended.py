## My personal graphics library which adds less typing needed for objects
# graphicsExtended.py



from graphics import *
import random as rando
import math as m


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

## Line E code:
#
# Creates a line with added color and outline funcitonality for lines
#
def lineE(point1, point2, fill = "black", width = 1):
	# Instantiates the line at its two points
	line = Line(Point(point1.x, point1.y), Point(point2.x, point2.y))

	# Sets the outline of the line
	line.setFill(fill)

	# Sets the width of the line
	line.setWidth(width)

	return line
## End LE

	#----------------------------------------------------------------------

## Draw Line E code:
#
# Draws a line with added color and outline funcitonality for lines
#
def drawLineE(win, point1, point2, fill = "black", width = 1):
	line = lineE(point1, point2, fill, width)
	line.draw(win)

	return line
## End DLE

	#----------------------------------------------------------------------


## Rectangle E code:
#
# Creates a rectangle with added color and outline funcitonality for rectangles
#
def rectE(point1, point2, fill = "white", outline = "black", borderWidth = 1):
	# Instantiates the rect at its two points
	rect = Rectangle(Point(point1.x, point1.y), Point(point2.x, point2.y))

	# Sets the outline of the rect
	rect.setFill(fill)

	# Sets the outline of the rect
	rect.setOutline(outline)

	# Sets the outline width of the rect
	rect.setWidth(borderWidth)

	return rect
## End RE

	#----------------------------------------------------------------------

## Draw Rectangle E code:
#
# Draws a rectangle with added color and outline funcitonality for rectangles
#
def drawRectE(win, point1, point2, fill = "white", outline = "black", borderWidth = 1):
	rect = rectE(point1, point2, fill, outline, borderWidth)
	rect.draw(win)

	return rect
## End DRE

	#----------------------------------------------------------------------


## Cir E code:
#
# Creates a circle with added color and outline funcitonality for circles
#
def cirE(point, radius, fill = "white", outline = "black", width = 1):
	# Instantiates the circle at its two points
	cir = Circle(Point(point.x, point.y), radius)

	# Sets the outline of the circle
	cir.setFill(fill)

	# Sets the outline of the circle
	cir.setOutline(outline)

	# Sets the width of the circle outline
	cir.setWidth(width)

	return cir
## End CE

	#----------------------------------------------------------------------

## Draw Cir E code:
#
# Draws a circle with added color and outline funcitonality for circles
#
def drawCirE(win, point, radius, fill = "white", outline = "black", width = 1):
	cir = cirE(point, radius, fill, outline)
	cir.draw(win)

	return cir
## End DCE

	#----------------------------------------------------------------------

## Ovl E code:
#
# Creates a oval with added color and outline funcitonality for ovals
#
def ovlE(point1, point2, fill = "white", outline = "black"):
	# Instantiates the oval at its two points
	ovl = Oval(Point(point1.x, point1.y), Point(point2.x, point2.y))

	# Sets the outline of the oval
	ovl.setFill(fill)

	# Sets the outline of the oval
	ovl.setOutline(outline)

	return ovl
## End CE

	#----------------------------------------------------------------------

## Draw Ovl E code:
#
# Draws a oval with added color and outline funcitonality for ovals
#
def drawOvlE(win, point1, point2, fill = "white", outline = "black"):
	ovl = ovlE(point1, point2, fill, outline)
	ovl.draw(win)

	return ovl
## End DCE

	#----------------------------------------------------------------------

## Poly E code:
#
# Creates a polygon with added color and outline funcitonality for polygons
#
def polyE(pointList = [Point(0,0)], fill = "white", outline = "black"):
	# Instantiates the polygon at its two points
	poly = Polygon(pointList)

	# Sets the outline of the polygon
	poly.setFill(fill)

	# Sets the outline of the polygon
	poly.setOutline(outline)

	return poly
## End PE

	#----------------------------------------------------------------------

## Draw Poly E code:
#
# Draws a polygon with added color and outline funcitonality for polygons
#
def drawPolyE(win, pointList = [Point(0,0)], fill = "white", outline = "black"):
	poly = polyE(pointList, fill, outline)
	poly.draw(win)

	return poly
## End DPE

	#----------------------------------------------------------------------

## Text E code:
#
# Creates a text obj with added color and outline funcitonality
#
def textE(point, words, size = 12, fill = "black"):
	# Instantiates the text at its point with the given words
	text = Text(point, words)

	# Sets the size of the text
	text.setSize(size)

	# Sets the outline of the text
	text.setTextColor(fill)

	return text
## End TE

	#----------------------------------------------------------------------

## Draw Text E code:
#
# Draws a text obj with added color and outline funcitonality
#
def drawTextE(win, point, words, size = 12, fill = "black"):
	text = textE(point, words, size, fill)
	text.draw(win)

	return text
## End DTE

	#----------------------------------------------------------------------

## Entry E code:
#
# Creates an entry obj with added color and outline funcitonality
#
def entryE(point, width, text = "Entry", fill = "white"):
	# Instantiates the entry at its point with the given words
	entry = Entry(point, width)

	# Sets the text for the entry
	entry.setText(text)

	# Sets the fill inside the entry
	entry.setFill(fill)

	return entry
## End EE

	#----------------------------------------------------------------------

## Draw Entry E code:
#
# Draws an entry obj with added color and outline funcitonality
#
def drawEntryE(win, point, width, text = "Entry", fill = "white"):
	entry = entryE(point, width, text, fill)
	entry.draw(win)

	return entry
## End DEE

	#----------------------------------------------------------------------

## Text Rect E code:
#
# Creates a text obj and bg with added color and outline funcitonality for static text and a bg
#
def textRectE(rectpoint1, rectpoint2, text, textSize = 12, fillRect = "white", fillText = "black", outlineRect = "black", borderWidth = 1):
	

	rectObj = rectE(rectpoint1, rectpoint2, fillRect, outlineRect, borderWidth)
	textX = (rectpoint1.x + rectpoint2.x) / 2
	textY = (rectpoint1.y + rectpoint2.y) / 2
	textPoint = Point(textX, textY)
	textObj = textE(textPoint, text, textSize, fillText)

	return rectObj, textObj
## End TRE

	#----------------------------------------------------------------------

## Draw Text Rect E code:
#
# Draws a text obj and bg with added color and outline funcitonality for static text and a bg
#
def drawTextRectE(win, rectpoint1, rectpoint2, text, textSize = 12, fillRect = "white", fillText = "black", outlineRect = "black"):
	rectObj, textObj = textRectE(rectpoint1, rectpoint2, text, textSize, fillRect, fillText, outlineRect)
	rectObj.draw(win)
	textObj.draw(win)

	return rectObj, textObj
## End DTRE

	#----------------------------------------------------------------------

## Button code:
#
# Draws a text obj and bg with added color and outline funcitonality for a button
#
class Button():
	
	# Initialises the class
	def __init__(self, midpoint: Point, width: float, height: float, text: str, textSize = 12, fillRect = "white", fillText = "black", outlineRect = "black", borderWidth = 1):
		# Sets the corners of the button
		rectpoint1 = Point(midpoint.x - (width / 2), midpoint.y - (height / 2))
		rectpoint2 = Point(midpoint.x + (width / 2), midpoint.y + (height / 2))

		self.rectpoint1 = rectpoint1
		self.rectpoint2 = rectpoint2

		# Pulls all of the corners of the button
		self.corners = [Point(rectpoint1.x, rectpoint1.y), Point(rectpoint2.x, rectpoint1.y), Point(rectpoint2.x, rectpoint2.y), Point(rectpoint1.x, rectpoint2.y)]

		# Finds the min and max values of the x and y
		# [Min x, Max x, Min y, Max y]
		self.maxMin = [rectpoint2.x, rectpoint2.x, rectpoint2.y, rectpoint2.y]

		for i in range(4):
			# Sets the min x
			if (self.corners[i].x < self.maxMin[0]):
				self.maxMin[0] = self.corners[i].x
			# Sets the max x
			if (self.corners[i].x > self.maxMin[1]):
				self.maxMin[1] = self.corners[i].x
			# Sets the min y
			if (self.corners[i].y < self.maxMin[2]):
				self.maxMin[2] = self.corners[i].y
			# Sets the max y
			if (self.corners[i].y > self.maxMin[3]):
				self.maxMin[3] = self.corners[i].y


		# Draws the button
		self.tag = text
		self.background, self.text = textRectE(rectpoint1, rectpoint2, text, textSize, fillRect, fillText, outlineRect, borderWidth)
 

		return
	
	# Gets the text associated with the button
	def getText(self):
		return self.tag
	
	# Sets the text associated with the button
	def setText(self, newText: str):
		self.tag = newText
		self.text.setText(newText)

	# Checks to see if the button has been pressed
	def checkButton(self, mousePos):
		pressed = False

		# Checks if the button exists
		if (self.background.canvas):
		
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

## Create X code:
#
# Creates an X at the center of a point scaling based on given size
#
def creaXE(point, size = 1, fill = "black", width = 1):
	half = size / 2

	# Assigns all of the corners of the x
	tRCorner = Point(point.x + half, point.y + half)
	bRCorner = Point(point.x + half, point.y - half)
	bLCorner = Point(point.x - half, point.y - half)
	tLCorner = Point(point.x - half, point.y + half)

	# Draws the lines of the X
	line1 = lineE(tLCorner, bRCorner, fill, width)
	line2 = lineE(tRCorner, bLCorner, fill, width)

	return line1, line2
## End DX

	#----------------------------------------------------------------------

## Draw X code:
#
# Draws an X at the center of a point scaling based on given size
#
def drawX(win, point, size = 1, fill = "black", width = 1):
	line1, line2 = creaXE(point, size, fill, width)
	line1.draw(win)
	line2.draw(win)

	return line1, line2
## End DX

	#----------------------------------------------------------------------

## Move on angle code:
#
# Moves a given shape along an angle a specified amount
#
def moveOnAngle(shape, curDirection, moveLength):
	# Gets the quadrant of the movement
	quadrant = 1
	moveDir = float(curDirection[0])

	while (moveDir > 90 or moveDir < 0):

		# If moveDir is too much
		if (moveDir > 90):
			moveDir -= 90

			if(quadrant == 1):
				quadrant = 4

			else:
				quadrant -= 1
		# If moveDir is too little
		elif (moveDir < 0):
			moveDir += 90

			if(quadrant == 4):
				quadrant = 1

			else:
				quadrant += 1


	# Sets the proportions for the movement
	moveRadian = moveDir * (m.pi / 180)

	firstMov = moveLength * m.sin(moveRadian) # Opposite
	secondMov = moveLength * m.cos(moveRadian) # Adjacent

	"""Sets the delta(X) and delta(Y)"""
	# Flips the x and y if the quadrant is even
	if (quadrant % 2 == 0):
		dX = secondMov
		dY = firstMov

		# Second quadrant has x negative
		if (quadrant == 2):
			dX *= -1 

		# Fourth quadrant has y negative
		else:
			dY *= -1 
	
	# Keeps them the same if odd
	else:
		dX = firstMov
		dY = secondMov

		# Third quadrant has x and y negative
		if (quadrant == 3):
			dX *= -1 
			dY *= -1

		# First doesn't change

	# Moves the shape
	shape.move(dX, dY)

## End MOA

	#----------------------------------------------------------------------

## Clear objects code:
#
# Undraws the entire list of items
#
def clearObjs(listsToClear: list, itemsToClear: list = []):
	try:
		for array in listsToClear:
			itemsToClear.extend(array)

	except:
		itemsToClear.extend(listsToClear)

	for item in itemsToClear:
		item.undraw()
## End COs

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

## HUE to RGB code:
#
# Converts Hue to RGB values
#
def hueToRgb(p, q, t):
	"""### Honestly I don't really understand this but oh well
	p = The calculated lightness value based on the hue and saturation\n
	q = The calculated value based on the lightness and saturation\n
	t = Helps determine the RGB components base on the hue value"""

	# Does magic matrix stuff
	if t < 0:
		t += 1
	if t > 1:
		t -= 1
	if t < (1 / 6):
		return p + (q - p) * 6 * t
	if t < (1 / 2):
		return q
	if t < (2 / 3):
		return p + (q - p) * (2 / 3 - t) * 6
	return p

## End HuTR

	#----------------------------------------------------------------------

## HSL to RGB code:
#
# Converts HSL code to RGB values
#
def hslToRgb(h = 360, s = 100, l = 50):
	"""h = Hue -> [0, 360]\n
	s = Saturation -> [0%, 100%]\n
	l = Lightness -> [0%, 100%]"""

	# Sets the hue from [0, 1]
	h /= 360

	# Clamps saturation and lightness to [0, 1]
	s = s / 100
	l = l / 100
	s = max(0, min(1, s))
	l = max(0, min(1, l))

	# If saturation is 0 all r g b values will be the same
	if s == 0:
		r = g = b = int(l * 255)

	# Otherwise set the rgb values
	else:
		if l < 0.5:
			q = l * (1 + s)  
		else: 
			q = l + s - l * s
		p = 2 * l - q

		r = int(round(hueToRgb(p, q, h + 1 / 3) * 255 , 0))
		g = int(round(hueToRgb(p, q, h) * 255 , 0))
		b = int(round(hueToRgb(p, q, h - 1 / 3) * 255, 0))
		
	return r, g, b

## End HlTR

	#----------------------------------------------------------------------

## HSL to Hex code:
#
# Converts HSL code to Hex code
#
def hslToHex(h = 360, s = 100, l = 50):
	"""h = Hue -> [0, 360]\n
	s = Saturation -> [0%, 100%]\n
	l = Lightness -> [0%, 100%]"""

	# Gets the rgb from the hsl
	r, g, b = hslToRgb(h, s, l)

	# Converts it to a hex value
	color = color_rgb(r, g, b)
		
	# Converts it to hex
	return color

## End HlTHx

	#----------------------------------------------------------------------


