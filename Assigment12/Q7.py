#7. Write a python script to check whether a given pair of numbers are co-Prime numbers or not.
x=int(input("Enter a first number"))
y=int(input("Enter second number"))
count=0
if(x>y):
    temp=x
else:
    temp=y
i=2
while(temp>i):
    if x%i==0 and y%i==0:
        count=count+1
        break
    i=i+1
if(count==0):
    print("co-Prime number")
else:
    print("Not co-prime number")

        


    
    
