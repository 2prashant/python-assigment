#5. Write a Python script to find the smallest number in a given list of numbers.
l1=[]
for x in range(0,int(input("Enter list size="))):
    num=int(input("Enter a number="))
    l1.append(num)
print(l1)
print("minimum Element=",min(l1))