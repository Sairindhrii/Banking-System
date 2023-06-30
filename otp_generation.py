import mysql.connector
import random
import pywhatkit
from datetime import date
import datetime
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

def generate_otp(acc):
    a=True

    otp=random.randint(1000,9999)
    otp_msg="Hello User. Your otp:"+str(otp)
    hour=datetime.datetime.now().hour #current hour
    minute=datetime.datetime.now().minute #current minute
    second=datetime.datetime.now().second #current second 
    s="select name, mobile_no from master where account_num={}".format(acc)
    cursor.execute(s)
    for row in cursor:
        mob='+91'+row[1]
                
    second=second+85
    minute+=second//60
    hour+=minute//60
    minute %=60
    second%=60
    pywhatkit.sendwhatmsg(mob,otp_msg ,hour,minute)

    return otp


def account_balance(acc):
    s="select mobile_no from master where account_num={}".format(acc)
    cursor.execute(s)
    row=cursor.fetchone()
    
    s2="select balance from closing_bal where account_num={}".format(acc)
    cursor.execute(s2)
    row2=cursor.fetchone()
    
    mob="+91"+row[0] #mobile number
    
    hour=datetime.datetime.now().hour
    minute=datetime.datetime.now().minute
    second=datetime.datetime.now().second
    
    second=second+85
    minute+=second//60
    hour+=minute//60
    minute %=60
    second%=60

    msg="Your account balance:"+str(row2[0])
    pywhatkit.sendwhatmsg(mob,msg,hour,minute)
    
def deposit_balance_sms(balance,acc,amount,status):
    s="select mobile_no from master where account_num={}".format(acc)
    cursor.execute(s)
    row=cursor.fetchone()
    mob="+91"+row[0] #mobile number

    hour=datetime.datetime.now().hour
    minute=datetime.datetime.now().minute
    second=datetime.datetime.now().second
    
    second=second+85
    minute+=second//60
    hour+=minute//60
    minute %=60
    second%=60

    
    dt=str(date.today())
    print(type(balance),balance,type(amount),amount,type(acc),acc)
    msg="A/c : "+"XX"+acc[2:]+"  "+status+"   with Rs: "+amount+"   on  "+dt+"\nAvailable balance:"+balance

    pywhatkit.sendwhatmsg(mob,msg,hour,minute)
    

def     withdrawal(bal,e_acc,status,amount):
    e_acc=str(e_acc)
    bal=str(bal)
    amount=str(amount)
    s="select mobile_no from master where account_num={}".format(e_acc)
    cursor.execute(s)
    row=cursor.fetchone()
    mob="+91"+row[0] #mobile number

    hour=datetime.datetime.now().hour
    minute=datetime.datetime.now().minute
    second=datetime.datetime.now().second
    
    second=second+85
    minute+=second//60
    hour+=minute//60
    minute %=60
    second%=60

    
    dt=str(date.today())

    msg="A/c : "+"XX"+e_acc[2:]+"  "+status+"   Rs: "+amount+"   on  "+dt+"\nAvailable balance:"+bal

    pywhatkit.sendwhatmsg(mob,msg,hour,minute)
    
    
    
