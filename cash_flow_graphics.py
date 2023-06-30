from tkinter import *
from datetime import date
import datetime
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class check_cash_flow():
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("700x500")

        #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="Today's Cash Flow",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=700,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
            
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        def getValue():
            d=date.today()
            print("Cash Flow on:",d)

         
            
            s="select sum(amount) from withdrawal where date_of_withdrawal='{}' ".format(d)
            cursor.execute(s)
            row=cursor.fetchone()
            if row[0]==None:
                withdrawal=0.00
            else:
                withdrawal=row[0]
            print("withdrawal:",withdrawal)
            withdrawal=str(withdrawal)
            

            
            s="select sum(amount) from deposit where date_of_deposit='{}' ".format(d)
            cursor.execute(s)
            row=cursor.fetchone()
            if row[0]==None:
                deposit=0.00
            else:
                deposit=row[0]
            print("deposit",deposit)
  
            
            print("balance remaining in bank:", float(deposit)-float(withdrawal))
            rem_bal=float(deposit)-float(withdrawal)

            deposit=float(deposit)

            withdrawal=float(withdrawal)

            sensor_value="Cash Flow on: "+str(d)
            p=sensor_value
            sensor_value="Deposit:                     "+str("%10.2f"%deposit)
            x=sensor_value
            sensor_value="Withdrawal:               "+str("%10.2f"%withdrawal)
            y=sensor_value
            sensor_value="Remainig Balance:  "+str("%10.2f"%rem_bal)
            z=sensor_value

            text=Label(root,text=p,font=("times new roman",25,"bold"),fg="black",relief=RIDGE)
            text.place(x=90,y=150)
            text=Label(root,text=x,font=("times new roman",25,"bold"),bg="black",fg="gold",relief=RIDGE)
            text.place(x=90,y=200)
            text=Label(root,text=y,font=("times new roman",25,"bold"),bg="black",fg="gold",relief=RIDGE)
            text.place(x=90,y=250)
            text=Label(root,text=z,font=("times new roman",25,"bold"),bg="black",fg="gold",relief=RIDGE)
            text.place(x=90,y=300)

    
        

            
        getValue()
        def  close_win():

            root.destroy()

       
                
        btn=Button (self.root,text="Close",padx=2,pady=6,command=close_win)
        btn.pack(side='bottom')

          

            

                    

                

                    

if __name__=="__main__":
    root=Tk()
    obj=check_cash_flow(root)
    root.mainloop()

