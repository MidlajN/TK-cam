# a program to use tkinter for capturing camera
from cProfile import label
from email.mime import image
import imp
from sys import implementation
from tkinter import *
from PIL import Image,ImageTk
import cv2

win = Tk()

win.geometry("1200x500")
win.title("TK_Cam")

label = Label(win)
label.grid(row=0,column=0 , padx= 3,pady=7)
cap = cv2.VideoCapture(0)

# Function to show frame
def show_frame():
    
    image = cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    img = Image.fromarray(image)

    imgtk = ImageTk.PhotoImage(image=img)
    label.imgtk = imgtk
    label.configure(image=imgtk)

    label.after(10,show_frame)

show_frame()
win.mainloop()

