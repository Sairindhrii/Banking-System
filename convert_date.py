from datetime import datetime
def date(d):
    date_object = datetime.strptime(d, '%Y-%m-%d').date()
    return str(date_object)



def ret_date(dd,d2):
    fd=datetime.strptime(dd ,'%Y-%m-%d').date()
    td=datetime.strptime(d2 ,'%Y-%m-%d').date()
    return fd,td
    
    
