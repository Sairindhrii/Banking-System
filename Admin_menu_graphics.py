from tkinter import *
from PIL import Image,ImageTk
from inactive_graphics import make_inactive
from activate_graphics import make_active
from calculate_interest_graphics import cal_int
from cash_flow_graphics import check_cash_flow
from date2date_graphics import date_to_date
class admin_menu:
    def __init__(self,root):
        self.root=root
        self.bottom= Frame(root, height=800, bg="white")
        self.bottom.pack(fill=X)
        self.root.title("IBBI Bank")
        self.root.geometry("1200x430+100+100")

        lbl_title=Label(self.root,text="ADMIN MENU", font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1200,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=2,y=5,width=100,height=40)


        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=50,width=500,height=370)
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=45,width=500,height=900)
        
        lbl_user_type=Label(main_frame,text="choose from below",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_user_type.place(x=0,y=0,width=500)
        
        new_user_btn=Button(btn_frame,text="1. check today's cash flow",command=self.check_flow,width=30,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        new_user_btn.grid(row=0,column=0,pady=1)
        

        existu_btn=Button(btn_frame,text="2.check opening/closing/withdrawal\nwithin a date range",command=self.displaying,width=30,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        existu_btn.grid(row=1,column=0,pady=1)

        acc_btn=Button(btn_frame,text="3.make account inactive",command=self.inactiv,width=30,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        acc_btn.grid(row=2,column=0,pady=1)

        pbook_btn=Button(btn_frame,text="4.make account active",command=self.activ,width=30,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        pbook_btn.grid(row=3,column=0,pady=1)

        cbal_btn=Button(btn_frame,text="5.calculate interest",command=self.calc,width=30,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        cbal_btn.grid(row=4,column=0,pady=1)

    def inactiv(self):
        self.new_window=Toplevel(self.root)
        self.app=make_inactive(self.new_window)
    def activ(self):
        self.new_window=Toplevel(self.root)
        self.app=make_active(self.new_window)
    def calc(self):
        self.new_window=Toplevel(self.root)
        self.app=cal_int(self.new_window)
    def check_flow(self):
        self.new_window=Toplevel(self.root)
        self.app=check_cash_flow(self.new_window)

    def displaying(self):
        self.new_window=Toplevel(self.root)
        self.app=date_to_date(self.new_window)
        


    
        
if __name__=="__main__":
    root=Tk()
    obj=admin_menu(root)
    root.mainloop()

