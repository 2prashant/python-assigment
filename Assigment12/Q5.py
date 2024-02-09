#5. Write a python script to find next prime number of a given number.
x=int(input("Enter a number"))+1
while x:
    j=2
    count=0
    while(j<(x//2)+1):
        if(x%j==0):
            count=count+1
        j=j+1
    if(count==0):
        print("Next prime number is ",x)
        break
    x=x+1





