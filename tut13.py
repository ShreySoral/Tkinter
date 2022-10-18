# Messagebox in tkinter
from tkinter import messagebox
from tkinter import *
root = Tk()
root.title("Menus and Submenus")
root.geometry("733x566")

def myfunc():
    print("Hello, world!")

def help():
    print("I will help you")
    messagebox.showinfo("Help", "I will help you with this GUI.")

def rate():
    print("Rate us")
    value=messagebox.askquestion("Was your experience good?", "You used this GUI was your experience good?")
    # print(value)
    if value=="yes":
        msg="Great. Rate us on app store please"
    else:
        msg="Tell us what went wrong. We will call you soon"
    messagebox.showinfo("Experience", msg)

def divya():
    ans=messagebox.askretrycancel("Divya se dosti karlo", "Sorry Divya nahi banegi aapki dost")
    if ans:
        print("Retry karne pe bhi kuch nahi hoga")
    else:
        print("Bahut badiya bhai cancel kardiya warna pitte")
# use these to create a non dropdown menu
# my_menu=Menu(root)
# my_menu.add_command(label="File",command=myfunc)
# my_menu.add_command(label="Exit",command=quit)
# root.config(menu=my_menu)

mainmenu=Menu(root)

m1=Menu(mainmenu,tearoff=0)
m1.add_command(label="New project",command=myfunc)
m1.add_command(label="Save",command=myfunc)
m1.add_separator()
m1.add_command(label="Save as",command=myfunc)
m1.add_command(label="Print",command=myfunc)
mainmenu.add_cascade(label="File",menu=m1)

root.config(menu=mainmenu)


m2=Menu(mainmenu,tearoff=0)
m2.add_command(label="Cut",command=myfunc)
m2.add_command(label="Copy",command=myfunc)
m2.add_separator()
m2.add_command(label="Paste",command=myfunc)
m2.add_command(label="Find",command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit",menu=m2)

m3=Menu(mainmenu,tearoff=0)
m3.add_command(label="Help",command=help)
m3.add_command(label="Rate us",command=rate)
m3.add_command(label="Befriend Divya",command=divya)
mainmenu.add_cascade(label="Help",menu=m3)
root.config(menu=mainmenu)

root.mainloop()