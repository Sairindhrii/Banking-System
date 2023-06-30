import mysql.connector
import ValidityCheck as v
import deposit_table as dep
from datetime import date

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()
#----------------------------------------Entering details--------------------------------------------------------------------------
def master():
    print("Enter your details:")
    name= input("Enter your name:")
    # age limit 18 to 80 years
    dob=input("enter date of birth (dd-mm-yyyy):")
    while True:
        yy=int(dob[dob.rfind('-')+1: :])
        today=date.today()
        y=today.year
        if not( y-yy >= 18 and y-yy <=80):
            print("Not appropriate age entered.")
            exit(0)
        else:
            dd=int(dob[0:dob.find('-')])
            mm=int(dob[dob.find('-')+1:dob.rfind('-')])
            yy=int(dob[dob.rfind('-')+1: :])
            d=[dd,mm,yy]
            if not (v.valid_date(d)):
                print("Enter again.")
            else:
                break
    #reversing the dob
    dob=str(yy)+'-'+str(mm)+'-'+str(dd)

    f_name=input("Enter your guardian's name:")
    n=input("Enter your nominee's name:")
    r=input("Enter your relation to your nominee:")
    add=input("Enter address :")
    lm=input("Enter landmark:")
    city=input("Enter city:")
    while True:
        pin=input("Enter pin code:")
        if (not (v.pin_code(pin))):
            print("Re enter pin code:")
        else:
            break
    state=input("Enter state:")
    while True:
        g=input("Enter gender (M(m)/F(f)/T(t):")
        if (not (v.gender(g))):
            print("Re enter gender.")
        else:
            break
    while True:
        mob=input("Enter your mobile no:")
        if (not (v.mobile_n(mob))):
             print("Re enter mobile number.")
        else:
            break
    while True:
        ad=input("Enter adhar number:")
        if not(v.adhar_no(ad)):
            print("Re enter adhar number.")
        else:
            break

    while True :
        while True:
            pd=input("Enter your password( must be atleast 8 digit, should contain 1 upper case, 1 lower case , 1 digit and 1 special character):")
            if not(v.passwd(pd)) :
                print("Re Enter password.")
            else:
            
                break
        while True:
            cpd=input("Confirm password:")
            if not(v.passwd(cpd)) :
                print("Re Enter confirm password.")
            else:
                break
        if not(pd==cpd):
            print("Re Enter password and Confirm Password!")
        else:
        
            break
          
    while True:
        pn=input("Enter pan number:")
        if not(v.pan(pn)):
            print("Re Enter pan number.")
        else:
            break
        
    acc=v.acc_no()
    dop=date.today()
    act='A'
    doc='0000-00-00'
    print("\n\n----DISPLAYING YOUR DETAILS----")
    print("Name:",name,"\nYour Account Number:",acc,"\nDob-:",dob,"\nGuardian's Name:",f_name,"\nNominee:",n,"Relation:",r,"\nAddress:",add,"\nLandMark:",lm)
    print("City:",city,"\nPin Code:",pin,"\nState:",state,"\nGender:",g,"\nMobile number:",mob)
    print("Adhar number:",ad,"\nPan number:",pn,"\nDate of Opening:",dop,"\nState of Activity:",act)
    print("\n\n")


    
    #------------------------------------------------------------------------------------------entering the data in master table------------------------------------------------------------------------------------------------------
    s="INSERT INTO MASTER VALUES ( {},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(acc,name,act,f_name,n,r,add,lm,city,pin,state,g,mob,ad,dob,pd,pn,dop,doc)
    cursor.execute(s)

    dump,b=dep.deposit()
    s="INSERT INTO CLOSING_BAL VALUES ({},{})".format(acc,b)
    cursor.execute(s)








