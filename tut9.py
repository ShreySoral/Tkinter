from tkinter import *
# Create the root window
# Travel Form Using Checkbuttons & Entry Widget
root = Tk()
def getvals():
    print("Submitting Form")
    print(f"{name_value.get(), phone_value.get(), gender_value.get(), emergency_value.get(), paymentmode_value.get(), food_service.get()}")
    with open("records.txt") as f:
        f.write(f"{name_value.get(), phone_value.get(), gender_value.get(), emergency_value.get(), paymentmode_value.get(), food_service.get()}\n")
root.geometry("644x344")
root.resizable(False,False)
# root.configure(bg="lightgreen")
# heading
label=Label(root,text="Welcome",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)

# text for the form
name=Label(root,text="Name")
phone=Label(root,text="Phone")
gender=Label(root,text="Gender")
emergency=Label(root,text="Emergency Contact")
paymentmode=Label(root,text="Payment Mode")

# pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# tkinter variables for storing entries for our form
name_value=StringVar()
phone_value=StringVar()
gender_value=StringVar()
emergency_value=StringVar()
paymentmode_value=StringVar()

food_service=IntVar()


# entries for our form
name_entry=Entry(root,textvariable=name_value)
phone_entry=Entry(root,textvariable=phone_value)
gender_entry=Entry(root,textvariable=gender_value)
emergency_entry=Entry(root,textvariable=emergency_value)
paymentmode_entry=Entry(root,textvariable=paymentmode_value)


# packing the entries
name_entry.grid(row=1,column=3)
phone_entry.grid(row=2,column=3)
gender_entry.grid(row=3,column=3)
emergency_entry.grid(row=4,column=3)
paymentmode_entry.grid(row=5,column=3)


# checkbox and packing it
foodservice=Checkbutton(text="Want to prebook your meals?",variable=food_service)
foodservice.grid(row=6,column=3)

# button and packing it and assigning it a command
button=Button(text="Submit to Travel",command=getvals).grid(row=7,column=3)


root.mainloop()