import withdrawal_table as wl
#password check
def password_check():
    print("Your account number and password(old) are required.")
    acc,p=wl.account_num_check() #for checking the account number
    if acc !=-9:
        #for checking password
        d=1
        c=1
        flag=0
        while True:
            pas=input("Enter  password(old):")
            conpas=input("Confirm  password(old):")
            if pas==conpas:
                if p==pas:
                    print("Password(old) has been verified.")
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
        return acc,p #return account num and old password

