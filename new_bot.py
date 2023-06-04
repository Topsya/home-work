
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

# def privet():
#     return "How can I help you?"

@input_error
def add_polz(opr):
      opr.split(" ")
      return  slowar_users.update({opr[1]: opr[2]})

@input_error
def change_polz(opr):
      opr.split(" ")
      slowar_users.update({opr[1]: opr[2]})
      return  slowar_users

@input_error
def poisk_phone(opr):
      opr.split(" ")
      return f' {slowar_users.get(opr[1], "this name is not")}'

# def show_all():
#     return slowar_users

# def bye():
#   # if opr.find("good bye") or opr.find("close") or opr.find("exit"):
#    return "Good bye!"
 

def main ():
    while  True:
       opr = input("enter comand:")
       if opr == 'hello':
            print("How can I help you?") 
       if  opr.find("add "): 
            return add_polz(opr)
       if opr.find("change "):
            return change_polz(opr)
       if opr.find("phone "):
            return poisk_phone(opr)
       if opr == "show all":
            print(slowar_users)
       elif opr == "good bye" or opr == "close" or opr == "exit":
            print("Good bye!")
            break
    return                 
      # print (slowar_users)      
if __name__ == '__main__':
 main ()
