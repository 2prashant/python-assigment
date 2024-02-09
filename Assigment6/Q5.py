#5. Write a python script to print two given words in dictionary order
#x=eval(input("Enter words"))
#y=eval(input("ENter words"))
x=(input("Enter words"))
y=(input("ENter words"))
'''
if(x>y):
    print(x,"world is large")
elif(y>x):
    print(y,"world is large")
else:
    print("World are same")
'''
print(x if x>y else y)



