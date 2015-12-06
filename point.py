import random
class Point:
    def __init__(self, NULL='null'):
        self.x=random.randint(0,10)
        self.y=random.randint(0,10)
        self.i=NULL
    def __str__(self):
        if(self.i=='null'):
            return "X: %s - Y: %s" % (self.x,self.y)
        else:
            return "X: %s - Y: %s - Cluster: %i" % (self.x,self.y,self.i)
    def setCluster(self,i):
        self.i = i
    def getCluster(self):
        return self.i
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setX(self,x):
        self.x=x
    def setY(self,y):
        self.y=y