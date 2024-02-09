#9. Write a python script to calculate LCM of two numbers
x=int(input("Enter first number"))
y=int(input("Enter second number"))
if x>y:
    temp=x
else:
    temp=y
while(temp):
    if(temp%x==0 and temp%y==0):
        print("LCM=",temp)
        break
    temp=temp+1
