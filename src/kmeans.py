from point import *
from cluster import *
from random import randint
from math import inf
from statistics import mean
class KMeans:
    def __init__(self,numOfPoints,numOfClusters):
        self.numOfPoints=numOfPoints
        self.numOfClusters=numOfClusters
        self.points = []
        self.clusters = []
        self.centroids = []

        self.MSE = inf #Mean Squared Error - Need to understand when KMeans finishes
        self.finished=False
        self.step = 0
        #Adding points
        for i in range(self.numOfPoints):
            self.points.append(Point(i))

        #Create Clusters with random centroid
        for i in range(self.numOfClusters):
            j = randint(0,len(self.points)-1)
            while(j in self.centroids):
                j = randint(0,len(self.points)-1)
            self.centroids.append(j)
            self.clusters.append(Cluster(i,self.points[j],self.points[j]))

    #Setup new Initial Centroids
    def stepZero(self):
        self.centroids.clear()
        self.centroids.clear()
        #Create Clusters with random centroid
        for i in range(self.numOfClusters):
            j = randint(0,len(self.points)-1)
            while(j in self.centroids):
                j = randint(0,len(self.points)-1)
            self.centroids.append(j)
            self.clusters.append(Cluster(i,self.points[j],self.points[j]))
    #Return Points
    def getPoints(self):
        return self.points

    #Return Clusters
    def getClusters(self):
        return self.clusters

    #Return Finished
    def isFinished(self):
        return self.finished

    #Next Step in K-Means
    def nextStep(self):

        if(not self.finished):
            newMSE = 0 #Need to compare with self.ERR

            #Find right cluster for each point
            for point in self.points:
                minDistance = inf
                for cluster in self.clusters:
                    tempDistance = point.distance(cluster.getCentroid())
                    if (tempDistance<minDistance):
                        minDistance=tempDistance
                        point.setCluster(cluster.getCluster())


            #Update Center of Mass and Centroid for each cluster
            for cluster in self.clusters:
                #Getting Points in this cluster
                tempPoints = [point for point in self.points if (point.cluster==cluster.id)]
                #Updating Mass
                (cluster.mass).setX(mean([elem.x for elem in tempPoints]))
                (cluster.mass).setY(mean([elem.y for elem in tempPoints]))
                #Updating Centroid
                minDistance=inf
                for point in tempPoints:
                    tempDistance = point.distance(cluster.mass)
                    if(tempDistance<minDistance):
                        minDistance=tempDistance
                        cluster.setCentroid(point)

                #Sum Partial MSE
                for point in tempPoints:
                    newMSE+=point.distance(cluster.getCentroid())

            if(newMSE<self.MSE):
                self.MSE=newMSE
                self.step+=1
            else:
                self.finished=True


