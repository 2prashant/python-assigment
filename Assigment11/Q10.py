#10. Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)
num=int(input("Enter a number="))
sum=0
print("Decimal to equivalent :",end=" ")
while(num!=0):
    x=num%8
    sum=sum*10+x
    num=num//8
rev=0
while (sum!=0):
    y=sum%10
    rev=rev*10+y
    sum=sum//10
print(rev)


