#6. Write a python script to print first N prime numbers
x=int(input("Inter a number="))
print("Prime number:")
i=2
while(i<=x):
    flag=0
    j=2
    while(j<(i/2)+1):
        if(i%j==0):
            flag=flag+1
        j=j+1
    if(flag==0):
        print(i,end=" ")
    i=i+1





