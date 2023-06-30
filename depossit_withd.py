import mysql.connector
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root",database="bank")
mycon.autocommit=True
cursor=mycon.cursor()
def depo(dOd,a,amount,no,md):
    s="INSERT INTO DEPOSIT VALUES('{}',{},{},{},'{}','{}')".format(dOd,a,amount,no,md,' ')
    cursor.execute(s)

def insert_withd(dOw,a,amount,no,md):
     s="INSERT INTO WITHDRAWAL VALUES('{}',{},{},{},'{}','{}')".format(dOw,a,amount,no,md,' ')
     cursor.execute(s)
    
