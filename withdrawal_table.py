import mysql.connector
from datetime import date
import ValidityCheck as v
import update_closing_bal as u
import depossit_withd as depp
import closingbal_and_withdrawal_check as x
import otp_generation as otp
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()
p='' ''
acc=0
def account_num_check():
    global p
    global acc
    #account number check
    while True:
        acc=int(input("Enter  account number:"))
        s="SELECT ACCOUNT_NUM ,NAME,ACTIVITY,PASSWORD  FROM MASTER where account_num={}".format(acc)
        cursor.execute(s)
        c=0
        row=cursor.fetchone()
        if row[0]==acc:
            c+=1
            print("Account holder name:",row[1])
            p=row[3] #password extract
                
        if not(row[2] =='A'):
            print("Your Account is inactive or closed.")
            c+=1
            acc=-9
            break
        
        if c==0:
            print("Incorrect account number entered.Re enter.")
        else:
            break
    
    return acc,p

def withdrawal(a):
    flagg=0
    global p
    global acc
    #date of withdrawal
    dOw=date.today()
    #mode of withdrawal of money
    if  a=="nt": #ie if not account to account transfer
        while True:
            md=input("Enter the mode of withdrawal of money(C for cash / Q for cheque):" )
            if not(v.mode(md)):
                print("Wrong mode entered.")
            else :
                break
        
        if md=='Q' or md=='q': # cheque number
            no=int(input("Enter the cheque number:"))
        else:
            no=0
    else : # in case of account to account transfer always transfer by cheque
        no=int(input("Enter cheque number:"))
        md='q'
            
    #password check
    d=1
    c=1
    flag=0
    while True:
        pas=input("Enter  password:")
        conpas=input("Confirm password:")
        if pas==conpas:
            if p==pas:
                amount=float(input("Enter the amount :"))
                b=x.check(amount,acc)
                if (b!=-1): #withdrawal and closing bal module called
                    u.update(b,acc)
                    otp.deposit_balance_sms(b,acc,amount,"debited")
                    break
                else:
                    print("Cannot withdraw as closing balance is less than withdrawal amount")
                    flagg=1
                    break
            elif c==3:
                print("Wrong password entered.Try later.")
                flag=1
                break
            else:
                print("Re enter  password.")
                c+=1
        elif d==3:
            print("Wrong password. Try later.")
            flag=1
            break
        else:
            print("Re enter  password.")
            d+=1
    if not(flag==1):
        md=md.capitalize()
        depp.insert_withd(dOw,acc,amount,no,md)
        
    return flagg,amount,md,no



#----------------------send sms------------------------






