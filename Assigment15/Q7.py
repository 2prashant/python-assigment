#7. Write a python script to determine whether a string contains a specific substring.
str=input("Enter string : ")
l=[]
for i in range(0,len(str)):
    for j in range(i+1,len(str)+1):
        l.append(str[i:j])
print("you are check string contains a specific substring or not ")
str1=(input("Enter string : "))
if(str1 in l):
    print("list contain specific substring")
else:
    print("list does not contain specific substring" )
           


