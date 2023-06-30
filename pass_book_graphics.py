from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from datetime import date
from tkinter import ttk
import csv
import otp_generation as otp
from password_graphics import accept
global e_acc
import pywhatkit
import pass_book as pb
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class passbook:
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("600x300")

        def getValue1():
            global e_acc
            #-----------account number get input and check----------------
            e_acc=acc.get()
            e_acc=int(e_acc)
            s="SELECT ACCOUNT_NUM ,ACTIVITY FROM MASTER"
            cursor.execute(s)
            
            c=0
            for row in cursor:
                if row[0]==int(e_acc):
                    
                    c+=1
                    print(e_acc)
                    with open('accno.csv', 'w') as f:
                        w = csv.writer(f)
                       
                        hd=[e_acc]
                        w.writerow(hd)
                        f.close()
                        
                    
                    if not(row[1] =='A'):
                        messagebox.showinfo("showinfo","Your Account is inactive or closed.")
                        root.destroy()
                        
            if c==0:
                messagebox.showinfo("showinfo","Incorrect account number entered.Re enter.")
                root.destroy()


        def passwd():
             getValue1()
             self.new_window=Toplevel(self.root)
             self.app=accept(self.new_window)

         #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="Account No and password check",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=600,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=30)

        #----------------------------------------------label frames-------------------------------------------------------------------------------------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Details Required",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=600,height=1500)


         #------------------labels and entries---------------------------------------------------

        lbl_ref_num=Label(labelframeleft,text="Account No ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_num.grid(row=0,column=0,sticky=W)

        entry_ref_num=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_num.grid(row=0,column=1)
        
        #----------------------------button for checking password------------------------------------------------------------
        btn=Button(self.root,text="Check Password",padx=2,pady=6,command=passwd)
        btn.place(x=40,y=120)

        def getValue():
            global e_acc


        #this function takes all value and closes the window  
        def close_win():
            global e_acc
            getValue()


            pb.pbook(e_acc)
            messagebox.showinfo("showinfo","Pass Book updated")
            root.destroy()


            
        btn=Button(self.root,text="Submit",padx=2,pady=6,command=close_win)
        btn.pack(side="bottom")
            
        acc=Entry(entry_ref_num)
        acc.pack()



        
if __name__=="__main__":
    root=Tk()
    obj=passbook(root)
    root.mainloop()
            
