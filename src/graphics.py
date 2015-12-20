from tkinter import *
from kmeans import *
from cluster import *
from point import *

#def Colors
color_cluster = {
    0: "blue",
    1: "red",
    2: "yellow",
    3: "green",
    4: "purple",
    'null': "black"
}


while True:
    try:
        numberOfPoints = int(input("How much points?"))
        break
    except ValueError:
        print("Not a number")

while True:
    try:
        numberOfClusters = int(input("How much clusters?"))
        if (numberOfClusters>= 1 and numberOfClusters <= 5):
            break
        else:
            print("Just 1 to 5 Clusters permitted")
    except ValueError:
        print("Not a number")


master = Tk()
canvas_width = 500
canvas_height = 500
window = Canvas(master,width=canvas_width,height=canvas_height,bg="white")
#Function to draw points
def canvas_point(canvas,x,y,color,w,r):
    return canvas.create_oval(x-r,y-r,x+r,y+r, width=w, fill=color_cluster[color])


main = KMeans(numberOfPoints,numberOfClusters)
for i in main.getPoints():
    canvas_point(window,10+(i.getX()*48),10+(i.getY()*48),i.getCluster(),0,3)


def onClick(event):
    if (main.isFinished()):
        window.quit()
    else:
        window.delete(ALL)
        main.nextStep()
        for i in main.getPoints():
            canvas_point(window,10+(i.getX()*48),10+(i.getY()*48),i.getCluster(),0,3)
        for j in main.getClusters():
            canvas_point(window,10+(j.getMass().getX()*48),10+(j.getMass().getY()*48),j.getCluster(),2,5)
window.pack()
window.bind("<Button-1>",onClick)
mainloop()