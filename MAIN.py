#==========================MAIN============================================
import FOR_ADMIIN  as ad
import FOR_USER as user
import Admin_Pass as ap
def main_call():
    print("User interface or Admin interface?")
    ch=input("Enter 'u' for user / 'a' for admin .")
    if ch=='u' or ch=='U' :
        user.user_main()
    elif ch=='a' or ch=='A':
        print("Admin password is required")
        pas=input("enter admin pass:")
        if pas==ap.admin():
            ad.call_func()
        else:
            print("Wrong admin password entered.")
    else:
        print("Wrong choice entered.")

    
