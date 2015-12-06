class Cluster:
    def __init__(self,i,j):
        self.i=i
        self.j=j
    def __str__(self):
        return "Cluster %s - Centroide: %s" % (self.i,self.j)
    def getCentroid(self):
        return self.j
    def getCluster(self):
        return self.i
    def setCentroid(self,j):
        self.j=j