from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from tkinter import ttk
import csv

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class email_idd:
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("500x200")

        lbl_title=Label(self.root,text="Change Email id",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=500,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=30)

        #----------------------------------------------label frames-------------------------------------------------------------------------------------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Enter Email Id",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=700,height=1500)
        
        lbl_ref_email=Label(labelframeleft,text="Email id: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_email.grid(row=0,column=0,sticky=W)

        entry_ref_email=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_email.grid(row=0,column=1)

        def val():

            with open('accno.csv','r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    e_acc=row[0]
                    break
            e_acc=int(e_acc)

            e_email=email.get()
            s="update master set email='{}' where account_num={}".format(e_email,e_acc)
            cursor.execute(s)

            if not(e_email == ''):
                messagebox.showinfo("showinfo","your email id  is updated")
        
        def close_win():
            val()
            root.destroy()

            

        btn=Button (self.root,text="Close",font=("times new roman",12,"bold"),padx=2,pady=6,command=close_win)
        btn.pack(side='bottom')

        email=Entry(entry_ref_email)
        email.pack()


if __name__=="__main__":
    root=Tk()
    obj=email_idd(root)
    root.mainloop()






            
