
#10. Write a Python script to create a list, where each element of the list is a digit of a given number
n=int(input("Enter number of item : "))
l=[]
for x in range(n):
    l.append(eval(input("Enter item in list : ")))
for x in range(n):
     print(l[x]," digit ",len(l[x]))