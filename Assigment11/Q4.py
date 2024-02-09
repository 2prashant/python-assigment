#4. Write a python script to calculate sum of first N odd natural numbers
num=int(input("Enter a number="))
sum=0
for x in range(0,num):
    sum=sum+(2*x+1)
print("sum of",num," odd number is ",sum)





