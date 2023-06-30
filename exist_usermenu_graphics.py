from tkinter import *
from PIL import Image,ImageTk
from deposit_user_graphics import deposit_func
from withdrawal_user_graphics import withdrawal_func
from account_to_account_graphics import account_to_account
from closing_balance_graphics import closing_bal
from change_password_graphics import change_pass
from forgot_pass_graphics import forgot_pass
from close_account_graphics import close_account
from change_details_graphics import change_det
from pass_book_graphics import passbook
class exist_user_menu:
    def __init__(self,root):
        self.root=root
        self.bottom= Frame(root, height=800, bg="white")
        self.bottom.pack(fill=X)
        self.root.title("IBBI Bank")
        self.root.geometry("1295x710+100+100")

        lbl_title=Label(self.root,text="USER MENU", font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1300,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=2,y=5,width=100,height=40)


        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=50,width=600,height=2000)
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=45,width=1000,height=3000)
        
        lbl_user_type=Label(main_frame,text="choose from below",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_user_type.place(x=0,y=0,width=700)
        
        new_user_btn=Button(btn_frame,text="1. deposit amount ",command=self.depo,width=30,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        new_user_btn.grid(row=0,column=0,pady=1)
        

        existu_btn=Button(btn_frame,text="2. withdraw amount ",command=self.withd,width=30,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        existu_btn.grid(row=1,column=0,pady=1)

        acc_btn=Button(btn_frame,text="3.account to account amount transfer",command=self.acc,width=30,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        acc_btn.grid(row=2,column=0,pady=1)

        pbook_btn=Button(btn_frame,text="4.pass book update",command=self.pb,width=30,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        pbook_btn.grid(row=3,column=0,pady=1)

        cbal_btn=Button(btn_frame,text="5.check closing balance",command=self.c_bal,width=30,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        cbal_btn.grid(row=4,column=0,pady=1)

        chng_btn=Button(btn_frame,text="6.change password",command=self.chng_pas,width=30,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        chng_btn.grid(row=5,column=0,pady=1)

        chng_add_btn=Button(btn_frame,text="7.change details",command=self.chng_det,width=30,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        chng_add_btn.grid(row=6,column=0,pady=1)

        close_btn=Button(btn_frame,text="8.close account",command=self.close_acc,width=30,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        close_btn.grid(row=7,column=0,pady=1)

        fp_btn=Button(btn_frame,text="9.forgot password?",command=self.forgo_pas,width=30,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        fp_btn.grid(row=8,column=0,pady=1)


    def depo(self):
        self.new_window=Toplevel(self.root)
        self.app=deposit_func(self.new_window)
    def withd(self):
        self.new_window=Toplevel(self.root)
        self.app=withdrawal_func(self.new_window)
    def acc(self):
        self.new_window=Toplevel(self.root)
        self.app=account_to_account(self.new_window)
    def c_bal(self):
        self.new_window=Toplevel(self.root)
        self.app=closing_bal(self.new_window)
    def chng_pas(self):
        self.new_window=Toplevel(self.root)
        self.app=change_pass(self.new_window)
    def forgo_pas(self):
        self.new_window=Toplevel(self.root)
        self.app=forgot_pass(self.new_window)
    def close_acc(self):
        self.new_window=Toplevel(self.root)
        self.app=close_account(self.new_window)
    def chng_det(self):
        self.new_window=Toplevel(self.root)
        self.app=change_det(self.new_window)
        
    def pb(self):
        self.new_window=Toplevel(self.root)
        self.app=passbook(self.new_window)
        
        
        
    
        
   


if __name__=="__main__":
    root=Tk()
    obj=exist_user_menu(root)
    root.mainloop()
