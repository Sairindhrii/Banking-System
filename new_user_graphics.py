from tkinter import *
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from tkinter import ttk
from datetime import date
import ValidityCheck as v
import mysql.connector
import deposit_table as dep
from datetime import date

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class details:
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("760x900")

        


        #---------------------------------------------------------title----------------------------------------------------------------------------------------------
        lbl_title=Label(self.root,text="    Account holder details  ",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=760,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((70,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=90,height=30)

        #----------------------------------------------label frames-------------------------------------------------------------------------------------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Details",font=("times new roman",15,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=760,height=1000)

        #------------------labels and entries---------------------------------------------------

        lbl_ref_name=Label(labelframeleft,text="Name : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_name.grid(row=0,column=0,sticky=W)

        entry_ref_name=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_name.grid(row=0,column=1)


        lbl_ref_guardian=Label(labelframeleft,text="Guardian's Name : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_guardian.grid(row=1,column=0,sticky=W)

        entry_ref_guardian=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_guardian.grid(row=1,column=1)


        lbl_ref_nominee=Label(labelframeleft,text="Nominee name : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_nominee.grid(row=2,column=0,sticky=W)
        

        entry_ref_nominee=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_nominee.grid(row=2,column=1)

        lbl_ref_reln=Label(labelframeleft,text="Relation with nominee: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_reln.grid(row=3,column=0,sticky=W)
        

        entry_ref_reln=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_reln.grid(row=3,column=1)


        lbl_ref_add=Label(labelframeleft,text="Address: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_add.grid(row=4,column=0,sticky=W)

        entry_ref_add=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_add.grid(row=4,column=1)
        

        lbl_ref_land=Label(labelframeleft,text="Nearest Landmark: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_land.grid(row=5,column=0,sticky=W)

        entry_ref_land=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_land.grid(row=5,column=1)
        

        lbl_ref_city=Label(labelframeleft,text="City : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_city.grid(row=6,column=0,sticky=W)

        entry_ref_city=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_city.grid(row=6,column=1)
        

        lbl_ref_state=Label(labelframeleft,text="State : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_state.grid(row=7,column=0,sticky=W)

        entry_ref_state=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_state.grid(row=7,column=1)

        lbl_ref_pin=Label(labelframeleft,text="Pin code : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_pin.grid(row=8,column=0,sticky=W)

        entry_ref_pin=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_pin.grid(row=8,column=1)
        

        lbl_ref_phone=Label(labelframeleft,text="Phone number: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_phone.grid(row=9,column=0,sticky=W)

        entry_ref_phone=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_phone.grid(row=9,column=1)

        lbl_ref_adhar=Label(labelframeleft,text="Adhar Number: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_adhar.grid(row=10,column=0,sticky=W)

        entry_ref_adhar=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_adhar.grid(row=10,column=1)

        lbl_ref_pan=Label(labelframeleft,text="Pan Number : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_pan.grid(row=11,column=0,sticky=W)

        entry_ref_pan=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_pan.grid(row=11,column=1)

        lbl_ref_email=Label(labelframeleft,text="Email : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_email.grid(row=12,column=0,sticky=W)

        entry_ref_email=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_email.grid(row=12,column=1)

        #modify calendar
        lbl_ref_dob=Label(labelframeleft,text="Date of Birth(dd-mm-yyyy) : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_dob.grid(row=13,column=0,sticky=W)

        entry_ref_dob=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_dob.grid(row=13,column=1)

   
      
        lbl_ref_gender=Label(labelframeleft,text="Gender : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_gender.grid(row=14,column=0,sticky=W)

        entry_ref_gender=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_gender.grid(row=14,column=1)


       
        lbl_ref_pass=Label(labelframeleft,text="New Password : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_pass.grid(row=15,column=0,sticky=W)

        entry_ref_pass=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_pass.grid(row=15,column=1)

        text = Label(labelframeleft, text="Password must be of min 8 length\n& must contain 1 digit,1 spl character,\n1 uppercase & 1 lower case.")
        text.place(x=490,y=570)


        lbl_ref_cpass=Label(labelframeleft,text="Confirm New Password : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_cpass.grid(row=16,column=0,sticky=W)

        entry_ref_cpass=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_cpass.grid(row=16,column=1)

        lbl_ref_atype=Label(labelframeleft,text="Account Type(S-savings/C-current):",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_atype.grid(row=17,column=0,sticky=W)

        entry_ref_atype=ttk.Entry(labelframeleft,width=42,font=("times new roman",12,"bold"))
        entry_ref_atype.grid(row=17,column=1)

        lbl_ref_num=Label(labelframeleft,text="Amount : ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_num.grid(row=18,column=0,sticky=W)

        entry_ref_num=ttk.Entry(labelframeleft,width=22,font=("times new roman",12,"bold"))
        entry_ref_num.grid(row=18,column=1)
        

        

        def printValue():
            count=0 
            pname= player_name.get()
            pamount=float(num.get())
            pguardian=guardian.get()
            pnominee=nominee.get()
            preln=reln.get()
            paddress=address.get()
            pland=land.get()
            pcity=city.get()
            pstate=state.get()
            pemail=email.get()
            patype=atype.get()
            
            ppin=pin.get()
            #----------------pincode check------------------
            if (not (v.pin_code(ppin))):
                messagebox.showinfo("showinfow","Incorrect pin code entered. Re-enter!")
                count=1
    
            pphone=phone.get()
            #---------------------phone number check--------------------------
            if (not (v.mobile_n(pphone))):
                messagebox.showinfo("showinfow","Re-enter phone number!")
                count=1
           
            
            padhar=adhar.get()
            #--------------------------adhar number check------------------
            if not(v.adhar_no(padhar)):
                messagebox.showinfo("showinfo", "Re-enter adhar number!")
                count=1
  
            ppan=pan.get()
            #--------------------------pan number check-------------------
            if not(v.pan(ppan)):
                messagebox.showinfo("showinfo", "Re-enter pan  number!")
                count=1
 
            
            pdob=dob.get()
            #------------------dob check-----------------------
            yy=int(pdob[pdob.rfind('-')+1: :])
            today=date.today()
            y=today.year
            if not( y-yy >= 18 and y-yy <=80):
                messagebox.showinfo("showinfo", "Not a proper age!")
                exit(0)
            else:
                dd=int(pdob[0:pdob.find('-')])
                mm=int(pdob[pdob.find('-')+1:pdob.rfind('-')])
                yy=int(pdob[pdob.rfind('-')+1: :])
                d=[dd,mm,yy]
                if not (v.valid_date(d)):
                    messagebox.showinfo("showinfo", "Enter DOB  Again!")
                    count=1
            #----------------------reversing the dob----------------------------------------
            pdob=str(yy)+'-'+str(mm)+'-'+str(dd)
            
            pgender=gender.get()
            #-------------------------------check gender----------------------------
            if (not (v.gender(pgender))):
                messagebox.showinfo("showinfo", "Enter Gender Again!")
                count=1
            
            ppass=password.get()
            #----------------------------check password---------------------------------
            if not(v.passwd(ppass)) :
                messagebox.showinfo("showinfo", "password does not fulfil criteria.Re Enter password!")
                count=1
                
            pcpass=cpassword.get()
            if not(ppass==pcpass):
                messagebox.showinfo("showinfo", "Passwords dont match.Re enter password and confirm password")
                count=1

            
            if not(count==1):
                acc=v.acc_no()  #generate account number
                Label(self.root, text=f'Your Account number is: {acc}', pady=20, bg='white').pack()                
                dop=date.today()  #date of opening 
                act='A'                    #activity
                doc='0000-00-00'   #date of closing

                


                
                #------------------------------------------------------------------------------------------entering the data in master table---------------------------------------------------------------------------------------------
                s="INSERT INTO MASTER VALUES ( {},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(acc,patype,pname,act,pguardian,pnominee,preln,paddress,pland,pcity,ppin,pstate,pgender,pphone,pemail,padhar,pdob,ppass,ppan,dop,doc)
                cursor.execute(s)


                #------------------------update deposit and closin_bal tab-----------

                #account opening always in cash 
                s="INSERT INTO DEPOSIT VALUES('{}',{},{},{},'{}','{}')".format(dop,acc,pamount,0,'C','')
                cursor.execute(s)
                s="INSERT INTO CLOSING_BAL VALUES ({},{})".format(acc,pamount)
                cursor.execute(s)


                messagebox.showinfo("showinfo","Account Opened Successfully")

                root.destroy()

      
        btn=Button(self.root, text="Submit Details", padx=2, pady=6,command=printValue)
        btn.place(x=150,y=810)

        player_name=Entry(entry_ref_name)
        player_name.pack()


        num = Entry(entry_ref_num)
        num.pack()

        guardian=Entry(entry_ref_guardian)
        guardian.pack()

        nominee=Entry(entry_ref_nominee)
        nominee.pack()

        reln=Entry(entry_ref_reln)
        reln.pack()

        address=Entry(entry_ref_add)
        address.pack()

        land=Entry(entry_ref_land)
        land.pack()

        city=Entry(entry_ref_city)
        city.pack()

        state=Entry(entry_ref_state)
        state.pack()

        pin=Entry(entry_ref_pin)
        pin.pack()

        phone=Entry(entry_ref_phone)
        phone.pack()

        adhar=Entry(entry_ref_adhar)
        adhar.pack()

        pan=Entry(entry_ref_pan)
        pan.pack()

        dob=Entry(entry_ref_dob)
        dob.pack()

        email=Entry(entry_ref_email)
        email.pack()

        gender=Entry(entry_ref_gender)
        gender.pack()

        password=Entry(entry_ref_pass,show="*")
        password.pack()

        atype=Entry(entry_ref_atype)
        atype.pack()

        


        cpassword=Entry(entry_ref_cpass,show="*")
        cpassword.pack()

        
        

if __name__=="__main__":
    root=Tk()
    obj=details(root)
    root.mainloop()
