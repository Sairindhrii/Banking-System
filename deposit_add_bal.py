import deposit_table as d
import update_closing_bal as u
import mysql.connector
import otp_generation as otp 
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

def add():
    acc,b=d.deposit()
    if acc !=-9:
        b1=b=float(b)
        s="select * from closing_bal"
        cursor.execute(s)
        for row in cursor:
            if row[0]==acc: #account no check
                break
        b+=float(row[1])  
        u.update(b,acc)
        otp.deposit_balance_sms(b,acc,b1,"credited")
        
        
        
    
