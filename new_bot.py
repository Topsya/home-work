
slowar_users = {}

def input_error(func):
   def inner(*args, **kwargs):
      # if opr.find("change "):
          try:
              result = func(*args, **kwargs)
              return result
          except KeyError: 
             print("Enter user name")
          except IndexError:
             print("Give me name and phone please. ")
          except ValueError:
              print("ValueError. Please try again. ")       
   return inner

@input_error
def add_polz(opr):
      a = opr.split(" ")
      # print (a)
      slowar_users[a[1]] = a[2]
      return f' add is ok , name{a[1]}, phone{a[2]}' 

@input_error
def change_polz(opr):
      chang = opr.split(" ")
      slowar_users[chang[1]] = chang[2] 
      return  f'change is all ready'

@input_error
def poisk_phone(opr):
      poisk = opr.split(" ")
      return f' {slowar_users.get(poisk[1], "this name is not")}'
 
def main ():
    while  True:
       opr = input("enter command, everything through the gap:")
       if opr.lower() == 'hello':
            print("How can I help you?") 
       elif  opr.startswith('add'): 
            print(add_polz(opr))
              
       elif opr.startswith('change'):
             print (change_polz(opr))
              
       elif opr.startswith('phone'):
             print (poisk_phone(opr))
              
       elif opr.lower() == 'show all':
            print(slowar_users)
       elif opr.lower() == 'good bye' or opr == 'close' or opr == 'exit':
            print("Good bye!")
            break
       else:
            print("Unknown command")            
      # print (slowar_users)      
if __name__ == '__main__':
 main ()
