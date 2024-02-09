#4. Write a Python script to find the greatest number in a given list of numbers.
l1=[]
for x in range(0,int(input("Enter size of list="))):
    num=int(input("Enter Number="))
    l1.append(num)
print(l1)
print("Max=",max(l1))