#================================================USER=================================================================
# closing balance check, statement check(pass book update), deposit, withdrawal, account to account transfer
#---------------------------------------------------------------------------prerequisites---------------------------------------------------------------------------------------------------
import mysql.connector
import master_table as m
import withdrawal_table as wl
import deposit_add_bal as dab
import ValidityCheck as v
import pass_book as pb
import account_to_account as aTa
import PasswordCheck as pc
import Admin_Pass as A
import FOR_ADMIIN as fa
import generate_password as gp
import otp_generation as otp
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()
#----------------------------------------------------------------------------functions---------------------------------------------------------------------------------------------------------
#===============================closing balance checking ==================================================================
def closing():
    print("Your account number and password are required.")
    acc,p=wl.account_num_check() #for checking the account number
    #for checking password
    if acc != -9: #inactive account or closed
        d=1
        c=1
        flag=0
        while True:
            pas=input("Enter your password:")
            conpas=input("Confirm your password:")
            if pas==conpas:
                if p==pas:
                    print("Your password has been verified.")
                    break
                    
                elif c==3:
                    print("Wrong password entered.Try later.")
                    flag=1
                    break
                else:
                    print("Re enter your password.")
                    c+=1
            elif d==3:
                print("Wrong password. Try later.")
                flag=1
                break
            else:
                print("Re enter your password.")
                d+=1
        if flag==0:
            s="select balance from closing_bal where account_num={}".format(acc)
            cursor.execute (s)
            for row in cursor:
                account_bal=row[0]
            otp.account_balance(acc,account_bal)
            print("Your account balance has been sent to your mobile whatsapp number.")
            
                
        
#================================for depositing amount to your account===============================
def depositing():
    
    dab.add()
    print("The amount  has been deposited.")

#================================for withdrawing amount from your account=============================
def withdrawing():
    a='nt' # not account to account transfer
    print("Your account number and password are required.")
    acc,dump2=wl.account_num_check()
    if acc !=-9:
        flagg,dump,dump2,dump3=wl.withdrawal(a)
        if flagg ==0:
            print("Withdrawal succesfully completed.")
    
    
#============================Pass book updation=======================================    
def statement():

    print("Your account number and password are required.")
    acc,p=wl.account_num_check() #for checking the account number
    if acc !=-9:  #inactive/closed account
        #for checking password
        d=1
        c=1
        flag=0
        while True:
            pas=input("Enter  password:")
            conpas=input("Confirm  password:")
            if pas==conpas:
                if p==pas:
                    print("Password has been verified.")
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
        if flag==0:
            pb.pbook(acc)            
         
#================account to account transfer==============================     
def transfer():
    aTa.account()
    

#===================change password=======================
def change_password():
    acc,oldp=pc.password_check() #return old password and account number
    pd=A.admin() #known to admin only
    ad=input("Enter admin password:")  #visuality offfffffff
    if not(pd==ad):
        print("Admin password dont match")
    else:
        print("Admin password verified")
    otp.generate_otp(acc)
    f=True
    while f :
        while True:
            npd=input("Enter new password( must be atleast 8 digit, should contain 1 upper case, 1 lower case , 1 digit and 1 special character):")
            if not(v.passwd(npd)) :
                print("Re Enter new password.")
            else:
                break
        while True:
            ncpd=input("Confirm new password:")
            if not(v.passwd(ncpd)) :
                print("Re Enter new confirm password.")
            else:
                break
        if not(npd==ncpd) and (oldp==npd) :
            print("Re Enter new password and Confirm Password!")
        else:
            f=False
            s="update master set password='{}' where account_num={}".format (npd, acc)
            cursor.execute(s)
            print("Password successfully updated")
                
#===============closing your account============================    
def close_account():
    fa.close()
    
    print("Your account has been closed.")
    
    

#===================================forgot password====================================
def forgot ():
    
    gp.forgot_gen_pass(0)
    
#======================================change address details=================================
def change ():
    bul,acc=gp.forgot_gen_pass(1)
    otp.generate_otp(acc)
    #send and receive otp
    if bul==True:
        add=input("enter new address:")
        landmark=input("enter landmark:")
        city=input("enter city :")
        while True:
            pin=input("Enter pin code:")
            if (not (v.pin_code(pin))):
                print("Re enter pin code:")
            else:
                break
        state=input("enter state:")
        s="update  master set address='{}', landmark='{}',city='{}',pin_code ='{}',state='{}' where account_num={}".format(add,landmark,city,pin,state,acc)
        cursor.execute(s)
        print("Your address has been changed successfully!")
    
    else :
        print("cant change address. details dont match!")
    
    
    
    
    
    
#----------------------------------------------------------------------------driver section------------------------------------------------------------    
def user_main():
    print("WELCOME ")
    user=input("Are you a new User?(enter y or Y for yes / n or N for no):")
    if user=='Y' or user=='y' :
        m.master()
    elif user=='n' or user=='N' :
        print("Enter the activity you want to perform.")
        print("Press 1 for closing balance checking")
        print("Press 2 for depositing amount to your account")
        print("Press 3 for withdrawing amount from your account")
        print("Press 4 for account to account transfer")
        print("Press 5 for statement checking")
        print("Press 6 for changing your password(must not forget old password)")
        print("Press 7 if you want  to close your account")
        print("Press 8 if you have forgotten your password")
        print("Press 9 if you want to change your addresss details")
        choice=int(input("Enter choice:"))
        if choice == 1:
            closing()
        elif choice==2:
            depositing()
        elif choice ==3:
            withdrawing()
        elif choice==4:
            transfer()
        elif choice==5:
            statement()
        elif choice ==6:
            change_password()
        elif choice==7:
            close_account()
        elif choice==8:
            forgot()
        elif choice==9:
            change()
        else:
            print("Wrong choice entered.")
            

