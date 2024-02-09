#7. Write a python script to count digits in a given number.
num=int(input("Enter a number="))
count=0
while num!=0:
    num=num//10
    count=count+1
print(" number of digit is ",count)



