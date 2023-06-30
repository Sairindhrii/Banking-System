from tkinter import *
from datetime import date
import datetime
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import interest_cal_savings as call
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()


class cal_int:

    def __init__(self,root):
        
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("700x450")


        #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="Calculating Interest of Savings Account",font=("times new roman",17,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=800,height=100)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=50)


        def getVal():
            call.cal_main()


        getVal()
        def  close_win():
            root.destroy()

       
                
        btn=Button (self.root,text="Interests Calculated\n(click to close window)",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE,padx=50,pady=10,command=close_win)
        btn.place(x=150,y=200)
            
if __name__=="__main__":
    root=Tk()
    obj=cal_int(root)
    root.mainloop()
