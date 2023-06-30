from tkinter import *
from PIL import Image,ImageTk
from exist_usermenu_graphics import exist_user_menu
from new_user_graphics import details
class User_Win:
    def __init__(self,root):
        self.root=root
        self.bottom= Frame(root, height=800, bg="white")
        self.bottom.pack(fill=X)
        self.root.title("IBBI Bank")
        self.root.geometry("1550x700+230+220")

        lbl_title=Label(self.root,text="USER PANEL", font=("times new roman",30,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1550,height=50)


        #-----------------------------------------------logo------------------------------------------------------------------------------------------------------
        
        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((100,40),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=2,y=5,width=90,height=40)
        
       #------------main frame ------------------------
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=50,width=1550,height=700)

        #---------------button frame ----------------------------------
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=260,height=110)


         #-------------------image-----------
        img3=Image.open(r"G:\My Drive\PROJECT BANK\wallpaper.jpg")
        img3=img3.resize((1350,590),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lblimg=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg.place(x=225,y=0,width=1350,height=600)



        #----------------------label and buttoons----------------------------
        
        lbl_user_type=Label(main_frame,text="User Type",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_user_type.place(x=0,y=0,width=230)
        
        new_user_btn=Button(btn_frame,text="New User",command=self.nuser,width=14,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        new_user_btn.grid(row=0,column=0,pady=1)
        

        existu_btn=Button(btn_frame,text="Existing User",command=self.menu,width=14,font=("times new roman",15,"bold"),bg="black",fg="gold",bd=2,cursor="hand2")
        existu_btn.grid(row=1,column=0,pady=1)
        
    def menu(self):
        self.new_window=Toplevel(self.root)
        self.app=exist_user_menu(self.new_window)


    def nuser(self):
        self.new_window=Toplevel(self.root)
        self.app=details(self.new_window)
        
        
   
          
if __name__=="__main__":
    root=Tk()
    obj=User_Win(root)
    root.mainloop()
    
