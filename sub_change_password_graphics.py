from tkinter import *
from tkinter import ttk
from PIL import  Image
import mysql.connector
from PIL import ImageTk
from tkinter import messagebox
import account_pass_check as check
import csv
import ValidityCheck as v
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class accept:
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("600x250+400+400")

        lbl_title=Label(self.root,text=" Password",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=600,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((101,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=30)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Enter",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=600,height=1000)
        
        lbl_ref_pass=Label(labelframeleft,text="Enter Old Password : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_pass.grid(row=0,column=0,sticky=W)

        entry_ref_pass=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_pass.grid(row=0,column=1)


        lbl_ref_cpass=Label(labelframeleft,text="Confirm Old Password : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_cpass.grid(row=1,column=0,sticky=W)

        entry_ref_cpass=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_cpass.grid(row=1,column=1)

        text = Label(labelframeleft, text="New Password must be of min 8 length\n& must contain 1 digit,1 spl character,\n1 uppercase & 1 lower case.")
        text.place(x=350,y=70)

    
        label1 = Label(labelframeleft, text="Helvetica", relief="solid", bd=1, font=("Helvetica", 16,"bold"),justify=LEFT)


        lbl_ref_npass=Label(labelframeleft,text="Enter New Password : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_npass.grid(row=2,column=0,sticky=W)

        entry_ref_npass=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_npass.grid(row=2,column=1)


        lbl_ref_ncpass=Label(labelframeleft,text="Confirm New Password : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_ncpass.grid(row=3,column=0,sticky=W)

        entry_ref_ncpass=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_ncpass.grid(row=3,column=1)
                        
            
            

        def val():
            with open('accno.csv','r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    e_acc=row[0]
                    break
            
            passwd=check.account_num_pass_check(int(e_acc))

            e_acc=int(e_acc)
            
            e_pass=password.get()
            e_cpass=cpassword.get()
            new_pass=npass.get()
            new_cpass=ncpass.get()
            
            if (e_pass==e_cpass==passwd):
                
                messagebox.showinfo("showinfo","old passwords  match")
                
                if (new_pass==new_cpass):
                    ret=v.passwd(new_pass)
                    if ret==True:
                        messagebox.showinfo("showinfo","New Passwords  match. New password will be updated")
                        s="update  master set password='{}' where account_num={}".format(new_pass,e_acc)
                        cursor.execute(s)
                    else:
                        messagebox.showinfo("showinfo","New Passwords dont match or Password rules not followed")
                        root.destroy()
                        
                        
                
                
            else :
                messagebox.showinfo("showinfo","old passwords dont match.")
                root.destroy()
            

                
        def close_win():
            val()
            root.destroy()
            
        btn=Button(self.root,text="Submit",command=close_win)
        btn.pack(side='bottom')
        
        password=Entry(entry_ref_pass,show="*")
        password.pack()
        
        cpassword=Entry(entry_ref_cpass,show="*")
        cpassword.pack()

        npass=Entry(entry_ref_npass,show="*")
        npass.pack()

        ncpass=Entry(entry_ref_ncpass,show="*")
        ncpass.pack()

        
        
    

if __name__=="__main__":
    root=Tk()
    obj=accept(root)
    root.mainloop()
      
