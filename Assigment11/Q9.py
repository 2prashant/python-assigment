#9. Write a python script to print binary equivalent of a given decimal number. (do not use bin() method)
num=int(input("Enter a number"))
print("Decimal  to binary :",end=" ")
while(num!=0):
    x=num%2
    print(x,end='')
    num=num//2


