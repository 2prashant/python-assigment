'''
Write a python script to check whether a given quadratic equation has two real &
distinct roots, real & equal roots or imaginary roots
'''
a=eval(input("Enter value of a in Quadratic equaction="))
b=eval(input("Enter value of b="))
c=eval(input("enter value of c="))
root=(b*b)-(4*a*c)
if(root>0):
    print("root is real and distinct")
elif root==0:
    print("root is real and equal")
else:
    print("root is imaginary")




