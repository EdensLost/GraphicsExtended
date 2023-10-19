## Imports
from graphics import *
from graphicsExtended import *

import math

# A library used for grouping many polygons together to form one object with group based features

class ObjGroup():

    # Initialises the class
    def __init__(self, shapes, colorsFill, colorsOutline):
        # Checks to see if shapes is a list and redefines it
        if (len(shapes) == 1 and type(shapes[0]) == type([])):
            shapes = shapes[0]

        # Sets all the values and everything for the lists in the shape to use later
        self.shapes = list(map(Polygon.clone, shapes))
        self.colorsFill = colorsFill
        self.colorsOutline = colorsOutline
        
        # Sets the center of the group
        self.setCenter(self.shapes)

        return
    
    # Gives a default print statment? I think
    def __repr__(self):

        return "Group"+str(tuple(p for p in self.shapes))
    
    # Draws the group
    def draw(self, win):
        poly = []
        for i in range(0, len(self.shapes)): 
            poly.append(drawPolyE(win, self.shapes[i].getPoints(), self.colorsFill[i], self.colorsOutline[i]))

        self.poly = poly

    # Undraws the group
    def undraw(self):
        poly = []
        for i in range(0, len(self.shapes)): 
            self.poly[i].undraw()

        self.poly = poly
    
    # Moves the group object
    def move(self, mX, mY):
        
        # Looks through all of the shapes to look though all the points in the shape
        for i in range(0, len(self.shapes)):

            # Looks through all of the points of the current shape
            for j in range(0, len(self.shapes[i].getPoints())):
                # Gets an x and y point
                pointX = self.shapes[i].points[j].getX()
                pointY = self.shapes[i].points[j].getY()

                # Calculates the new points
                newPointX = pointX + mX
                newPointY = pointY + mY

                # Sets the new points
                self.shapes[i].points[j].x = newPointX
                self.shapes[i].points[j].y = newPointY

            self.poly[i].move(mX, mY)

        # Undraws and redraws the shape to apply the new scale
        '''self.undraw()
        self.draw(win)'''
        

        # Sets the center of the group
        self.setCenter(self.poly)

    # Scales up or down the group object
    def scale(self, growAmt):
        # Looks through all of the shapes to look though all the points in the shape
        for i in range(0, len(self.shapes)):

            # Looks through all of the points of the current shape
            for j in range(0, len(self.shapes[i].getPoints())):
                # Gets an x and y point
                pointX = self.shapes[i].points[j].getX()
                pointY = self.shapes[i].points[j].getY()

                # Calculates the distance from the center to y and x
                xDist = pointX - self.center.x
                yDist = pointY - self.center.y

                # Multiplies the distance by the growth value
                newXDist = xDist * growAmt
                newYDist = yDist * growAmt

                # Calculates the new points
                newPointX = newXDist + self.center.x
                newPointY = newYDist + self.center.y

                # Sets the new points
                self.shapes[i].points[j].x = newPointX
                self.shapes[i].points[j].y = newPointY

        # Sets the center of the group
        self.setCenter(self.poly)

        return
    
    # Rotates a group
    def rotate(self, rotDeg):
        

        # Looks through all of the shapes to look though all the points in the shape
        for i in range(0, len(self.shapes)):

            # Looks through all of the points of the current shape
            for j in range(0, len(self.shapes[i].getPoints())):

                # Gets an x and y point
                pointX = self.shapes[i].points[j].getX()
                pointY = self.shapes[i].points[j].getY()


                # Calculates the distance from the center to y and x
                xDist = pointX - self.center.x 
                yDist = pointY - self.center.y 


                # Sets absolute of the distance because a triangle can not have negative length
                xAbsDist = math.fabs(xDist) #  == a
                yAbsDist = math.fabs(yDist) #  == o


                # Uses the pythagorean theorem to get the radius distance
                hDist = math.sqrt(math.pow(yAbsDist, 2) + math.pow(xAbsDist, 2))


                # Use the inverse tan(x) to get the angle towards the point in radians
                try:
                    radAngl = math.atan(yAbsDist / xAbsDist)

                except:
                    if (xAbsDist == 0 and yAbsDist != 0):
                        radAngl = math.asin(yAbsDist / hDist)

                    elif (yAbsDist == 0 and xAbsDist != 0):
                        radAngl = math.acos(xAbsDist / hDist)
                        
                    else:
                        radAngl = 0
                
 

                # Flip the angle if the angle is in a position where it's reversed so that it goes clockwise
                if (xDist * yDist >= 0):
                    radAngl = (math.pi/2) - radAngl

 

                # Converts the degrees to radians then adds the current rotation to it
                addAngl = (rotDeg * (math.pi / 180)) + radAngl


                # Converts the added angle into degrees
                degAngl = (addAngl * (180 / math.pi))

 

                # Finds the initial orientation of the angle
                if (xDist >= 0 and yDist >= 0):
                    quadrant = 1
                elif (xDist < 0 and yDist >= 0):
                    quadrant = 2
                elif (xDist < 0 and yDist < 0):
                    quadrant = 3
                elif (xDist >= 0 and yDist < 0):
                    quadrant = 4    


                # Finds the end orientation of the angle
                found = False
                while (found == False):

                    # Checks if the angle that was given was positive
                    if (degAngl > 90):
                        degAngl -= 90
                
                        
                        if(quadrant > 1):
                            quadrant -= 1
  

                        else:
                            quadrant = 4
 
                        
                    # If neither are true then the loop ends
                    else:
                        found = True


                # Converts the degree angle to radians
                newAngl = (degAngl * (math.pi / 180))
                

                # Flip the angle if the angle is in a position where it's reversed so that it goes clockwise
                if (quadrant == 1 or quadrant == 3):
                    newAngl = (math.pi/2) - newAngl


                # Gets the new x distance from the hDistance multiplied by the cos(x) of the new angle
                newXDist = math.fabs(hDist) * math.cos(newAngl) # newXDist == new a


                # Gets the new y distance from the hDistance multiplied by the sin(x) of the new angle
                newYDist = math.fabs(hDist) * math.sin(newAngl) # newYDist == new o


                # Sets the negative values needed for putting the points in the quadrants
                if (quadrant == 1):
                    newXDist *= 1
                    newYDist *= 1

                elif (quadrant == 2):
                    newXDist *= -1
                    newYDist *= 1

                elif (quadrant == 3):
                    newXDist *= -1
                    newYDist *= -1

                elif (quadrant == 4):
                    newXDist *= 1
                    newYDist *= -1

                # Calculates the new points
                newPointX = self.center.x + newXDist
                newPointY = self.center.y + newYDist

                # Sets the new points
                self.shapes[i].points[j].x = newPointX
                self.shapes[i].points[j].y = newPointY

        # Sets the center of the group
        self.setCenter(self.poly)

        
        return

    # Moves an group to a point
    def moveToPoint(self, win, p):
        xDist = p.getX() - self.center.getX() 
        yDist = p.getY() - self.center.getY()

        self.move(xDist, yDist)

        
    # Draws a bounding box on top of the shape with the center point in the middle
    def drawBounds(self, win):
        shapeCenter = self.center
        boxTL = Point(shapeCenter.x - (self.width / 2), shapeCenter.y - (self.height / 2))
        boxTR = Point(shapeCenter.x + (self.width / 2), shapeCenter.y + (self.height / 2))


        square = drawRectE(win, boxTL, boxTR, "red")
        centerPoint = drawCirE(win, shapeCenter, 1, "black")
        win.getMouse()
        centerPoint.undraw()
        square.undraw()

    # Sets the center and the height and width of the group
    def setCenter(self, shapes):
        # maxMins [minX, maxX, minY, maxY]
        maxMins = [None, None, None, None]

        # Looks through all of the shapes to look though all the points in the shape
        for i in range(0, len(shapes)):

            # Looks through all of the points of the current shape
            for j in range(0, len(self.shapes[i].getPoints())):
                shapeX = self.shapes[i].points[j].getX()
                shapeY = self.shapes[i].points[j].getY()

                # If maxMins has no values add some for the base to go off of
                if (maxMins[0] == None or maxMins[1] == None or maxMins[2] == None or maxMins[3] == None):
                    maxMins[0] = shapeX
                    maxMins[1] = shapeX
                    maxMins[2] = shapeY
                    maxMins[3] = shapeY
                else:
                    # For setting the min of x to the new min of x
                    if (shapeX < maxMins[0]):
                        maxMins[0] = shapeX
                    
                    # For setting the max of x to the new max of x
                    if (shapeX > maxMins[1]):
                        maxMins[1] = shapeX

                    # For setting the min of y to the new min of y
                    if (shapeY < maxMins[2]):
                        maxMins[2] = shapeY

                    # For setting the max of y to the new max of y
                    if (shapeY > maxMins[3]):
                        maxMins[3] = shapeY

        self.width = maxMins[1] - maxMins[0]
        self.height = maxMins[3] - maxMins[2]

        self.center = Point((self.width / 2) + maxMins[0], (self.height / 2) + maxMins[2])

    # Sets the color of a certain object in the shape group
    def setColor(self, index, color):
        # Grabs the indexed shape
        self.colorsFill[index] = color
        self.colorsOutline[index] = color
        self.poly[index].setFill(color)
        self.poly[index].setOutline(color)

    # Sets the scale and rotation so you don't have to manually draw
    def scaleRot(self, win, growAmt = 1, rotDeg = 0):
        
        # If the scale amount will change the scale
        if (growAmt != 1):
            self.scale(growAmt)

        # If the rot amount will change the rotation
        if (rotDeg != 0):
            self.rotate(rotDeg)

        # Undraws and redraws the shape to apply the new scale and rot
        self.undraw()
        self.draw(win)



