import numpy
import math
import pygame


"all vectors must be input as simple lists"
def absoluteValue(distanceVector):
    return (math.sqrt(math.pow((distancevector[0],2) + math.pow(distancevector[1],2) + math.pow(distancevector[2],2))))

def projectAOntoB(a,b):
    return (b * (numpy.dot(a,b) / (math.pow(absoluteValue(b),2))))

def rotateFromAToB(vector, a, b, rotation):
    return (vector - projectAOntoB(vector, a) - projectAOntoB(vector, b)) + (projectAOntoB(vector, a)*math.cos(rotation) - projectAOntoB(vector, b)*math.cos(rotation)) 
    


class eye:
    """
    its basicly a camera
    treat veiwing axis as the x axis, side axis as the y axis, and up as the z axis of the basis of the eye
    (REMEMBER TO MAKE IT A RIGHT HANDED SYSTEM! it could be important)
    """
    def __init__(self, closeClip, farClip, FOVAngle, startPosition, veiwingAxis, sideAxis, upAxis memory):
        closeClip = closeClip
        farClip = farClip
        FOVAngle = FOVAngle
        position = numpy.array(startPosition)
        veiwingAxis = numpy.array(veiwingAxis)
        sideAxis = numpy.array(sideAxis)
        upAxis = numpy.array(upAxis)
        memory = []

    def move(self, displacement):
        self.position += numpy.array(displacement)

    def turn(self, rotation):
        

    def see(self, world, screen):
        "looks at the specified world, and prints what it sees onto the specified screen."
        for item in world.itemsInWorld:
            if self.closeClip < absoluteValue(item.position) < self.farClip:
                if absoluteValue(projectAOntoB(item.position, upAxis)) > 0:
                    math.atan(absoluteValue(projectAOntoB(item.position, sideAxis)) / absoluteValue(projectAOntoB(item.position, upAxis)))
                else:
                    math.atan(absoluteValue(projectAOntoB(item.position, sideAxis)) / absoluteValue(projectAOntoB(item.position, upAxis))) + 180
        

class block:
    "a simple 1x1x1 monocolor block"
    def __init__(self, color, position):
        self.color = color
        self.position = position

        

class world:
    "a way of sorting multiple 'levels'"
    def __init__(self, objectlList):
        self.itemsInWorld = []
        for item in objectList:
            self.itemsInWorld.append(item)

    def spawnNewItem(self, item):
        self.itemsInWorld.append(item)

            

"simple pygame loop imported from: http://www.nerdparadise.com/tech/python/pygame/basics/part1/"

pygame.init()
screen = pygame.display.set_mode((800, 500))
done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        
        pygame.display.flip()
"ends here"

if done is True:
    pygame.quit()




