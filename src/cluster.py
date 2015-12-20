class Cluster:
    def __init__(self,id,mass,centroid):
        self.id=id
        self.mass=mass
        self.centroid=centroid

    def __str__(self):
        return "Cluster %s - Centroide: %s" % (self.id,self.centroid)

    def getCentroid(self):
        return self.centroid

    def getCluster(self):
        return self.id

    def setMass(self,mass):
        self.mass=mass

    def getMass(self):
        return self.mass
    def setCentroid(self,centroid):
        self.centroid=centroid