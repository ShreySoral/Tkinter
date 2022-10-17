from tkinter import *
# GUI is a collection of packed widgets
root = Tk()
# width x height
root.geometry("644x434")
# width, height
root.minsize(300, 100)
# width, height
root.maxsize(1200, 988)
# Label
label = Label(text="This is my GUI",foreground="green")
label.place(x=10, y=0)
root.mainloop()