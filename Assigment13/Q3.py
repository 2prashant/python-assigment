#3. Write a python script to get the last item of the list ( mylist = ["Java", "C", "Python"])
n=int(input("Enter number of element : "))
mylist=[]
for x in range(n):
    mylist.append(eval(input("Enter data in list : ")))
print("mylist = ",mylist)
