'''
12. Write a python script to accept one complex number from the user and display the
greater number between real part and imaginary part
'''
#c=a+ib, a is real b is img.
'''
a=eval(input("Enter a number="))
b=eval(input("enter a number="))
print(a,"+i",b)
if a>b:
    print("grater number is ",a)
else:
    print("Grater number is ",b)
    '''
x=complex(input("Enter complex number"))
print(x)
print("real",x.real) if x.real>x.imag else print("img",x.imag)


