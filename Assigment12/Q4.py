#4. Write a python script to print all Prime numbers between two given numbers (both values inclusive)
x=int(input("Enter first number="))
y=int(input("Enter second number="))
print("Prime number:")
while(x<y):
    count=0
    j=2
    while(j<x//2+1):
        if(x%j==0):
            count=count+1
        j=j+1
    if count==0:
        print(x,end=" ")
    x=x+1




