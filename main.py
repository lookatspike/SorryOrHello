from tkinter import *
import os
#from PIL import ImageTk,Image


root = Tk()
root.title("Sorry/Hello ")


def hello():
    hello_label = Label (root, text= "Hello " + myTextbox.get())
    hello_label.pack()
def sorry():
    hello_label = Label (root, text= "I'm so sorry,  " + myTextbox.get())
    hello_label.pack()

myLabel = Label(root, text = "Enter with the name of the person you want to apologize to / say hello to")
myLabel.pack()
myTextbox = Entry(root, width=30)
myTextbox.pack()
myButton1 = Button(root, text="Say Hello", command=hello)
myButton2 = Button(root, text="Say Sorry", command=sorry)

myButton1.pack()
myButton2.pack()




root.mainloop()