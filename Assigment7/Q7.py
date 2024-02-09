'''
7. Write a python program to check whether a given number is positive, negative or
zero using match case statement
'''
x=int(input("Enter a number"))
match x:
    case x if x>0:
        print("Positive number")
    case x if x<0:
        print("Negative number")
    case x if x==0:
         print("number is Zero")
    case _:
          print("Invalid input")
    
