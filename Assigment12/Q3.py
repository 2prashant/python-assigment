#3. Write a python script to print all Prime numbers under 100
i=2
while i<100:
    count=0
    j=2
    while j<i//2+1:
        if(i%j==0):
           count=count+1 
        j=j+1
    if(count==0):
        print(i,end=" ")
    i=i+1
    

