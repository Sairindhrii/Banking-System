import mysql.connector
from datetime import date
import datetime
import convert_date as cd  #return date in datetime datatype 
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()


#interest calculation quarterly 2022-23 

def calc(f_date,t_date,bal):
    acc=[] #list to store active and savings account number  
    deposit=0.0
    withdrawal=0.0
    s="select account_num from master where activity='{}' and account_type='{}' ".format('A','S')
    cursor.execute(s)
    for row in cursor:
        acc.append(row[0])
   # print(acc)
    for i in range (len(acc)):
        acnt=acc[0]
        while f_date <= t_date:
            s="select amount from deposit where account_num={} and date_of_deposit='{}' ".format(acnt, f_date)
            cursor.execute(s)
            for row in cursor:
                if not row[0] == None:
                    deposit+=float(row[0])
            s="select amount from withdrawal where account_num={} and date_of_withdrawal='{}' ".format(acnt ,f_date)
            cursor.execute(s)
            for row in cursor :
                if not row[0]==None:
                    withdrawal+=float(row[0])
            f_date=f_date+ datetime.timedelta(days=1)
        bal+=deposit-withdrawal # after 1st quarter op_bal calculated.
        intr=((bal*4)/100.0)/4
        print(deposit,withdrawal,bal)
        #send interest smsssss
        bal+=intr
        s="insert into deposit values ('{}',{},{},{},'{}','{}') ".format(t_date,acnt,intr,0,'I',' ')
        cursor.execute(s)

    return bal,acnt

    
    
def cal_main():
    dd,d2=cd.ret_date('2022-04-01','2022-06-30')
    c_bal,acnt=calc(dd,d2,0.0)
    dd,d2=cd.ret_date('2022-07-01','2022-09-30')
    c_bal,acnt=calc(dd,d2,c_bal)
    dd,d2=cd.ret_date('2022-10-01','2022-12-31')
    c_bal,acnt=calc(dd,d2,c_bal)
    dd,d2=cd.ret_date('2023-01-01','2023-03-31')
    c_bal,acnt=calc(dd,d2,c_bal)
    s="update closing_bal set balance={} where account_num={}".format(c_bal,acnt)
    cursor.execute(s)
   









        
