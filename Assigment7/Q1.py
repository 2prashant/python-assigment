#                                   Match Case
#1. Write a python script to display the number of days in a given month number.
'''
x=int(input("Enter a month"))
match x:
    case 1:
        print("31 dayes")
    case 2:
        print("30 or 29 dayes")
    case 3:
        print("31 dayes")
    case 4:
        print("30 dayes")
    case 5:
        print("31 dayes")
    case 6:
        print("30 dayes")
    case 7:
        print("31 dayes")
    case 8:
        print("31 dayes")
    case 9:
        print("30 dayes")
    case 10:
        print("31 dayes")
    case 11:
        print("30 dayes")
    case 12:
        print("31 dayes")
    case _:
        print("Invalid month")

        '''

x=int(input("Enter month="))
match x:
    case match if x in (1,3,5,7,8,10,12):
        print("31 dayes")
    case match if  x in (4,6,9,11):
        print("30 dayes")
    case 2:
         print("28 or 29 dayes")
    case _:
         print("Invalid choice")
    




         



