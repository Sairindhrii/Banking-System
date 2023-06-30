
#---------------------------------this module is for getting details of account to which you transfer-------------------
from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from datetime import date
from tkinter import ttk
import update_closing_bal as u
import update_withdrawal as up 
import csv

import sub_account2account_graphics as sub

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class account:
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("600x300")


        #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="Account to Account transfer",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
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

        lbl_ref_amount=Label(labelframeleft,text="Amount ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_amount.grid(row=0,column=0,sticky=W)

        entry_ref_amount=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_amount.grid(row=0,column=1)

        lbl_ref_acc2=Label(labelframeleft,text="Account No (to which you want to transfer): ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_acc2.grid(row=1,column=0,sticky=W)

        entry_ref_acc2=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_acc2.grid(row=1,column=1)


        lbl_ref_cheque=Label(labelframeleft,text="Cheque No.",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_cheque.grid(row=2,column=0,sticky=W)

        entry_ref_cheque=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_cheque.grid(row=2,column=1)



        def  getValue():
            #------------------------getting the account number from which you want to transfer-----------------------
            with open('accno.csv','r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    e_acc=row[0]
                    break

            e_acc=int(e_acc) 
            e_mode='Q'
            e_cheque_num=cheque_num.get()
            dod=date.today()  #assigning today's date


            e_amount=amount.get()
            e_amount=float(e_amount)  #floating typecast
            s="select * from closing_bal"
            cursor.execute(s)
            for row in cursor:
            
                if row[0]==e_acc:
                    bal=float(row[1])
                
                    break
        
    
            if not(bal>=e_amount):
                messagebox.showinfo("showinfo","insufficient balance cannot perform transfer")
                flag=0
                root.destroy()
                
            else:
                bal -=e_amount
                
                
                if bal<=1000:
                    bal-=500
                    messagebox.showinfo("showinfo","Rs 500 has been deducted from the account due to below minimum balance.")
                flag=1
   
            
            if flag==1:
                #------------update withdrawal table for 'account from' -------------------
                up.update(dod,e_acc,e_amount,e_cheque_num,e_mode)
                u.update(bal,e_acc)   #----------updating closing balance import module


            #------------account no to which we deposit--------------------
            e_acc2=acc2.get()
            e_acc2=int(e_acc2)
       
            
            res=sub.check(e_acc2)  #for checking account number to which you want to transfer
            print(res)
            if res==False:
                messagebox.showinfo("showinfo","cannot continue transfer")
                root.destroy()

                
            if flag==1:
                sub.update_depo(dod,e_acc2,e_amount,e_cheque_num,e_mode)
                sub.bal_ret(e_amount,e_acc2)
                root.destroy()

        btn=Button(self.root,text="Submit",padx=2,pady=6,command=getValue)
        btn.pack(side="bottom")

        acc2=Entry(entry_ref_acc2)
        acc2.pack()

        amount=Entry(entry_ref_amount)
        amount.pack()

        cheque_num=Entry(entry_ref_cheque)
        cheque_num.pack()

        
if __name__=="__main__":
    root=Tk()
    obj=account(root)
    root.mainloop()

        
        

                
                
            



                

            
                


            
            
            

            
            
            
            
           
            
            
            

        

        
        
        

    

    

    



    






