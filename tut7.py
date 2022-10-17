from tkinter import *
# Entry widget and grid layout in Tkinter.
def getvals():
    print(user_value.get())
    print(password_value.get())
root= Tk()
root.geometry("655x333")

user=Label(root,text="Username")
user.grid()
password=Label(root,text="Password")
password.grid(row=1)

# Entry widget in tkinter.

# variable classes
# booleanvar, doublevar, intvar, stringvar


user_value=StringVar()
password_value=StringVar()

user_entry=Entry(root,textvariable=user_value)
user_entry.grid(row=0,column=1)

password_entry=Entry(root,textvariable=password_value)
password_entry.grid(row=1,column=1)


button=Button(text="Submit",command=getvals).grid()
root.mainloop()