from tkinter import *
import tkinter.messagebox as tmsg
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('600x600')
        self.title('Window.')

    def text(status):
        t1 = Label(text='Please click the below button',anchor='e')
        t1.pack(side=TOP)
    
    def createbutton(self):
        self.b1 = Button(self,text='Submit Now',command=self.click)
        self.b1.pack()

    def click(self):
        print('It works.')
        tmsg.showinfo('Information','This button is for only demo purpose.')

if __name__=='__main__':
    window = GUI()
    window.text()
    window.createbutton()
    window.mainloop()