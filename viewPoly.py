## Imports
from graphics import *
from graphicsExtended import *
from graphicObjectsGrouper import *

# Sets whats drawn
def baseDrawings(win, ref, inst):
	# Draws polygons and other objects for refrence
	if (ref != None and inst != None):
		ref.undraw()
		inst.undraw()
	
	
	"""
		Look in the objects.txt file created when you use the polydrawer for the first time 
		The number you put in the list will be right beside what you named the object
		Only put that number for drawing the corrosponding object

		You don't need all of these lists but it can be helpful for changing 
		the color of specific parts later if you separate the indexes like this
	"""
	#[Base Drawing]
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
	"""
		An important thing to note is that the order the objects are draw 
		corrosponds with their order in the list

		So make sure your bottom object is at the top of the list and top object is at the bottom
	"""


	"""
		win --> [This should be the window you want the object to draw to]

		baseDrawingIndexs --> [These are all of the indexes you want to pull your objects from to be drawn]

		objScale --> [Can be set to any float and multiplies the scale of the object] 

		objRotation --> [Can be set to any float and changes the rotation of the object by degrees]
	"""	
	objScale = 1
	objRotation = 0
	
	ref = setupInitialObjectGroup(win, baseDrawingIndexs, objScale, objRotation)
	
ScreenSize = 800

win = drawWindowE("Polydraw", ScreenSize, ScreenSize, 100, 100, "grey")

# Draws refrences if any exist
ref = None
inst = None
inst = baseDrawings(win, ref, inst)
win.getMouse()
win.close()