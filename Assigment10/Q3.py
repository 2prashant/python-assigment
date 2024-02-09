#3. Write a python script to print first M multiples of N.
n=int(input("Enter a number"))
for i in range(int(input("Enter number of multiple="))):
    print(n*(i+1),end=" ")

