from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from datetime import date
from tkinter import ttk
import update_closing_bal as u
import otp_generation as otp 
import pywhatkit
global e_acc
global e_amount
global bal

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class deposit_func:
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("500x300")


        #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="DEPOSIT AMOUNT",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=500,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((101,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=30)


        #----------------------------------------------label frames-------------------------------------------------------------------------------------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Details Required",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=500,height=1000)


        #------------------labels and entries---------------------------------------------------

        lbl_ref_num=Label(labelframeleft,text="Account Number: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_num.grid(row=0,column=0,sticky=W)

        entry_ref_num=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_num.grid(row=0,column=1)
        


        lbl_ref_amount=Label(labelframeleft,text="Amount: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_amount.grid(row=1,column=0,sticky=W)

        entry_ref_amount=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_amount.grid(row=1,column=1)
        

        #radio button
        lbl_ref_mode=Label(labelframeleft,text="Mode(C-Cash/Q-Cheque): ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_mode.grid(row=2,column=0,sticky=W)

        entry_ref_mode=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_mode.grid(row=2,column=1)
        

        lbl_ref_cheque_num=Label(labelframeleft,text="Cheque Number: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_cheque_num.grid(row=3,column=0,sticky=W)

        entry_ref_cheque_num=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_cheque_num.grid(row=3,column=1)


    


        def getValue():
            global e_acc
            global e_amount
            global bal
            flag=0
     
            #-----------account number get input and check----------------
            e_acc=acc.get()
            e_acc=int(e_acc)
            s="SELECT ACCOUNT_NUM ,ACTIVITY  FROM MASTER"
            cursor.execute(s)
            c=0
            for row in cursor:
                if row[0]==e_acc:
                    c+=1
                    if not(row[1] =='A'):
                        messagebox.showinfo("showinfo","Your Account is inactive or closed.")
                        c+=1
                    else:
                        flag=1 #correct accout number
            if c==0:
                messagebox.showinfo("showinfo","Incorrect account number entered.Re enter.")
                
            #------------------------deposit amount input---------------------------------
                
            e_amount=amount.get()

            #-------------------mode of deposit input-----------------------------------------
            e_mode=mode.get()


            e_cheque_num=cheque_num.get()
            if (e_cheque_num==""):
                e_cheque_num=0
           

            dod=date.today()


            e_cheque_num=int(e_cheque_num)
            if flag==1:
                s="INSERT INTO DEPOSIT VALUES('{}',{},{},{},'{}','{}')".format(dod,e_acc,e_amount,e_cheque_num,e_mode,'')
                cursor.execute(s)

                bal=float(e_amount)
                s="select * from closing_bal"
                cursor.execute(s)
                for row in cursor:
                    if row[0]==e_acc: #account no check
                        break
            
                bal+=float(row[1])
             
                u.update(bal,e_acc)
                           
         #this function takes all value and closes the window  
        def close_win():
            global e_acc
            global e_amount
            global bal
            getValue()
            e_amount=str(e_amount)
            e_acc=str(e_acc)
            bal=str(bal)
            
            otp.deposit_balance_sms(bal,e_acc,e_amount,"credited")

             #implement 2 mins delay loop
            
            root.destroy()
            


        btn=Button(self.root,text="Submit",padx=2,pady=6,command=close_win)
        btn.pack(side="bottom")

        acc=Entry(entry_ref_num)
        acc.pack()

        amount=Entry(entry_ref_amount)
        amount.pack()

        mode=Entry(entry_ref_mode)
        mode.pack()

        cheque_num=Entry(entry_ref_cheque_num)
        cheque_num.pack()


if __name__=="__main__":
    root=Tk()
    obj=deposit_func(root)
    root.mainloop()



          

        


        
                
                
                

        
  
            
            


        

        


        

        


        



        
