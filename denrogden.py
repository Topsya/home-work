from datetime import datetime, timedelta
 
users = {  
          'Igor' : datetime(2000,5,23) ,
          'Anton' : datetime(1986,8,1) ,
          'Katya' : datetime(1989,9,8) ,
          'Valya' : datetime(1995,10,15)
          }
Monday =  "Monday:"  
Tuesday =   "Tuesday:" 
Wednesday =  "Wednesday:" 
Thursday =  "Thursday:" 
Friday = "Friday:"
 
 
segodnya = datetime.now()
one_week = timedelta(days=7)
one_week_plas = segodnya + one_week 
two_week_plas = segodnya + 2 * one_week

def get_birthdays_per_week(users): 
  for name,birthday   in users.items():
     birthday2023 = datetime( year=2023, month= birthday.month, day = birthday.day)
     if one_week_plas.month.day <= birthday.month.day <= two_week_plas.month.day :
        if birthday2023.isoweekday() ==1:
            Monday.append(name)
        elif birthday2023.isoweekday() ==2:
            Tuesday.append(name)      
        elif birthday2023.isoweekday() ==3:
            Wednesday.append(name)    
        elif birthday2023.isoweekday() ==4:
            Thursday.append(name) 
        elif birthday2023.isoweekday() ==5:
            Friday.append(name)                   
        else :  
            Monday.append(name)  
  return Monday, Tuesday, Wednesday, Thursday, Friday              
             
print (f'{Monday}\n{Tuesday}\n{Wednesday}\n{Thursday}\n{Friday}')
