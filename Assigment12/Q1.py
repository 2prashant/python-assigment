#                     More on loops
#1. Write a python script to reverse a number.
x=int(input("Enter a number"))
rev=0
while x!=0:
    y=x%10
    rev=rev*10+y
    x=x//10

x=rev
print("Reverse number:",x)

