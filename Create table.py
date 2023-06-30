import mysql.connector
mycon=mysql.connector.connect(host="localhost",user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()
s= "USE bank"
cursor.execute(s)

def master():
    s= "CREATE TABLE MASTER( ACCOUNT_NUM  INTEGER  NOT NULL PRIMARY KEY, ACCOUNT_TYPE  VARCHAR(15) ,\
          NAME VARCHAR(25) NOT NULL , ACTIVITY VARCHAR(1), GUARDIAN VARCHAR(25), NOMINEE VARCHAR(25), RELATION VARCHAR(25), ADDRESS VARCHAR(25) ,\
          LANDMARK VARCHAR(25), CITY VARCHAR(10), PIN_CODE VARCHAR(8) NOT NULL , STATE VARCHAR(15), GENDER  VARCHAR(1),MOBILE_NO VARCHAR(10) NOT NULL,\
          EMAIL VARCHAR(25),ADHAR_NO VARCHAR(12) NOT NULL, DOB DATE NOT NULL, PASSWORD VARCHAR(20) NOT NULL, PAN_NO VARCHAR(12),\
          DATE_OF_OPENING DATE NOT NULL, DATE_OF_CLOSING DATE)"
    cursor.execute(s)

def deposit():
    s="CREATE TABLE DEPOSIT ( DATE_OF_DEPOSIT  DATE  NOT  NULL,  ACCOUNT_NUM  INTEGER  NOT NULL,\
         AMOUNT  decimal(10,2)  NOT NULL , CHEQUE_NUM INTEGER, MODE VARCHAR(1)  NOT NULL, PRINT CHAR(1) )"
    cursor.execute(s)

def withdrawal():
    s="CREATE TABLE WITHDRAWAL ( DATE_OF_WITHDRAWAL  DATE NOT  NULL,  ACCOUNT_NUM  INTEGER  NOT NULL,\
    AMOUNT  decimal(10,2)  NOT NULL ,  CHEQUE_NUM INTEGER, MODE  VARCHAR(1)  NOT NULL , PRINT CHAR(1) )"
    cursor.execute(s)

def closing_bal():
    s=" CREATE TABLE CLOSING_BAL( ACCOUNT_NUM INTEGER NOT NULL, BALANCE decimal(10,2) NOT NULL)"
    cursor.execute(s)

master()
deposit()
withdrawal()
closing_bal()
