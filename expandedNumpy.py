import numpy
import math
planerVector = numpy.array([0.0,0.0])
newPlanerVector = numpy.array([0.0,0.0])

def clearPlanerVectors():
    planerVector = numpy.array([0.0,0.0])
    newPlanerVector = numpy.array([0.0,0.0])   

def absoluteValue(vector):
    psuedoSum = 0
    for x in vector:
        psuedoSum += (vector[x-1])**2
    finalResult = psuedoSum**(1/2)
    return finalResult

def projectAOntoB(a,b):
    return (b * (numpy.dot(a,b) / ((absoluteValue(b))**2)))

def projectAOntoBLen(a,b):
    return (numpy.dot(a,b) / ((absoluteValue(b))**2))

def norm(vector):
    return (vector / absoluteValue(vector))


def rotateFromAToB(vector, a, b, rotation):
    """
    A and B must be perpendicular unit vectors
    a is the x axis, b is the y axis
    """
    planerVector[0] = projectAOntoBLen(vector,a)
    planerVector[1] = projectAOntoBLen(vector,b)
    newPlanerVector[0] = (planerVector[0]*math.cos(rotation) - planerVector[1]*math.sin(rotation))
    newPlanerVector[1] = (planerVector[0]*math.sin(rotation) + planerVector[1]*math.cos(rotation))
    return ((vector - projectAOntoB(vector, a) - projectAOntoB(vector, b))
            + (newPlanerVector[0]*a) + (newPlanerVector[1]*b))
    clearPlanervectors()

def angleInPlane(vector, a, b):
    """
    A and B must be perpendicular unit vectors"
    a is the x axis, b is the y axis"
    """
    planerVector = numpy.array([projectAOntoBLen(vector,a),projectAOntoBLen(vector,b)])
    'planerVector[1] = projectAOntoBLen(vector,b)'
    length = absoluteValue(planerVector)
    baseAngle = math.acos(numpy.dot(planerVector,numpy.array([1,0])) /(length))
    if planeVector[1] >= 0:
        return baseAngle
    else:
        return (180 - baseAngle)
    
