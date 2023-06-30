import mysql.connector
import random
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

#===============checking of master table attributes================
def valid_date(date): #input date in list
    month=[0,31,28,31,30,31,30,31,31,30,31,30,31] 
    if date[1]>12: #valid month
        return False
    if date[2]%4==0 and date[2]%100!=0 or date[2]%400==0: #leap year
       month[2]=29
    if date[0]>=1 and date[0]<= month[date[1]]: #valid day
        return True
    else:
        return False
    
def pin_code(pin):
    if not(len(pin)==6):
        return False
    return True

def pan (n):
    if not(len(n)==10):
        print("pan number not valid!")
        return False
    elif not(ord(n[0])>=65 and ord(n[0])<=90  and ord(n[9])>=65 and ord(n[9])<=90):
            print("pan number not valid!")
            return False
    else:
        return True

def adhar_no(a):
    if not( len(a)==12):
        print(" adhar number not valid!")
        return False
    return True 

def mobile_n(m):
    if not(len(m)==10):
        print(" mobile number invalid!")
        return False
    return True

def gender(g):
    if not(g=='M' or g=='m' or  g=='F' or g=='f' or g=='T' or g=='t'):
        print("invalid gender!")
        return False
    return True

def passwd(p):
    cap=0
    small=0
    dig=0
    spl=0
    if not(len(p))>=8:
           print("PASSWORD NOT AVAILABLE")
           return False
    else:
        for i in range (len(p)):
            if ord(p[i])>=65 and ord(p[i])<=90:
                cap+=1
            elif ord(p[i])>=97 and ord(p[i])<=122:
                small+=1
            elif ord(p[i])>=48 and ord(p[i])<=57:
                dig+=1
            elif ord(p[i])==32:
                space+=1
            else:
                spl+=1
        if cap>=1 and small>=1 and dig >=1 and spl>=1:
            return True
        else:
            return False

def acc_no(): #return 6 digit acc no randomly
    s="select count(*) from master"
    cursor.execute(s)
    for row in cursor:
        num=row[0] #counting the no of records in the table
    if not(num==0):
        a=True
        while a: #checking if the randomly generated acc num present in the table
            acc_num=random.randint(100000,999999)
            cursor.execute("SELECT ACCOUNT_NUM FROM MASTER")
            for row in cursor:
               if not(row[0]==acc_num):
                   a=False
                   break
    else:
        acc_num=random.randint(100000,999999)
        
    return acc_num
    
 #===========checking of deposit table attributes=====================           
def mode(m):
    if not(m=='C' or m=='c' or m=='q' or m=='Q'):
        return False
    else :
        return True
            
                


    
