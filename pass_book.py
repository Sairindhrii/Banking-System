import mysql.connector
from datetime import date
import datetime
import update_print as pt 
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

#============================== deposits and withdrawals between from - to dates==============================================
def pbook(acc):
    rec=[]
    l=[]

    #dd_date deposit date
    #wd_date  withdrawal date
    deposit=0
    withdrawal=0
    op_bal=0
    #deposit sum of  transactions  printed 
    c=0
    s="select date_of_deposit, amount,print from deposit where account_num={} order by date_of_deposit asc, print desc ".format(acc)
    cursor.execute(s)
    for row in cursor:
        if not row[0]==None:
            if c==0:
                dd_date=row[0]
                c+=1
            if row[2]=='P':
                deposit+=row[1]
            
            
    #withdrawal   sum of transactions  printed
    c=0
    s2="select date_of_withdrawal, amount,print  from withdrawal where  account_num={} order by date_of_withdrawal asc, print desc ".format(acc)
    cursor.execute(s2)
    for row in cursor:
        if not row[0]==None :
            if c==0:
                wd_date=row[0]
                c+=1
            if row[2]=='P':
                withdrawal+=row[1]


    op_bal=deposit-withdrawal
    
    
    if dd_date < wd_date:
        current_date=dd_date
    else:
        current_date=wd_date
    s_date=date.today() #system date
    
    while current_date <= s_date:
        s="select print,amount from deposit where account_num={} and date_of_deposit='{}' order by date_of_deposit asc, print desc ".format(acc,current_date)
        cursor.execute(s)
        for row in cursor:
            if row[1] != None:
                if row[0] !='P':
                    op_bal+=row[1]  
                    print(current_date,  row[1] , op_bal)
                    pt.dep(current_date, row[1], acc)
                     
                    


                    
        s="select print,amount from withdrawal where account_num={} and date_of_withdrawal='{}' order by date_of_withdrawal asc, print desc ".format(acc,current_date)
        cursor.execute(s)
        for row in cursor:
            if row[1] != None:
                if row[0] !='P':
                    op_bal-=row[1]  
                    print(current_date,  row[1], op_bal)
                    pt.withd(current_date, row[1], acc)
                    
        current_date=current_date+ datetime.timedelta(days=1)
        
                
    
















