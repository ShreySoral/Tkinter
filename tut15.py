# creating radio buttons in tkinter.
from tkinter import *
from tkinter import messagebox
root= Tk()
root.geometry("455x233")
root.title("Radio Buttons tutorial")

def order():
    messagebox.showinfo("Order Recieved", f"We have recieved your order for {var.get()}. Thanks for ordering")

# var=IntVar()

var=StringVar()
var.set("Radio")
# var.set(1)
Label(root,text="What would you like to have sir?",font="lucida 19 bold",justify=LEFT,padx=14).pack()
radio=Radiobutton(root, text="Breakfast", padx=14,variable=var,value="Breakfast").pack(anchor="w")
radio=Radiobutton(root, text="Lunch", padx=14,variable=var,value="Lunch").pack(anchor="w")
radio=Radiobutton(root, text="Dinner", padx=14,variable=var,value="Dinner").pack(anchor="w")

Button(text="Order Now",command=order).pack()
root.mainloop()