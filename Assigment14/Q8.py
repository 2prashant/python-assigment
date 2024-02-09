'''
8. Write a Python script to print distinct elements along with their frequencies of
occurrence in the list. // solve but not good solution
'''
l1=[]  
for x in range(0,int(input("Enter list size="))):
    num=int(input("Enter number="))
    l1.append(num)
print(l1)
for x in range(len(l1)):
    print("repetaction of ",l1[x]," in list ",l1.count(l1[x])," time")
    


