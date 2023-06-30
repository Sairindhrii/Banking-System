from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from tkinter import ttk
from sub3_change_details_mobileno import mobile_num
from sub3_change_details_emailid import email_idd
from sub3_change_details_nominee import nominee_name
from sub3_change_details_address import address
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class buttons:
    def __init__(self,root):
        
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("500x500")

        def mobile():
            self.new_window=Toplevel(self.root)
            self.app=mobile_num(self.new_window)
        def email_chng():
            self.new_window=Toplevel(self.root)
            self.app=email_idd(self.new_window)
        def nominee_chng():
            self.new_window=Toplevel(self.root)
            self.app=nominee_name(self.new_window)
        def address_chng():
            self.new_window=Toplevel(self.root)
            self.app=address(self.new_window)
            
            

        lbl_title=Label(self.root,text="Change Details",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=500,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=30)

        #----------------------------------------------label frames-------------------------------------------------------------------------------------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Click on Button which field you want to change",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=700,height=1500)

        btn=Button(self.root,text="Change Mobile No.",background="light blue",font=("times new roman",12,"bold"),padx=2,pady=6,command=mobile)
        btn.place(x=30,y=90)

        btn=Button(self.root,text="Change Email Id",background="light blue",font=("times new roman",12,"bold"),padx=2,pady=6,command=email_chng)
        btn.place(x=30,y=150)

        btn=Button(self.root,text="Change Nominee",background="light blue",font=("times new roman",12,"bold"),padx=2,pady=6,command=nominee_chng)
        btn.place(x=30,y=210)

        btn=Button(self.root,text="Change Address ",background="light blue",font=("times new roman",12,"bold"),padx=2,pady=6,command=address_chng)
        btn.place(x=30,y=270)





        def  close_win():
            root.destroy()
                
        btn=Button (self.root,text="Close",font=("times new roman",12,"bold"),padx=2,pady=6,command=close_win)
        btn.pack(side='bottom')


       
        





if __name__=="__main__":
    root=Tk()
    obj=buttons(root)
    root.mainloop()


    
