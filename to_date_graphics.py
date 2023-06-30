from tkinter import *
from tkcalendar import Calendar
import datetime
from datetime import datetime
import csv
class to_date:
    def __init__(self,root):
        
        self.root=root
        self.root.title("IBBI BANK")
        self.root.geometry("260x285")

        cal = Calendar(self.root, selectmode = 'day', year = 2023, month = 6,day = 22)
        cal.pack(pady = 10)
        def tdate():
           date.config( text =cal.get_date())
           tt=cal.get_date()
           print(type(tt),tt)
           tt = datetime.strptime(tt, '%m/%d/%y').date()

           tt=str(tt)
           with open ('to_date.csv','w') as f:
               w=csv.writer(f)

               hd=[tt]
               w.writerow(hd)
               f.close()

               root.destroy()

           
           #return the date selected by the user in datetime format 
       
           
        btn=Button(self.root, text = "Get Date",command = tdate)
        btn.pack(pady = 10)
     
        date = Label(self.root, text = "")
        date.pack(pady = 10)
 
if __name__=="__main__":
    root=Tk()
    obj=to_date(root)
    root.mainloop()
