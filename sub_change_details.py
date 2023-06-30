from tkinter import *
from tkinter import ttk
from PIL import  Image
import mysql.connector
from PIL import ImageTk
from tkinter import messagebox
from sub1_change_details import details
import account_pass_check as check
import otp_generation as otp_gen
import csv
global ret


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

         

                        
            
            

        def val():
            
            with open('accno.csv','r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    e_acc=row[0]
                    break
                
            passwd=check.account_num_pass_check(int(e_acc))
            
            e_pass=password.get()
            e_cpass=cpassword.get()

            if (e_pass==e_cpass==passwd):
                
                messagebox.showinfo("showinfo","passwords  match")
                messagebox.showinfo("showinfo","OTP will be sent to you shortly")
                ret=otp_gen.generate_otp(e_acc)
                with open('otp.csv', 'w') as f:
                    w = csv.writer(f)
                    hd=[ret]
                    w.writerow(hd)
                    f.close()
                
                
    
            else :
                messagebox.showinfo("showinfo","passwords dont match.")
                root.destroy()

        

        
                
        def close_win():
            val()
            self.new_window=Toplevel(self.root)
            self.app=details(self.new_window)
      
            
        btn=Button(self.root,text="Submit",command=close_win)
        btn.place(x=120,y=170)
        
        password=Entry(entry_ref_pass,show="*")
        password.pack()
        cpassword=Entry(entry_ref_cpass,show="*")
        cpassword.pack()
        
    

if __name__=="__main__":
    root=Tk()
    obj=accept(root)
    root.mainloop()
      
