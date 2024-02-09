'''9. Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
'''
x=int(input("Enter year="))
match x:
    case x if x%100!=0 and x%4==0:
        print("Non century leap year")
    case x if x%400==0:
        print("Centuray leap year")
    case x if x%100!=0 and x%4!=0:
        print("non centuray non leap year")
    case x if x%400!=0:
        print("century non leap year")
    case _:
        print("Invalid input")
