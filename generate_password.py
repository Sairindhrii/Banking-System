import mysql.connector
import random
import withdrawal_table as wl
import convert_date as cv
import PasswordCheck as pc
mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()


def forgot_gen_pass(counter):
    flagg=1
    print("Enter all the details correctly!")
    if counter==1:
        acc,dupp=pc.password_check()
    else:
        acc,dup=wl.account_num_check()
        otp.generate_otp(acc)
    if acc != -9:
        e_dob=input("Enter your Dob (yyyy-mm-dd):")
        e_mob=input("Enter your mobile  number :")
        e_adhar=input("Enter your adhar number:")
        e_pan=input("Enter your pan number:")
        e_dob=cv.date(e_dob) #return in datetime then string format 
        s="select dob,mobile_no,adhar_no,pan_no,name  from master where account_num={}".format (acc)
        cursor.execute(s)
        for row in cursor :
            dob=str(row[0]) #dob in date time format 
            mob=row[1]
            adhar=row[2]
            pan=row[3]
            name=row[4]
        if  mob==e_mob and adhar==e_adhar  and e_pan== pan and dob==dob :
            #---------------------------------------send and confirm otp by user------------------------------------------
            if counter==1:
                return True,acc
            dob=str(dob)
            yy=int(dob[0:dob.find('-')])
            mm=int (dob[ dob.find('-')+1: dob.rfind('-')])
            dd=int(dob[dob.rfind('-')+1::])
            d=yy-mm+dd
            c=random.randint(65,90)
            s=random.randint(97,122)
            l=[36,37,38,42,64,94]
            sp=random.randint(0,5)
            z=' '
            z=name[0]+chr(c)+chr(s)+chr(l[sp])+str(d)
            print("Your new password is:",z) #send by sms
       
        else :
            if counter==1:
                return False,0
            print("Wrong details entered . Cannot change password.")
            flagg=0
        if flagg==1:
            s="update master set password='{}' where account_num={}".format(z,acc)
            cursor.execute(s)
    
    
    

