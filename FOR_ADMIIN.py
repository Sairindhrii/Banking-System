#======================For admin========================
import Admin_Pass as A   #for getting admin password
import withdrawal_table as wl
import ValidityCheck as v
from datetime import date
import datetime
import mysql.connector
import update_print as pt
import interest_cal_savings as ic
import otp_generation as otp
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

#====================================functions================================
#==========================closing an account==================================
def close():   #called from user
    dOw=date.today()
    acc,p=wl.account_num_check() # checking  account number
    if acc !=-9:
        s="select balance from closing_bal where account_num={}".format(acc)
        cursor.execute (s)
        for row in cursor:
            print("Remaining balance has been paid to you :",row[0])
        amount=row[0]
        mode='C'
        
        no=0
        s="INSERT INTO WITHDRAWAL VALUES('{}',{},{},{},'{}','{}')".format(dOw,acc,amount,no,mode,' ')
        cursor.execute(s)
        s="update closing_bal set balance={} where account_num={} ".format(00.0,acc)
        cursor.execute(s)
        s="update master set activity='C' where account_num={}".format(acc)
        cursor.execute(s)
        c_date=date.today()
        s="update master set date_of_closing='{}' where account_num={}".format(c_date,acc)
        cursor.execute(s)
        otp.deposit_balance_sms(00.0,acc,amount,"closed")
#======================= as on date (daily transaction history) ==================

def   history():
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
    messagebox.showinfo("showinfo","Withdrawal:",withdrawal)
    
    
    s="select sum(amount) from deposit where date_of_deposit='{}' ".format(d)
    cursor.execute(s)
    row=cursor.fetchone()
    if row[0]==None:
        deposit=0.00
    else:
        deposit=row[0]
    print("deposit",deposit)
    messagebox.showinfo("showinfo","Deposit:",deposit)
    
    print("balance remaining in bank:", float(deposit)-float(withdrawal))
    rem_bal=float(deposit)-float(withdrawal)

    messagebox.showinfo("showinfo","Remainig balance in bank:",rem_bal)
    

    
#=====================================================    date to date=====================
def date_to_date():
    f_date=input("Enter FROM date:")
    yy=int(f_date[f_date.rfind('-')+1: :])
    dd=int(f_date[0:f_date.find('-')])
    mm=int(f_date[f_date.find('-')+1:f_date.rfind('-')])
    yy=int(f_date[f_date.rfind('-')+1: :])
    d=[dd,mm,yy]
    if not (v.valid_date(d)):
        print("Incorrect date.Enter again:")
    f_date=str(yy)+'-'+str(mm)+'-'+str(dd)
    
    t_date=input("Enter TO date:")
    yy=int(t_date[t_date.rfind('-')+1: :])
    dd=int(t_date[0:t_date.find('-')])
    mm=int(t_date[t_date.find('-')+1:t_date.rfind('-')])
    yy=int(t_date[t_date.rfind('-')+1: :])
    d=[dd,mm,yy]
    if not (v.valid_date(d)):
        print("Incorrect date.Enter again:")
    t_date=str(yy)+'-'+str(mm)+'-'+str(dd)
    
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
    print("date","           ","opening balance","          ","total deposit","                 ","total withdrawal","              ","closing balance")

    f_date = datetime.datetime.strptime(f_date, "%Y-%m-%d").date() #f_date to date format
    t_date=datetime.datetime.strptime(t_date, "%Y-%m-%d").date()   #t_date to date format 

    closebal=0
    op_bal=bal
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
            print(f_date,"       ",op_bal,"                    ",deposit,"                               ",withdrawal,"                         ",closebal)
        op_bal=closebal
 
        f_date = f_date+ datetime.timedelta(days=1)



#================================(send sms) inactive account======================================================
#if any account is inactive put I in master table database 
def inactive():
    s_date=date.today()
    s="select account_num from master"
    cursor.execute(s)
    for row in cursor:
        sys=date.today()
        sys=sys-datetime.timedelta(days=60)  #current date-60days
        d=pt.last_transac(row[0])   #d stores the last date of transaction
        if d< sys:
            pt.update_active(row[0])
    

#=============if asked by user to make account inactive account active==============
def activate():
    acc=int(input("Enter your account number  if you want to activate your account:"))
    s="update master set activity='{}' where account_num={}".format('A',acc)
    cursor.execute(s)
    print("Your account has been activated.")

#======================quarterly interest calculation====================

def interest_calculation():
    ic.cal_main()


def call_func():
    print("Admin's functions")
    print("Press 1 to check cash flow on current date.")
    print("Press 2 to to check opening/ closing/withdrawal within a range of date.")
    print("Press 3 to make an account inactive. ")
    print("Press 4 to make account active.")
    print("Press 5 to calculate interest.")
    choice=int(input("Enter choice:"))
    if choice==1:
        history()
    elif choice ==2:
        date_to_date()
    elif choice==3:
        inactive()
    elif choice==4:
        activate()
    elif choice==5:
        interest_calculation()
    else:
        print("Wrong choice entered")


