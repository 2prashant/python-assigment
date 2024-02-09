#2. Write a Python script to create a list of first N odd natural numbers.
l1=[]
for x in range(0,int(input("Enter a number="))):
    l1.append(2*x+1)
print(l1)
