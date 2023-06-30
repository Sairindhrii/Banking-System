import mysql.connector


mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()



def account_num_pass_check(e_acc):
    
    s="select account_num,password from master"
    cursor.execute(s)
    for row in cursor:

        if row[0]==e_acc :
            pd=row[1]

            break
    
    return pd

        
#account_num_pass_check(123456)
