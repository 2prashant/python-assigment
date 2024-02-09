'''
listA = []
# Input number of elemetns
n = int(input("Enter number of elements in the list : "))
# iterating till the range
for i in range(0, n):
   print("Enter element No-{}: ".format(i+1))
   elm = int(input())
   listA.append(elm) # adding the element
print("The entered list is: \n",listA)
'''
#2. Write a python script to get the data type of a list.
print("Enter number")
l1=eval(input())
print(l1)
print(type(l1))

