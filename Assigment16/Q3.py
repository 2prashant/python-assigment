#3. Write a python program to reverse the tuple.
print("Enter data in tuple")
t1=tuple([int (x) for x in input().split(',')])
print(t1)
size=len(t1)-1
i=0
while i<=size:
    t2=t1[size] 
    size-=1
    i+=1
print("after reverse : ")
print(t2)


