from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from tkinter import ttk
import otp_generation as otp_gen
import ValidityCheck as v
from calendar_graphics import dateee
import csv
global e_acc
global ret

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class forgot_pass:
    global  counter
    counter= False
    

    def __init__(self,root):
        
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("700x600")
        

        def getValue1():
            global e_acc
            global counter
       
            e_acc=acc.get()
            e_acc=int(e_acc)
            counter=True
            s="SELECT ACCOUNT_NUM ,ACTIVITY FROM MASTER"
            cursor.execute(s)
            
            c=0
            for row in cursor:
                if row[0]==e_acc:
                    c+=1
                    
                    if not(row[1] =='A'):
                        messagebox.showinfo("showinfo","Your Account is inactive or closed.")
                        root.destroy()
                        
            if c==0:
                messagebox.showinfo("showinfo","Incorrect account number entered.Re enter.")
                root.destroy()
                
        def otp_generation():
            global e_acc
            
            global ret
            getValue1()
            
            ret=otp_gen.generate_otp(e_acc)   #automatic otp generated nd sent in whatsapp

        def dob_open():
            self.new_window=Toplevel(self.root)
            self.app=dateee(self.new_window)



        #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="Forgot Password",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=700,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=30)

        #----------------------------------------------label frames-------------------------------------------------------------------------------------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Accurate Details Required",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=700,height=1500)


         #------------------labels and entries---------------------------------------------------

        lbl_ref_num=Label(labelframeleft,text="Account Number: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_num.grid(row=0,column=0,sticky=W)

        entry_ref_num=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_num.grid(row=0,column=1)
        
        #----------------------------button for checking password------------------------------------------------------------
        btn=Button(self.root,text="Generate OTP",padx=2,pady=6,command=otp_generation )
        btn.place(x=450,y=80)

        
        

        #radio button
        lbl_ref_mob=Label(labelframeleft,text="Mobile No: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_mob.grid(row=1,column=0,sticky=W)

        entry_ref_mob=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_mob.grid(row=1,column=1)
        

        lbl_ref_pan=Label(labelframeleft,text="Pan No: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_pan.grid(row=2,column=0,sticky=W)

        entry_ref_pan=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_pan.grid(row=2,column=1)

        lbl_ref_adhar=Label(labelframeleft,text="Adhar No: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_adhar.grid(row=3,column=0,sticky=W)

        entry_ref_adhar=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_adhar.grid(row=3,column=1)

        lbl_ref_otp=Label(labelframeleft,text="OTP:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_otp.grid(row=4,column=0,sticky=W)

        entry_ref_otp=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_otp.grid(row=4,column=1)

        text = Label(labelframeleft, text="Password must be of min 8 length\n& must contain 1 digit,1 spl character,\n1 uppercase & 1 lower case.")
        text.place(x=390,y=230)

        label1 = Label(labelframeleft, text="Tkinter", fg="red")
        label1 = Label(labelframeleft, text="Helvetica", relief="solid", bd=1, font=("Helvetica", 16,"bold"),justify=LEFT)


        lbl_ref_npass=Label(labelframeleft,text="Enter New Password:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_npass.grid(row=6,column=0,sticky=W)

        entry_ref_npass=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_npass.grid(row=6,column=1)

        lbl_ref_ncpass=Label(labelframeleft,text="Confirm new password:",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_ncpass.grid(row=7,column=0,sticky=W)

        entry_ref_ncpass=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_ncpass.grid(row=7,column=1)

        btn=Button(self.root,text="SELECT DOB", padx=2,pady=7,command=dob_open)
        btn.place(x=450,y=200)

     
        def getValue():
            global e_acc
            global ret
            
            e_mob=mob.get()
            e_pan=pan.get()
            e_adhar=adhar.get()
            

            s="select dob,mobile_no,pan_no,adhar_no from master where account_num={}".format(e_acc)
            cursor.execute(s)
            row=cursor.fetchone()
            
            with open ('dob.csv', 'r') as f:
                csv_reader=csv.reader(f)
                for row in csv_reader:
                    e_dob=row[0]
                    break
      
            e_dob=str(e_dob)
            dobb=str(row[0])

            print("printing")
            print("enter values",e_dob,type(e_dob),e_pan,type(e_pan),e_mob,type(e_mob),e_adhar,type(e_adhar))
            print("sql values",dobb,type(dobb),row[1],type(row[1]),row[2],type(row[2]),row[3],type(row[3]))
            
            

              
            
            if e_dob==dobb and e_mob==row[1] and e_pan==row[2] and e_adhar==row[3]:
                messagebox.showinfo("showinfo","Details matched")
            else:
                messagebox.showinfo("showinfo","Details dont match.")
                root.destroy()

            e_otp=otp.get()
         
            ret=str(ret)

            print(ret, e_otp)

            if ret==e_otp:
                messagebox.showinfo("showinfo","OTP verified")
                e_npass=npass.get()
                e_ncpass=ncpass.get()
                if (e_npass==e_ncpass):
                    ret2=v.passwd(e_npass)
                    if ret2==True:
                        messagebox.showinfo("showinfo","New Passwords  match. New password will be updated")
                        s="update  master set password='{}' where account_num={}".format(e_npass,e_acc)
                        cursor.execute(s)
                else:
                    messagebox.showinfo("showinfo","New Passwords dont match or Password rules not followed")
                    root.destroy()
                        
            else:
                messagebox.showinfo("showinfo","otp doesn't match.")
                
   
        def  close_win():
            global counter
            if counter==False:
                root.destroy()
                
            getValue()
            root.destroy()

       
                
        btn=Button (self.root,text="Submit",padx=2,pady=6,command=close_win)
        btn.pack(side='bottom')

        acc=Entry(entry_ref_num)
        acc.pack()



        mob=Entry(entry_ref_mob)
        mob.pack()

        pan=Entry(entry_ref_pan)
        pan.pack()

        adhar=Entry(entry_ref_adhar)
        adhar.pack()

        otp=Entry(entry_ref_otp)
        otp.pack()

        npass=Entry(entry_ref_npass,show="*")
        npass.pack()

        ncpass=Entry(entry_ref_ncpass,show="*")
        ncpass.pack()

        
        





if __name__=="__main__":
    root=Tk()
    obj=forgot_pass(root)
    root.mainloop()


        


