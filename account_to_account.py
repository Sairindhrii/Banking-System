import mysql.connector
import withdrawal_table as wl
import update_closing_bal as u
import depossit_withd as depp
from datetime import date
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()
def account():
    a='t '# account to account transfer
    print("Account.no FROM which you want to tansfer is required.")
    acc,p=wl.account_num_check()
    if acc !=-9:
        print("The password of account from which you want to withdraw amount is required:")
        f,amount,mode,no=wl.withdrawal(a)
        if f==0:
            print("Withdrawal from",acc,"successful!")
            print("Account.no TO which you want to tansfer is required .")
            acc2,dump=wl.account_num_check()
            dOd=date.today()
            mode=mode.capitalize()
            depp.depo(dOd,acc2,amount,no,mode)
            
            s="select * from closing_bal"
            cursor.execute(s)
            for row in cursor:
                if row[0]==acc2: #account no check
                    break
            amount+=float(row[1])  
            u.update(amount,acc2)
            print("Deposition to ", acc2, "successful!")
        else:
            print("Transfer cannot take place.")
    

