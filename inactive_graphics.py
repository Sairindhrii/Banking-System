from tkinter import *
from datetime import date
import datetime
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

import FOR_ADMIIN as am
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()


class make_inactive():

    def __init__(self,root):
        
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("800x450")


        #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="Checking and\n making accounts inactive\nwhich were inactive for long period",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=800,height=100)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=50)


        def getVal():
            am.inactive


        getVal()
        def  close_win():
            root.destroy()

       
                
        btn=Button (self.root,text="Activity of Accounts Updated\n(click to close window)",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,padx=50,pady=10,command=close_win)
        btn.place(x=150,y=200)
            
if __name__=="__main__":
    root=Tk()
    obj=make_inactive(root)
    root.mainloop()




        
        
    
