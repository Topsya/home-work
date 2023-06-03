
slowar_users = {}

def privet():
    return "How can I help you?"

def add_polz(opr):
      opr.split(" ")
      return  slowar_users.update({opr[1]: opr[2]})

def change_polz(opr):
      opr.split(" ")
      slowar_users.update({opr[1]: opr[2]})
      return  slowar_users

def poisk_phone(opr):
      opr.split(" ")
      return f' {slowar_users.get(opr[1], "this name is not")}'

def show_all():
    return slowar_users

def bye():
  # if opr.find("good bye") or opr.find("close") or opr.find("exit"):
     return "Good bye!"
 

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
def main ():
    while  True:
       opr = input("enter comand:")
       if opr == 'hello':
          print(privet()) 
       elif  opr.find("add "): 
         return add_polz()
       elif opr.find("change "):
          return change_polz()
       elif opr.find("phone "):
          return poisk_phone()
       elif opr == "show all":
          print(show_all())
       elif opr == "good bye" or opr =="close" or opr == "exit" :
           print(bye())
           continue
                      
      # print (slowar_users)      

# opr = input("enter comand:")
main ()
# if __name__ == '__main__':