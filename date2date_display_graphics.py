from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from tkinter import ttk
import csv
from from_date_graphics import from_date
from to_date_graphics import to_date
import Admin_Pass as A   #for getting the opening balance 
from datetime import date
import datetime

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()


class date_to_date_display:
    def __init__ (self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("750x750")


        def from_open():
            self.new_window=Toplevel(self.root)
            self.app=from_date(self.new_window)

        def to_open():
            self.new_window=Toplevel(self.root)
            self.app=to_date(self.new_window)    
        
        #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="Date To Date Display Closing Balance,\nDeposit and Withdrawal\nwithin a range of date",font=("times new roman",12,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=750,height=75)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
            
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=110,height=70)


        def getValue():

            with open ('from_date.csv', 'r') as f:
                csv_reader=csv.reader(f)
                for row in csv_reader:
                    f_date=row[0]
                    break

            with open ('to_date.csv', 'r') as f:
                csv_reader=csv.reader(f)
                for row in csv_reader:
                    t_date=row[0]
                    break

            print(f_date,t_date)
  
            deposit=0
            withdrawal=0
            s="select sum(amount) from deposit where date_of_deposit < '{}' ".format(f_date)
            cursor.execute(s)
            for row in cursor:
                if not row[0]==None:
                    deposit+=row[0]
            s="select sum(amount) from withdrawal where date_of_withdrawal < '{}' ".format(f_date)
            cursor.execute(s)
            for row in  cursor:
                if not row[0]==None:
                    withdrawal+=row[0]
            bal=A.opening_balance()+deposit-withdrawal


            sensor_value="Date\t\tOpening\t\tTotal \t\tTotal\t\tClosing"
            p=sensor_value
            text=Label(root,text=p,font=("times new roman",12,"bold"),fg="black")
            text.place(x=25,y=100)
            sensor_value="\t\tBalance \t\tDeposit \t\tWithdrawal \tBalance"
            q=sensor_value
            text=Label(root,text=q,font=("times new roman",12,"bold"),fg="black")
            text.place(x=25,y=125)
            


      
            
            f_date = datetime.datetime.strptime(f_date, "%Y-%m-%d").date() #f_date to date format
            t_date=datetime.datetime.strptime(t_date, "%Y-%m-%d").date()   #t_date to date format 

            closebal=0
            op_bal=bal
            i=150
            while( f_date <= t_date):
                deposit=0
                withdrawal=0
                s="select sum(amount) from deposit where date_of_deposit = '{}' ".format(f_date)
                cursor.execute(s)
                for row in cursor:
                    if not row[0]==None:
                        deposit+=row[0]
                s="select sum(amount) from withdrawal where date_of_withdrawal = '{}' ".format(f_date)
                cursor.execute(s)
                for row in cursor:
                    if not row[0]==None:
                        withdrawal+=row[0]
                
                closebal=op_bal+deposit-withdrawal
               
                if deposit !=0 or withdrawal !=0:

                    sensor_value=str(f_date)+"\t"+str("%10.2f"%op_bal)+"\t"+str("%10.2f"%deposit)+"\t"+str("%10.2f"%withdrawal)+"\t         "+str("%10.2f"%closebal)
                    x1=sensor_value
                    text=Label(root,text=x1,font=("times new roman",12,"bold"),fg="black",relief=RIDGE)
                    text.place(x=25,y=i)
                    i=i+30
                
                op_bal=closebal
         
                f_date = f_date+ datetime.timedelta(days=1)



        getValue()
        def  close_win():
                
            
            root.destroy()

       
                
        btn=Button (self.root,text="Close Window",padx=2,pady=6,command=close_win)
        btn.pack(side='bottom')











if __name__=="__main__":
    root=Tk()
    obj=date_to_date_display(root)
    root.mainloop()








        
