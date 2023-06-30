import mysql.connector
from datetime import date
import ValidityCheck as v
import update_closing_bal as u
import depossit_withd as depp
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root",database="bank")
mycon.autocommit=True
cursor=mycon.cursor()
def deposit():#account number check
    while True:
        a=int(input("Enter account number:"))
        s="SELECT ACCOUNT_NUM ,NAME,ACTIVITY  FROM MASTER"
        cursor.execute(s)
        c=0
        for row in cursor:
            if row[0]==a:
                c+=1
              #  print("Account holder name:",row[1])
                
                
                if not(row[2] =='A'):
                        print("Your Account is inactive or closed.")
                        c+=1
                        a=-9
                break
        if c==0:
            print("Incorrect account number entered.Re enter.")
        else:
            break
    #date of deposit 
    dOd=date.today()
    amount=float(input("Enter the amount:"))
    while True:
        md=input("Enter the mode of deposit of money(C for cash / Q for cheque):" )
        if not(v.mode(md)):
            print("Wrong mode entered.")
        else :
            break
    #cheque number   
    if md=='Q' or md=='q':
        no=int(input("Enter the cheque number:"))
    else:
        no=0
    md=md.capitalize()
    depp.depo(dOd,a,amount,no,md)
    #s="INSERT INTO DEPOSIT VALUES('{}',{},{},{},'{}','{}')".format(dOd,a,amount,no,md.capitalize(),' ')
    #cursor.execute(s)
    return a,amount

#-----------------------send sms-----------------------------
#dump,dump2=deposit()

