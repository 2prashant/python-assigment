#2. Write a python script to check whether a given number is Prime or not
x=int(input("Enter a number="))
for i in range(2,x//2+1):
    if(x%i==0):
        print(" Not Prime number")
        break
else:
    print("prime number")


