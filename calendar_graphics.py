
from tkinter import *
from tkcalendar import Calendar
import datetime
from datetime import datetime
import csv
class dateee:
    def __init__(self,root):
        
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("260x285")

        cal = Calendar(self.root, selectmode = 'day', year = 2020, month = 5,day = 22)
        cal.pack(pady = 10)
        def grad_date():
           date.config( text =cal.get_date())
           tt=cal.get_date()
           print(type(tt),tt)
           tt = datetime.strptime(tt, '%m/%d/%y').date()

           tt=str(tt)
           with open ('dob.csv','w') as f:
               w=csv.writer(f)

               hd=[tt]
               w.writerow(hd)
               f.close()

               root.destroy()

           
           #return the date selected by the user in datetime format 
       
           
        btn=Button(self.root, text = "Get Date",command = grad_date)
        btn.pack(pady = 10)
     
        date = Label(self.root, text = "")
        date.pack(pady = 10)
 
if __name__=="__main__":
    root=Tk()
    obj=dateee(root)
    root.mainloop()
