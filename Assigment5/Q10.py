'''
10. Write a python script to use IS operator to display if both variables are the same
object or not?
'''
#  SLove
a,b,c,d,e=5,7,"prashant",5+8j,9.5
print(a is 5)
print(b is not 9)
print(c is "prashant")
print(d is not 9+2j)
print(e is 9)

#or
l3=[12,24,35,46,78]
print(35 in l3 )
print(90 in l3)

print(90 is not l3) 
print(12 is not l3)


print("Solve")
# solve
l1=[1,2,3,4,5]
l2=[1,2,3,4,5]
print(l1 is l2)
print(l1==l2)
