#Calculator
from art import logo
from replit import clear

def cal():
  print(logo)
  a=float(input("Enter the First Number : "))

  should=True
  while should:
    operation=input("Choose the operation to be perform ? \n + \n - \n * \n / \nEnter the Operation : ")
    b=float(input("Enter the Second Number : "))
  
    def add(a,b):
      return (a+b)
   
    def sub(a,b):
      return(a-b)
    def multiply(a,b):
      return (a*b)
    def divide(a,b):
      return (a/b)

    if operation == "+":
      ans=(add(a,b))
    elif operation == "-":
      ans=(sub(a,b))
    elif operation == "*":
      ans=(multiply(a,b))
    elif operation == "/":
      ans=(divide(a,b))
    else:
      print("Invalid Input")
    print(ans)
  

    result = input("Type 'Y' to Proceed with the answer Or 'N' to start new calculation Or 'E' to Exit  :  ").lower()
    if result=="y":
      should=True
      a=ans
    elif result=="n":
      should=False
      clear()
      cal()
    else:
      exit()
cal()