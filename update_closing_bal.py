import mysql.connector
from datetime import date
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

def update(b,acc):
    s="update closing_bal set balance={} where account_num={} ".format(b,acc)
    cursor.execute(s)
