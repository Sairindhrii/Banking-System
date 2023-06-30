from tkinter import *
import mysql.connector
from tkinter import messagebox
from PIL import  Image
from PIL import ImageTk
from tkinter import ttk
import csv
import ValidityCheck as v

mycon=mysql.connector.connect(host="localhost", user="root", passwd="root", database="bank")
mycon.autocommit=True
cursor=mycon.cursor()

class address:
    def __init__(self,root):
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("500x300")

        lbl_title=Label(self.root,text="Change Address",font=("times new roman",15,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=500,height=50)

        img2=Image.open(r"G:\My Drive\PROJECT BANK\logo.png")
        img2=img2.resize((120,45),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=30)

        #----------------------------------------------label frames-------------------------------------------------------------------------------------------------
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Enter new address details",font=("times new roman",12,"bold"),bg="white",fg="black")
        labelframeleft.place(x=5,y=50,width=700,height=1500)
        
        lbl_ref_pin=Label(labelframeleft,text="Pin Code: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_pin.grid(row=0,column=0,sticky=W)

        entry_ref_pin=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_pin.grid(row=0,column=1)

        lbl_ref_city=Label(labelframeleft,text="City: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_city.grid(row=1,column=0,sticky=W)

        entry_ref_city=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_city.grid(row=1,column=1)

        lbl_ref_state=Label(labelframeleft,text="State: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_state.grid(row=2,column=0,sticky=W)

        entry_ref_state=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_state.grid(row=2,column=1)

        lbl_ref_land=Label(labelframeleft,text="Land Mark: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_land.grid(row=3,column=0,sticky=W)

        entry_ref_land=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_land.grid(row=3,column=1)


        lbl_ref_add=Label(labelframeleft,text="Full Address: ",font=("times new roman",12,"bold"),padx=2,pady=6)
        lbl_ref_add.grid(row=4,column=0,sticky=W)

        entry_ref_add=ttk.Entry(labelframeleft,width=80,font=("times new roman",12,"bold"))
        entry_ref_add.grid(row=4,column=1)

        def val():

            with open('accno.csv','r') as f:
                csv_reader = csv.reader(f)
                for row in csv_reader:
                    e_acc=row[0]
                    break
            e_acc=int(e_acc)
            
            e_pin=pin.get()
            e_city=city.get()
            e_land=land.get()
            e_add=add.get()
            e_state=state.get()

            ret=v.pin_code (e_pin)
            if  ret==True:
                s="update master set pin_code='{}' where account_num={}".format(e_pin,e_acc)
                cursor.execute(s)
                
                s="update master set address='{}' where account_num={}".format(e_add,e_acc)
                cursor.execute(s)

                s="update master set city='{}' where account_num={}".format(e_city,e_acc)
                cursor.execute(s)

                s="update master set state='{}' where account_num={}".format(e_state,e_acc)
                cursor.execute(s)
                
                s="update master set landmark='{}' where account_num={}".format(e_land,e_acc)
                cursor.execute(s)

                messagebox.showinfo("showinfo","address details updated!")
            else:
                if not (e_pin==''):
                    messagebox.showinfo("showinfo","Incorrect pin")
                root.destroy()


            
            

        def close_win():
            val()
            
            root.destroy()

        btn=Button (self.root,text="Close",font=("times new roman",12,"bold"),padx=2,pady=6,command=close_win)
        btn.pack(side='bottom')

        pin=Entry(entry_ref_pin)
        pin.pack()

        land=Entry(entry_ref_land)
        land.pack()

        city=Entry(entry_ref_city)
        city.pack()

        state=Entry(entry_ref_state)
        state.pack()

        add=Entry(entry_ref_add)
        add.pack()


if __name__=="__main__":
    root=Tk()
    obj=address(root)
    root.mainloop()



