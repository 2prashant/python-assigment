#3. Write a python script to calculate sum of cubes of first N natural numbers.
num=int(input("Enter a number="))
sum=0
for x in range(1,num+1):
    sum=sum+x**3
print("Sum=",sum)

