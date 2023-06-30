from tkinter import *
from tkinter import ttk
from PIL import  Image
import mysql.connector
from PIL import ImageTk
from tkinter import messagebox
import account_pass_check as check
import csv
global passwd
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class accept:
    
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("400x200+400+400")

        lbl_title=Label(self.root,text="Password",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=400,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((101,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=30)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Enter",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=500,height=1000)
        lbl_ref_pass=Label(labelframeleft,text="Password : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_pass.grid(row=0,column=0,sticky=W)

        entry_ref_pass=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_pass.grid(row=0,column=1)


        lbl_ref_cpass=Label(labelframeleft,text="Confirm Password : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_cpass.grid(row=1,column=0,sticky=W)

        entry_ref_cpass=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_cpass.grid(row=1,column=1)


        def clear_text():
            password.delete(0,END)
            cpassword.delete(0,END)
            
            
            
        

        def val():
                
            e_pass=password.get()
            e_cpass=cpassword.get()
            #print ("pass-",e_pass,"\nconfirm pass-",e_cpass,"\npassword-",passwd)

            if (e_pass==e_cpass):
                
                if (e_pass==passwd):
                    messagebox.showinfo("showinfo","passwords  match")
                    root.destroy()
                else:
                    messagebox.showinfo("showinfo","passwords dont match. Press Reset button")
                
                
            else :
                messagebox.showinfo("showinfo","passwords dont match. Press Reset button")
                
                
               
                
        def close_win():
            val()

                
            
        btn=Button(self.root,text="Submit",command=close_win)
        btn.place(x=120,y=170)

        btn2=Button(self.root,text="Reset",command=clear_text)
        btn2.place(x=200,y=170)
        
        password=Entry(entry_ref_pass,show="*")
        password.pack()
        cpassword=Entry(entry_ref_cpass,show="*")
        cpassword.pack()
        
def Value():
    global passwd
    with open('accno.csv','r') as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            e_acc=row[0]
            passwd=check.account_num_pass_check(int(e_acc))   
            break

if __name__=="__main__":
    root=Tk()
    Value()
    obj=accept(root)
    root.mainloop()
      
