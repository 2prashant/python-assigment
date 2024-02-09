#8. Write a python script to check if a string contains only numbers.

num=input("Enter string : ")
count=0
for e in num:
    if ord(e)>=49 and ord(e)<=57:
         temp=0        
    else:
         count+=1
if(count!=0):
     print("string does not contains only number")
else:
     print("String contains only numbers")









"""
original_list = [1, 'apple', 2, 'banana', 3, 'cherry', 4.5, 5]
int_values_only = [x for x in original_list if isinstance(x, int)]

print(int_values_only)   
"""









"""
str=input("Enter string") //  not solve
count=0
for x in str :
         if(isinstance(int (x),int)!=True):
                 count+=1
                 break
if(count==0):
        print("String ontains only numbers")
else:
        print("String does not contains only numbers")
"""                
    
   


           
