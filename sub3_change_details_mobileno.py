from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from tkinter import ttk
import csv
import ValidityCheck as v
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class mobile_num:
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("500x200")

        lbl_title=Label(self.root,text="Change Mobile No.",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=500,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=30)

        #----------------------------------------------label frames-------------------------------------------------------------------------------------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Enter new mobile number",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=700,height=1500)
        
        lbl_ref_mob=Label(labelframeleft,text="Mobile Number: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_mob.grid(row=0,column=0,sticky=W)

        entry_ref_mob=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_mob.grid(row=0,column=1)

        def val():
            e_mobile=0
            with open('accno.csv','r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    e_acc=row[0]
                    break
            e_acc=int(e_acc)
            e_mob=mob.get()

            ret=v.mobile_n(e_mob)
            if  ret==True:
                s="update master set mobile_no='{}' where account_num={}".format(e_mob,e_acc)
                cursor.execute(s)
                messagebox.showinfo("showinfo","your mobile number is updated")
            else:
                if not (e_mobile==0):
                    messagebox.showinfo("showinfo","Incorrect mobile number")
                root.destroy()
            

            
            

        def close_win():
            val()
            
            root.destroy()

        btn=Button (self.root,text="Close",font=("times new roman",12,"bold"),padx=2,pady=6,command=close_win)
        btn.pack(side='bottom')

        mob=Entry(entry_ref_mob)
        mob.pack()


if __name__=="__main__":
    root=Tk()
    obj=mobile_num(root)
    root.mainloop()





        

