from tkinter import *
root = Tk()
root.geometry("500x400")
root.minsize(500, 400)

root.title("News Paper")
var1 = Label(text='''News Bharat''', bg="black", fg="white", font="Roboto 20 bold")
var1.pack(side=TOP, anchor="nw", fill=X)
var2 = Label(text='''Heading of the news''', bg="black", fg="yellow", font="Roboto 15 bold")
var2.pack(side=TOP, anchor="nw", fill=X)
Var = Label(text='''22 may 2021''', font="cosmicsansms 10", padx=2, pady=2, bg="white")
Var.pack(anchor="ne")

photo1 = PhotoImage(file="2.png")
Labe1 = Label(image=photo1)
Labe1.pack(side=TOP, anchor="nw", pady=30)

f = open("1.txt")
text1 = f.read()
News1 = Label(text=text1, bg="white", fg="black", font="Roboto 6", relief=SUNKEN)
News1.pack(side=BOTTOM, anchor="sw")

root.mainloop()