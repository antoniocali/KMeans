import point
import cluster
import math
import random
from statistics import mean
points=[]
centroids=[]
clusters = []

def distance(x,y):
    return math.sqrt(abs(x.getX()-y.getX())**2+abs(x.getY()-y.getY())**2)

while True:
    try:
        numberOfPoints = int(input("How much points?"))
        break
    except ValueError:
        print("Not a number")

while True:
    try:
        numberOfClusters = int(input("How much clusters?"))
        break
    except ValueError:
        print("Not a number")


#Step 0 - Creazione Punti
for i in range(numberOfPoints):
    points.append(point.Point())

#Step 0 - Creazione Clusters con Centroidi casuali
for i in range(numberOfClusters):
    j = random.randint(0,len(points)-1)
    while(j in centroids):
        j = random.randint(0,len(points)-1)
    centroids.append(j)
    clusters.append(cluster.Cluster(i,points[j]))

for i in clusters:
    print(i)

ERR = math.inf #Errore totale - utile per sapere quando finire
finished=False
step = 0
while(not finished):
    print("STEP " + str(step))
    newERR=0 #Nuovo Errore totale.
    #Attribuire Cluster
    for t,i in enumerate(points):
        tempDistance = math.inf
        for k,j in enumerate(clusters):
            temp = distance(i,j.getCentroid())
            if(temp<tempDistance):
                tempDistance = temp
                i.setCluster(j.getCluster())

    #Aggiornamento Centroide
    for i,t in enumerate(clusters):
        tempCentroid = point.Point()
        tempList = [elem for elem in points if (t.getCluster()==elem.getCluster())]
        tempCentroid.setX(mean([elem.getX() for elem in tempList]))
        tempCentroid.setY(mean([elem.getY() for elem in tempList]))
        print("Centro di Massa: " + str(tempCentroid)) #Stampa il centro di massa
        tempDistance = math.inf
        #Calcola il punto più vicino nel cluster al centro di massa
        for elem in tempList:
            if(distance(elem,tempCentroid)<tempDistance):
                tempDistance = distance(elem,tempCentroid)
                t.setCentroid(elem)
        #Stampa il Cluster con il relativo Centroide
        print("Cluster " + str(i) + " - Centroide: " + str(t.getCentroid()))
        #Aggiungere l'errore al newError per il t-esimo cluster
        for elem in tempList:
            newERR = newERR + distance(elem,t.getCentroid())
            print(elem)
    #Lo stop ha migliorato l'errore?
    if(newERR<ERR):
        ERR=newERR
    else:
        finished=True

    step+=1
    input("Enter for next step")



