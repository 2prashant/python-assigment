#6. Write a python script to reverse a String. (“iNeuron”).
s1="ineuron"
count=0
i=0
for x in s1:
    count=count+1
j=count-1
while(i<j):
    temp=s1[i]
    s1[i]=s1[count]