#9. Write a python script to check if a string contains only characters of the alphabet.
str=input("Enter string : ")
count=0
for e in str:
    if((ord(e)>=65 and ord(e)<=90) or (ord(e)>=97 and ord(e)<=122)==False):
        count+=1
        break
if(count==0):
    print("string contains only characters of the alphabet.")
else:
    print("string does not contains only characters of the alphabet.")

        
