import mysql.connector
from datetime import date
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

def dep(date,amount,acc):
    
    s="update deposit set print='{}' where account_num={} and date_of_deposit='{}' and amount={} and print=' ' ".format('P',acc,date,amount)
    cursor.execute(s)
    

def withd(date,amount,acc):
    s="update withdrawal set print='{}' where account_num={} and date_of_withdrawal='{}' and amount={} and print=' ' ".format('P',acc,date,amount)
    cursor.execute(s)


#for returning the latest transactions 
def  last_transac(acc):
    s="select date_of_deposit from deposit where account_num={}".format(acc)
    cursor.execute(s)
    for row in cursor:
        dd=row[0]
    s="select date_of_withdrawal from withdrawal where account_num={} ".format(acc)
    cursor.execute(s)
    wd=None
    for row in cursor:
        if not row[0]==None:
            wd=row[0]
    
    #print(acc,wd,dd)
    if  not wd==None:
        if dd<wd:
            return wd
        else :
            return dd
    else:
        return dd

def update_active(acc):
    s="update master set activity='{}' where account_num={}".format('I',acc)
    cursor.execute(s)
    
        
    
