#---------this module is for removing 'unread result found error' from 'account_to_graphics' module----------------

from tkinter import *
import mysql.connector
from tkinter import messagebox
import update_closing_bal as u
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()



def update_depo(dod,e_acc2,e_amount,e_cheque_num,e_mode):
    s="INSERT INTO DEPOSIT VALUES('{}',{},{},{},'{}','{}')".format(dod,e_acc2,e_amount,e_cheque_num,e_mode,'')
    cursor.execute(s)



def check(e_acc2):
    s="SELECT ACCOUNT_NUM ,ACTIVITY FROM MASTER"
    cursor.execute(s)
    c=0
    for row in cursor:
        if row[0]==e_acc2:
            c+=1
            if not(row[1]=='A'):
                messagebox.showinfo("showinfo"," Account to which you want to transfer is inactive or closed.")
                return False       

    if c==0:
        messagebox.showinfo("showinfo","Incorrect account number entered")
        return False
    return True
        
def bal_ret(e_amount,e_acc2):
    bal_2=float(e_amount)
    s="select * from closing_bal"
    cursor.execute(s)
    for row in cursor:
        if row[0]==e_acc2:
            break
               
    bal_2+=float(row[1])
                 
    u.update(bal_2,e_acc2)

    
    
