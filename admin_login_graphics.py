from tkinter import *
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from tkinter import ttk
import Admin_Pass as ap
from Admin_menu_graphics import admin_menu

class admin_login():
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("700x500")


        

        #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="Admin Login",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=700,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
            
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="ENTER",font=("times new roman",15,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=760,height=1000)
        
              
        lbl_ref_pass=Label(labelframeleft,text="Password : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_pass.grid(row=0,column=0,sticky=W)

        entry_ref_pass=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_pass.grid(row=0,column=1)

      


        lbl_ref_cpass=Label(labelframeleft,text="Confirm  Password : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_cpass.grid(row=1,column=0,sticky=W)

        entry_ref_cpass=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_cpass.grid(row=1,column=1)

        def val():
            e_pass=password.get()
            e_cpass=cpassword.get()

            passwd=ap.adminn()
            print(passwd)
            if passwd==e_pass==e_cpass:
                messagebox.showinfo("showinfo","Admin Passwords Matched")
                self.new_window=Toplevel(self.root)
                self.app=admin_menu(self.new_window)
                
            else:
                messagebox.showinfo("showinfo","Admin Passwords don't Match")
                root.destroy()
                
        
        btn=Button(self.root, text="Submit Details", padx=2, pady=6,command=val)
        btn.pack(side="bottom")   

        password=Entry(entry_ref_pass,show="*")
        password.pack()    


        cpassword=Entry(entry_ref_cpass,show="*")
        cpassword.pack()


        


if __name__=="__main__":
    root=Tk()
    obj=admin_login(root)
    root.mainloop()
