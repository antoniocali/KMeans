from random import random
from math import sqrt
class Point:
    def __init__(self, id,NULL='null'):
        self.x=(random())*10.
        self.y=(random())*10.
        self.id=id
        self.cluster=NULL
    def __str__(self):
        if(self.cluster=='null'):
            return "X: %s - Y: %s" % (self.x,self.y)
        else:
            return "X: %s - Y: %s - Cluster: %i" % (self.x,self.y,self.cluster)
    def setCluster(self,cluster):
        self.cluster = cluster
    def getCluster(self):
        return self.cluster
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
        self.x=x

    def setY(self,y):
        self.y=y

    def distance(self,point):
        return sqrt(abs(point.getX()-self.x)**2 +abs(point.getY()-self.y)**2)

