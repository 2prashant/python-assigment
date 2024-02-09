#8. Write a python script to calculate sum of digits of a given number
x=int(input("Enter a number"))
sum=0
while(x!=0):
    num=x%10
    sum=sum+num
    x=x//10
print("Sum of digit is ",sum)

