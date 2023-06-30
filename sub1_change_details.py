from tkinter import *
from tkinter import ttk
from PIL import  Image
import mysql.connector
from PIL import ImageTk
from tkinter import messagebox
import otp_generation as otp_gen
from sub2_change_details import buttons
import csv
global ret
global e_acc
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()


class details:
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("500x300+400+400")

        lbl_title=Label(self.root,text="Check Details",font=("times new roman",16,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=500,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((101,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=30)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Enter Details Accurately",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=500,height=1000)
        lbl_ref_pan=Label(labelframeleft,text="PAN NO : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_pan.grid(row=0,column=0,sticky=W)

        entry_ref_pan=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_pan.grid(row=0,column=1)


        lbl_ref_adhar=Label(labelframeleft,text="Adhar No : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_adhar.grid(row=1,column=0,sticky=W)

        entry_ref_adhar=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_adhar.grid(row=1,column=1)


        lbl_ref_otp=Label(labelframeleft,text="OTP : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_otp.grid(row=2,column=0,sticky=W)

        entry_ref_otp=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_otp.grid(row=2,column=1)



        def value():
            global ret
            global e_acc

            

            with open('accno.csv','r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    e_acc=row[0]
                    break


        
            with open('otp.csv','r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    ret=row[0]
                    break
            


            e_pan=pan.get()
            e_adhar=adhar.get()
            

            s="select pan_no,adhar_no from master where account_num={}".format(e_acc)
            cursor.execute(s)
            row=cursor.fetchone()
          
            
            if   e_pan==row[0] and e_adhar==row[1]:
                messagebox.showinfo("showinfo","Details matched")
            else:
                messagebox.showinfo("showinfo","Details dont match.")
                root.destroy()

            e_otp=otp.get()

            #otp not generated/verified 
            try :
                ret=str(ret)
            except UnboundLocalError as e:
                messagebox.showinfo("showinfo","OTP not verified")
                root.destroy()
                
                
            #wrong otp entered
            if ret==e_otp:
                messagebox.showinfo("showinfo","OTP verified")
            else:
                messagebox.showinfo("showinfo","OTP not verified")
                root.destroy()

        def close_win():

             value()
             self.new_window=Toplevel(self.root)
             self.app=buttons(self.new_window)

        btn=Button (self.root,text="Verify",font=("times new roman",12,"bold"),padx=2,pady=6,command=close_win)
        btn.pack(side='bottom')


        pan=Entry(entry_ref_pan)
        pan.pack()

        adhar=Entry(entry_ref_adhar)
        adhar.pack()

        otp=Entry(entry_ref_otp)
        otp.pack()


if __name__=="__main__":
    root=Tk()
    obj=details(root)
    root.mainloop()            







        

         
