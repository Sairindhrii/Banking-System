#check if the closing balance of the customer is less than the withdrawal
import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()
def check(amount,acc):
    s="select * from closing_bal"
    cursor.execute(s)
    for row in cursor:
        if row[0]==acc: #account no check
            break
    b=float(row[1])
   
    if not(b>=amount):
        return -1
    else:
        b-=amount
        if b<=1000:
            b-=500
            print("Rs 500 has been deducted from the account due to below minimum balance.")
    return b


            
        
    
