# menus and submenus in tkinter
from tkinter import *
root=Tk()
root.title("Menus and Submenus")
root.geometry("733x566")

def myfunc():
    print("Hello, world!")

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


root.mainloop()