# Handling events in Tkinter
from tkinter import *
def Shrey(event):
    print(f"You clicked on the button at {event.x}, {event.y}")
root=Tk()
root.title("Events in Tkinter")
root.geometry("644x344")

widget=Button(root,text="Click Me Please")
widget.pack()

widget.bind('<Button-1>',Shrey)
widget.bind('<Double-1>',quit)
root.mainloop()