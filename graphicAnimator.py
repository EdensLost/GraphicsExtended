## Imports
import time
import math as m
from graphics import *
from graphicsExtended import *

# A library used for making graphic animation easier



# A basic linear interpolator useable for any function
def lerp(start, end, interpolator):
    # Divides out the frames into a fraction
    interpolatorFract = 1 / interpolator

    # Gets the difference between the start and stop value 
    dif = end - start

    # Multiplies the difference by the fraction to get an accurate step per frame
    step = dif * interpolatorFract

    return step

# A lerp for going along a line between 2 points
def pointLerp(startPoint, stopPoint, frames, curFrame):
    # Runs a lerp for the two x and y values of the points
    mXStep = lerp(startPoint.x, stopPoint.x, frames)
    mYStep = lerp(startPoint.y, stopPoint.y, frames)

    # Sets the current x and y values based on the current frame
    xPoint = startPoint.x + (mXStep * (curFrame + 1))
    yPoint = startPoint.y + (mYStep * (curFrame + 1))

    # Sets the final point
    point = Point(xPoint, yPoint)
    return point


# A lerp for fading between colors
def colorLerp(startColor, stopColor, frames, curFrame):
    # Runs a lerp for each color paramater for the given colors
    redStep = lerp(startColor[0], stopColor[0], frames)
    greenStep = lerp(startColor[1], stopColor[1], frames)
    blueStep = lerp(startColor[2], stopColor[2], frames)

    # Grabs the current value of the colors values
    redVal = startColor[0] + (redStep * (curFrame + 1))
    greenVal = startColor[1] + (greenStep * (curFrame + 1))
    blueVal = startColor[2] + (blueStep * (curFrame + 1))

    # Creates the new color value
    color = color_rgb(int(redVal), int(greenVal), int(blueVal))

    return color



    
# Finds the step of an exponential interpolation
def xLerp(start, end, interpolator):

    '''
    Start(Step)^(Interpolator) = End

    so

    Step = (End / Start)^(1 / Interpolator)
    '''

    # End divided by the start
    endOverStart = end / start

    # Find the nth root of the end divided by the start using the interpolator
    step = endOverStart ** (1 / interpolator)

    return step