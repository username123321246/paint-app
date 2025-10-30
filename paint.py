from tkinter import *
from tkinter.colorchooser import askcolor

class Paint(object):
    pen_size = 10
    color = "blue"

def __init__(self):
    self.root = Tk()
    self.pen = Button(self.root, text = "Pen", command =self.usepen)
    self.pen.grid(row = 0, column = 0)

    self.erase = Button(self.root, text ="Eraser", command = self.useeraser)
    self.erase.grid(row = 0, column = 1)

    self.change = Button(self.root, text= "Color", command = self.changecolor)
    self.change.grid(row = 0, column = 2)

    self.brush = Button(self.root, text = "Brush", command = self.usebrush)
    self.brush.grid(row = 0, column = 3)

    self.scale = Scale(self.root, from_ = 1, to = 10, orient = HORIZONTAL)
    self.scale.grid(row = 0, column = 4)

    self.canvas = Canvas(self.root, width = 200, height = 200, bg = "white")
    self.canvas.grid(row = 1, columnspan = 4)
    
    self.setup()

    


    self.root.mainloop()


if __name__ == "__main__":
    Paint()