#10. Write a python script to display all prime numbers within a range.
# range
start = 15
end = 45
for i in range(start,end+1,1):
    count=2
    flag=0
    while(count<=i//2):
        if(i%count==0):
            flag=flag+1
            break
        else:
            count=count+1
    if(flag==0):
        print(i,end=" ")

            


