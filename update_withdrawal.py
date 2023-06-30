import mysql.connector

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

def update(dod,e_acc,e_amount,e_cheque_num,e_mode):
    s="INSERT  INTO WITHDRAWAL VALUES('{}',{},{},{},'{}','{}')".format(dod,e_acc,e_amount,e_cheque_num,e_mode,'')
    cursor.execute(s)

