# canvas widget in tkinter
from tkinter import *
root = Tk()
canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")
root.title("Canvas widget in Tkinter Tutorial")
root.resizable(False,False)

can_widget=Canvas(root,width=canvas_width,height=canvas_height)
can_widget.pack()

# the line goes from the point x1,y1 to x2,y2
can_widget.create_line(0,0,800,400,fill="red")
can_widget.create_line(0,400,800,0,fill="red")

# to create a rectangle specify parameters in this order - corners of top left 
# and corners of bottom right
can_widget.create_rectangle(3,5,700,300,fill="blue")

# create text
can_widget.create_text(200,200,text="Python")


# create an oval
can_widget.create_oval(344,233,244,355,fill="green")
root.mainloop()