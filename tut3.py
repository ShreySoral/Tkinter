from tkinter import *
from PIL import Image,ImageTk
root = Tk()
root.title("Tut3")
root.geometry("400x400")
# display image
image=Image.open("download.jpg")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()
root.mainloop()