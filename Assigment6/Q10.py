'''
10. Write a python script to print greater among three numbers. Print number only once
even if the numbers are the same.
'''
x=int(input("Enter first Number"))
y=int(input("enter second number"))
z=int(input("Enter third Number"))
if x>y and x>z:
    print(x," is large")
elif y>x and y>z:
    print(y," is large")
elif z>x and z>y:
    print(z," is large")
else:
    print("Number are same")
    