#8. Write a python script to print first N terms of a Fibonacci series.
x=int(input("Enter a number"))
print("0 1",end=" ")
prev=0
next=1
i=0
while i<x-2:
    fib=prev+next
    print(fib,end=" ")
    prev=next
    next=fib
    i=i+1


