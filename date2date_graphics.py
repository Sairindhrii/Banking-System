from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from tkinter import ttk
import csv
from from_date_graphics import from_date
from to_date_graphics import to_date
import Admin_Pass as A   #for getting the opening balance 
from datetime import date
import datetime
from date2date_display_graphics import date_to_date_display
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()


class date_to_date:
    def __init__ (self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("600x300")


        def from_open():
            self.new_window=Toplevel(self.root)
            self.app=from_date(self.new_window)

        def to_open():
            self.new_window=Toplevel(self.root)
            self.app=to_date(self.new_window)

        def display():
            self.new_window=Toplevel(self.root)
            self.app=date_to_date_display(self.new_window)
             
        
        #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="Select the Range of Dates accurately",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=600,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
            
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=45)

        #----------------------------------------------label frames-------------------------------------------------------------------------------------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Select Dates ",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=600,height=1500)


        btn=Button(self.root,text="Select 'From Date' ", padx=2,pady=7,command=from_open)
        btn.place(x=30,y=100)

        btn=Button(self.root,text="Select 'To Date' ", padx=2,pady=7,command=to_open)
        btn.place(x=30,y=150)

        btn=Button(self.root,text="Display ", padx=2,pady=7,command=display)
        btn.place(x=30,y=200)


       
        
        def  close_win():
                
            
            root.destroy()

       
                
        btn=Button (self.root,text="Close Window",padx=2,pady=6,command=close_win)
        btn.pack(side='bottom')
                
            


if __name__=="__main__":
    root=Tk()
    obj=date_to_date(root)
    root.mainloop()

            
     
     


        
