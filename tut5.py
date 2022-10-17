from tkinter import *
# frames in tkinter
root = Tk()
root.geometry("655x333")
frame = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
frame.pack(side=LEFT, fil="y")

frame2 = Frame(root, borderwidth=9, bg="grey", relief=SUNKEN)
frame2.pack(side=TOP, fill="x")
l1 = Label(frame, text="project tkinter - Pycharm")
l1.pack(pady=142)

l2 = Label(frame2, text="welcome to sublime text",
           font="comicsansms 19 bold", fg="red")
l2.pack()
root.mainloop()
