from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):
    pen_size = 10
    DEFAULT_COLOR = "blue"

    def __init__(self):
        self.root = Tk()
        self.root.title("Simple Paint App")
        self.root.geometry("400x300")

        self.pen = Button(self.root, text="Pen", command=self.use_pen)
        self.pen.grid(row=0, column=0)

        self.erase = Button(self.root, text="Eraser", command=self.use_eraser)
        self.erase.grid(row=0, column=1)

        self.change = Button(self.root, text="Color", command=self.choose_color)
        self.change.grid(row=0, column=2)

        self.brush = Button(self.root, text="Brush", command=self.use_brush)
        self.brush.grid(row=0, column=3)

        self.scale = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.scale.grid(row=0, column=4)

        self.canvas = Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.grid(row=1, columnspan=5)


        self.setup()
        self.root.mainloop()
    
    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.scale.get()
        self.color = self.DEFAULT_COLOR
        self.erase_on = False
        self.activebutton = self.pen
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)
        
    def use_pen(self):
        self.activate_button(self.pen)
    
    def use_brush(self):
        self.activate_button(self.brush)
    
    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color = self.color)[1]
    def use_eraser(self):
        self.activate_button(self.erase, eraser_mode = True)
    
    
    def activate_button(self, button, eraser_mode = False):
        self.activebutton.config(relief= RAISED)
        button.config(relief = SUNKEN)
        self.activebutton = button
        self.eraser_on = eraser_mode
    
    def paint(self, event):
        self.line_width = self.scale.get()
        paint_color = "white" if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width = self.line_width, fill = paint_color,  
                                    capstyle = ROUND, 
                                    smooth = TRUE,
                                    splinesteps = 36)

        self.old_x = event
        self.old_y = event.y
    
    def reset(self,event):
        self.old_x, self.old_y = None, None




if __name__ == "__main__":
    Paint()
