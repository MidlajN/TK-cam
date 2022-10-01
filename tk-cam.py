# a program to use tkinter for capturing camera
from ast import Return
from cProfile import label
import time
import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
from PIL import Image,ImageTk
import cv2

class TKCam:
    def __init__(self):
        
        # Tkinter GUI
        self.win = tk.Tk()
        self.win.geometry("1200x480")
        self.win.title("TK_Cam")


        # Tkinter GUI left part
        self.left_side = tk.Frame(self.win)
        self.label = Label(self.win)
        # self.label.grid(row=0,column=0 , padx= 0,pady=0)
        self.label.pack(side=tk.LEFT)
        self.left_side.pack()
        
        # Tkinter GUI right part
        self.right_side = tk.Frame(self.win)
        self.label_for_fps = tk.Label(self.right_side , text="")

        self.font_title = tkfont.Font(family='Helvetica', size=20 , weight='bold')



        # frame rate
        self.start_time = time.time()
        self.fps_show = 0
        self.fps = 0
        self.frame_time = 0
        self.frame_start_time = 0


        # for getting camera access
        self.cap = cv2.VideoCapture(0)

    def GUI_info (self):
        tk.Label(self.right_side, text= "TK-Cam", font=self.font_title).grid(row=0,
                column=0, columnspan=3, sticky=tk.W, padx=5, pady=20)

        tk.Label(self.right_side, text="FPS : ").grid(row=1, column=0, columnspan=2, sticky=tk.W, padx=5, pady=2)
        self.label_for_fps.grid(row=1, column=2, sticky=tk.W)

        self.right_side.pack()


    def get_frame(self):
            if self.cap.isOpened():
                ret ,frame = self.cap.read()
                return ret , cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)


    # Function to show frame
    def show_frame(self):
        ret,self.image = self.get_frame()
        self.update_fps()
        if ret:

            img = Image.fromarray(self.image)
            imgtk = ImageTk.PhotoImage(image=img)
            self.label.imgtk = imgtk
            self.label.configure(image=imgtk)
        self.win.after(10, self.show_frame)

    def update_fps(self):
        now = time.time()

        # refresh fps
        if str(self.start_time).split('.')[0] != str(now).split('.')[0]:
            self.fps_show = self.fps
        self.start_time = now
        self.frame_time = now - self.frame_start_time
        self.fps = 1.0 / self.frame_time
        self.frame_start_time = now

        self.label_for_fps["text"] = str(self.fps.__round__(2))
   

    def run(self):
        self.show_frame()
        self.GUI_info()
        self.win.mainloop()
 
       
def main():
    tk_cam = TKCam()
    tk_cam.run()

if __name__ == '__main__':
    main()

