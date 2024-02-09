#10. Write a python script to calculate HCF of two number
x=int(input("Enter first number"))
y=int(input("Enter second number"))
if x>y:
    HCF=x
else:
    HCF=y
while HCF>=1:
      if(x%HCF==0 and y%HCF==0):
           print("HCF=",HCF)
           break
      HCF=HCF-1

