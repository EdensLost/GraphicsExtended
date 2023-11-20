## Imports
from graphics import *
from graphicsExtended import *
from graphicObjectsGrouper import *

# A program library used for saving shapes to a file to make reusing the shapes easier later

# Global variables for easy editing
ScreenSize = 800


"""
	If you haven't used the program yet create an object first by running the program

	Look in the objects.txt file created when you use the polydrawer for the first time 
	The number you put in the list will be right beside what you named the object
	Only put that number for drawing the corrosponding object

	You don't need all of these lists but it can be helpful for changing 
	the color of specific parts later if you separate the indexes like this
"""
baseDrawingIndexs = []
# exampleIndex1 name
exampleIndex1 = []
# exampleIndex2 name
exampleIndex2 = []
# exampleIndex3 name
exampleIndex3 = []
# exampleIndex4 name
exampleIndex4 = []
# Add all parts together
baseDrawingIndexs.extend(exampleIndex1 + exampleIndex2 + exampleIndex3 + exampleIndex4)

# Sets the color and name of the polygon (The name isn't important)
colorFill = "000000"
startName = f"example"

## Base drawings code: 
#
# Adds refrence drawings to background
#
## To Fix: nothing
#
def baseDrawings(win, ref, inst):
	# Draws polygons and other objects for refrence
	if (ref != None and inst != None):
		ref.undraw()
		inst.undraw()
		

	''' [Base Drawing] ----> Add a # when there are indexes you want to draw

	
	ref = setupInitialObjectGroup(win, baseDrawingIndexs)


	#'''
	
	inst = drawTextE(win, Point(50, 2), "D and click = delete last point, F and click = finish shape")
	# --------------

	return inst
## End of Base

	#----------------------------------------------------------------------

## Polydraw code: 
#
# Draws a shape based on clicked points after given a screen size and point amount
#
## To Fix: Make run smoother by finding out how to keep shapes in a list and make it accessable
#
def polydraw():
	# Adds # to var
	setColorFill = "#"
	setColorOutline = "#"

	# Asks for what to add to the shape name
	setName = str(input("\nWhat is the name of the object?\nName = "))
	name = startName + setName

	setColorFill += colorFill
	setColorOutline += colorFill

	# Instantiates the list of points and current point amount
	pointsForPoly = []
	curPoints = -1

	# Instatiates the previous point
	oldP = None

	# Creates the window 
	win = drawWindowE("Polydraw", ScreenSize, ScreenSize, 100, 100, "grey")

	# Draws refrences if any exist
	ref = None
	inst = None
	inst = baseDrawings(win, ref, inst)

	

	drawing = True

	while(drawing == True):
		# Gets a point where the mouse clicked and check what key was pressed
		p = win.getMouse()
		key = win.checkKey()

		# If D was pressed delete the last point
		if (key == "d" and curPoints >= 0):
			# Subtracts one from the amount of points
			curPoints -= 1

			# Removes the point from the list
			pointsForPoly.pop()

			# Tries to undraw the last point
			try: oldP.undraw()
			except: pass

			if (curPoints > 0):
				# Undraws the deleted line and removes the line from the line list
				refLine.undraw()

				# Sets the old point to the point before the deleted one
				oldP = pointsForPoly[curPoints]

			else:
				oldP = None



			# Redraws the scene
			drawRectE(win, Point(0, 0), Point(100, 100), "grey")

			# Draws refrences if any exist
			inst = baseDrawings(win, ref, inst)


			print("reset")
			for i in range(curPoints + 1):
				
				drawCirE(win, pointsForPoly[i], 1, "black")
				drawTextE(win, pointsForPoly[i], i, 12)


				if (i > 0):
					drawLineE(win, pointsForPoly[i - 1], pointsForPoly[i])
		

			print("\nDeleted last point")

		# If F was pressed complete the polygon
		elif (key == "f" and curPoints >= 0):
			

			print(f"\n{name} Drawing Finished")

			polyShape = drawPolyE(win, pointsForPoly, setColorFill, setColorOutline)

			finishInst = drawTextE(win, Point(50, 20), "Click and press q to add to the objects list\nPress any other key to return back to drawing the shape")
			win.getMouse()
			key = win.checkKey()
			if (key == "q"):
				
				polyShape.undraw()
				drawing = False

			# Redraws the scene
			drawRectE(win, Point(0, 0), Point(100, 100), "grey")
			inst = baseDrawings(win, ref, inst)


			print("reset")
			for i in range(curPoints + 1):
				
				drawCirE(win, pointsForPoly[i], 1, "black")
				drawTextE(win, pointsForPoly[i], i, 12)


				if (i > 0):
					drawLineE(win, pointsForPoly[i - 1], pointsForPoly[i])


			

		# Draw the point and a line between it and the last one in d or f is not pressed
		else:
			curPoints += 1
			
			drawCirE(win, p, 1, "black")
			drawTextE(win, p, curPoints, 12)

			if (oldP != None):
				refLine = Line(p, oldP)
				refLine.draw(win)

			print(p)
			pointsForPoly.append(p)

			oldP = p

			# Redraws everything so the lines show up correctly when only two points exist
			if (curPoints == 1):
				inst = baseDrawings(win, ref, inst)


				print("reset")
				for i in range(curPoints + 1):
					
					drawCirE(win, pointsForPoly[i], 1, "black")
					drawTextE(win, pointsForPoly[i], i, 12)


					if (i > 0):
						drawLineE(win, pointsForPoly[i - 1], pointsForPoly[i])

		
		

		

	
	print(curPoints, pointsForPoly)

	win.getMouse()
	win.close()

	return pointsForPoly, name, setColorFill, setColorOutline
## End of PD

	#----------------------------------------------------------------------

## Shape file code: 
#
# Adds/creates a file to hold all the points of the object to be used later
#
## To Fix: nothing
#
def shapeFile(points, objName, colorFill, colorOutline):

	try: 
		file = open(f"objects.txt", "x")
		file.close()
	except: 
		pass

	file = open(f"objects.txt", "r")

	lines = file.readlines()

	try: 
		numLine = lines[len(lines) - 5]

		setnum, DISCARD = numLine.split(" ", 1)

	except:
		setnum = "-1"

	setnum = eval(setnum) + 1
	
	# Opens the objects file
	file.close()
	file = open(f"objects.txt", "a")

	# Writes all of the points under the name of the object after all of the text already in the objects file
	file.writelines(f"{setnum} [{objName}] \nPolygon({points}): \n{colorFill}: \n{colorOutline}:\n\n")

	# Closes the file
	file.close()

## End of shapeFile

	#----------------------------------------------------------------------

## Main code: 
#
# Runs polydraw then adds/creates a file to hold all the points of the object to be used later
#
## To Fix: nothing
#
def main():
	# Draws the shape
	pointsForPoly, setname, setColorFill, setColorOutline = polydraw()

	# Adds the shape to a file
	shapeFile(pointsForPoly, setname, setColorFill, setColorOutline)
## End of main

	#----------------------------------------------------------------------

main()