# Used for obtaining values from the objects.txt used for creating object groups easier
def getObjVals(frstIndex):
	# Opens the object file to refrence the polygons inside it
	file = open(f"objects.txt", "r")

	# Reads all the lines in the objects file
	objectsFile = file.readlines()

	# Reads the objects file and splits off the \n from the object so the string is useable
	obj, DISCARD = objectsFile[frstIndex].split(':', 1)

	# Reads the objects file and splits off the \n from the object so the string is useable
	fill, DISCARD = objectsFile[frstIndex + 1].split(':', 1)

	# Reads the objects file and splits off the \n from the object so the string is useable
	outline, DISCARD = objectsFile[frstIndex + 2].split(':', 1)

	return obj, fill, outline
	
def createGroupObj(firstIndexes):
    # Instantiates the lists needed for the group obj
    shapesToGroup = []
    colorsFillToGroup = []
    colorsOutlineToGroup = []

    # Runs through all the given indexes
    for i in range(len(firstIndexes)):
        # Changes the index to make it readable to the code
        curIndex = firstIndexes[i] * 5 + 1

        # Gets all of the variables for the objects
        obj, fill, outline = getObjVals(curIndex)

        # Adds all the variables to the lists
        shapesToGroup.append(eval(obj))
        colorsFillToGroup.append(fill)
        colorsOutlineToGroup.append(outline)

    # Creates the group from the list
    groupObj = ObjGroup(shapesToGroup, colorsFillToGroup, colorsOutlineToGroup)

    return groupObj

# Sets up initial object group and draws it
def setupInitialObjectGroup(win, shapeIndexs, startScale = 1, startRot = 0, startPoint = None):

    # Creates group object
    shape = createGroupObj(shapeIndexs)
    
    shape.draw(win)

    # If there is no new point set to normal point
    if (startPoint != None):
        shape.moveToPoint(win, startPoint)

    

    # Sets initial scale and rotation
    shape.scaleRot(win, startScale, startRot)

    
    

    return shape

# Grabs the list of groups polygons to make a new single group out of multiple
def groupGroups(win, groups):
    
    colorsFill = []
    colorsOutline = []
    polygons = []

    # Searches through all given groups and puts their parameters together
    for i in range(len(groups)):
        colorsFill.extend(groups[i].colorsFill)
        colorsOutline.extend(groups[i].colorsOutline)
        polygons.extend(groups[i].poly)

    # Creates the new group from the other groups and draws it
    groupGroup = ObjGroup(polygons, colorsFill, colorsOutline)
    groupGroup.draw(win)

    # Undraws old shapes
    for i in range(len(groups)):
        groups[i].undraw()

    return groupGroup


        