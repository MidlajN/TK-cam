# a program to use tkinter for capturing camera
from ast import Return
from cProfile import label
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
import cv2

class TKCam:
    def __init__(self):
        
        # Tkinter GUI
        self.win = tk.Tk()
        self.win.geometry("1200x500")
        self.win.title("TK_Cam")


        # Tkinter GUI left part
        self.left_side = tk.Frame(self.win)
        self.label = Label(self.win)
        self.label.grid(row=0,column=0 , padx= 5,pady=7)
        self.label.pack(side=tk.LEFT)
        self.left_side.pack()

        self.cap = cv2.VideoCapture(0)


    def get_frame(self):
            if self.cap.isOpened():
                ret ,frame = self.cap.read()
                return ret , cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)


    # Function to show frame
    def show_frame(self):
        ret,self.image = self.get_frame()
        if ret:
            img = Image.fromarray(self.image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)
        self.win.after(10, self.show_frame)
   

    def run(self):
        self.show_frame()
        self.win.mainloop()
 
       
def main():
    tk_cam = TKCam()
    tk_cam.run()

if __name__ == '__main__':
    main()

