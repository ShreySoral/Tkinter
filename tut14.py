# sliders in Tkinter using Scale()
from tkinter import *
from tkinter import messagebox
root= Tk()
root.geometry("455x233")
root.title("Slider tutorial")

def getdollar():
    messagebox.showinfo("Amount in dollars", f"We have credited {myslider2.get()} dollars to your account")
    # print(f"We have credited {myslider2.get()} dollars to your bank account. Thank you for banking with us")
# myslider=Scale(root, from_=0, to=100)
# myslider.pack()
Label(root,text="How many dollars do you want?").pack()

myslider2=Scale(root, from_=0, to=100,orient=HORIZONTAL,tickinterval=50)
myslider2.set(50)
myslider2.pack()



Button(root,text="Get dollars",pady=10,command=getdollar).pack()

root.mainloop()