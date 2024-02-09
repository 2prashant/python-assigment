#9. Write a python script to check whether a given year is a leap year or not.
x=int(input("Enter a year"))
if x%400==0 or x%100!=0 and x%4==0:
    print("Year is leap")
else:
    print("Year is not leap")