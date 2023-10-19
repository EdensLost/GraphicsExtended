## Imports
from graphics import *
from graphicsExtended import *
from graphicObjectsGrouper import *

# A program library used for saving shapes to a file to make reusing the shapes easier later



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

	# Asks for what color the user wants
	setColorFill += input("\nWhat color should the objects fill be? (Hexcode: 0f0f0f)\nColor = ")
	setColorOutline += input("\nWhat color should the objects outline be? (Hexcode: 0f0f0f)\nColor = ")
	setName = str(input("\nWhat is the name of the object?\nName = "))

	# Instantiates the list of points and current point amount
	pointsForPoly = []
	curPoints = -1

	# Instatiates the previous point
	oldP = None

	# Creates the window 
	win = drawWindowE("Polydraw", 1300, 1300, 100, 100, "grey")

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

			oldP.undraw()
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
				
				drawCirE(win, pointsForPoly[i], .2, "black")
				drawTextE(win, pointsForPoly[i], i, 5)


				if (i > 0):
					drawLineE(win, pointsForPoly[i - 1], pointsForPoly[i])
		

			print("\nDeleted last point")

		# If F was pressed complete the polygon
		elif (key == "f" and curPoints >= 0):
			

			print(f"\n{setName} Drawing Finished")

			polyShape = drawPolyE(win, pointsForPoly, setColorFill, setColorOutline)

			inst.setText("Click and press q to add to the objects list\nPress any other key to return back to drawing the shape")
			win.getMouse()
			key = win.checkKey()
			if (key == "q"):
				
				polyShape.undraw()
				drawing = False

			# Redraws the scene
			drawRectE(win, Point(0, 0), Point(100, 100), "grey")

			# Draws refrences if any exist
			baseDrawings(win, ref, inst)


			

		# Draw the point and a line between it and the last one in d or f is not pressed
		else:
			curPoints += 1
			
			drawCirE(win, p, .2, "black")
			drawTextE(win, p, curPoints, 5)

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
					
					drawCirE(win, pointsForPoly[i], .2, "black")
					drawTextE(win, pointsForPoly[i], i, 5)


					if (i > 0):
						drawLineE(win, pointsForPoly[i - 1], pointsForPoly[i])

		
		

		

	
	print(curPoints, pointsForPoly)

	input("\nEnter to close")
	win.close()

	return pointsForPoly, setName, setColorFill, setColorOutline
## End of PD

	#----------------------------------------------------------------------

## Shape file code: 
#
# Adds/creates a file to hold all the points of the object to be used later
#
## To Fix: nothing
#
def shapeFile(points, objName, colorFill, colorOutline):
	file = open(f"objects.txt", "r")

	lines = file.readlines()

	try: 
		numLine = lines[len(lines) - 5]

		setnum, DISCARD = numLine.split(" ", 1)

	except:
		setnum = "-1"

	setnum = eval(setnum) + 1
	
	# Opens the objects file
	file = open(f"objects.txt", "a")

	# Writes all of the points under the name of the object after all of the text already in the objects file
	file.writelines(f"{setnum} [{objName}] \nPolygon({points}): \n{colorFill}: \n{colorOutline}:\n\n")

	# Closes the file
	file.close()

## End of shapeFile

	#----------------------------------------------------------------------

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
	
	#''' [Base Drawing]

	baseDrawingIndexs = [10, 11, 62, 63, 64, 65]
	ref = setupInitialObjectGroup(win, baseDrawingIndexs)

	baseDrawingIndexs = [68]
	ref = setupInitialObjectGroup(win, baseDrawingIndexs, .4, -7, Point(16.1, 33))
	ref.setColor(0, "#000000")

	baseDrawingIndexs = [68]
	ref = setupInitialObjectGroup(win, baseDrawingIndexs, .4, -7, Point(15.8, 33))
	ref.setColor(0, "#34185e")

	baseDrawingIndexs = [68]
	ref = setupInitialObjectGroup(win, baseDrawingIndexs, .4, -7, Point(15.5, 33))


	#''' a35315


	inst = drawTextE(win, Point(50, 2), "D and click = delete last point, F and click = finish shape")
	# --------------

	return inst

# Right Jack-O-Lantern Eye Inner


## End of main

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