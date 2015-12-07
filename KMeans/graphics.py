from tkinter import *
color_cluster = {
    0: "blue",
    1: "red",
    2: "yellow",
    3: "green",
    4: "purple",
    'null': "black"
}
def canvas_point(canvas,x,y,d,w,r):
   id = canvas.create_oval(x-r,y-r,x+r,y+r, width=w, fill=color_cluster[d])
   return id


class Graphics_Cluster():
    def create_graph(self):
        range = 480
        for i in self.n:
            canvas_point(self.w,10+(i.getX()*48),10+(i.getY()*48),i.getCluster(),0,3)
        self.w.pack()
        mainloop()

    def __init__(self,n):
        self.n=n
        master = Tk()
        canvas_width = 500
        canvas_height = 500
        self.w = Canvas(master,width=canvas_width,height=canvas_height,bg="white")
       # self.create_graph()

    def set_points(self,n):
        self.n=n

    def add_centroid(self,x,y,d):
        range = 480
        canvas_point(self.w,10+(x*48),10+(y*48),d,2,4)


