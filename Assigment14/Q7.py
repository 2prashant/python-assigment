#7. Write a Python script to remove all non int values from a list.
#not solve
x=int(input("Enter list size : "))
l1=[]
for e in range(x):
    l1.append(eval(input("Enter data in list : ")))
print(l1)
l1=[int (e) for e in l1 if isinstance(e,int)]
print(l1)
   


