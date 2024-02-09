#6. Write a python script to check whether a given number is a three digit number or not.
x=int(input("Enter a number"))
'''
temp=x
x=x//10
x=x//10
if(x==0):
    print(temp," is not three digit number")
elif x!=0:
    x=x//10
    if(x==0):
        print(temp," is three digit number")
    else :
        print(temp,"Not three digit number")
'''

#OR

print("Three digit number" if 99<x<1000 else "Not three digit number")