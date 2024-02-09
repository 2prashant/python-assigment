'''
5. Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number.
'''
x=int(input("Enter a number"))
match x:
     case x if x%2==0:
          print("Saurabh Shukla")
     case x if x>0:
          if(x%2!=0):
               print("Aditya chaudharay")
     case x if x<0:
              if(x%2!=0):
                    print("Prateek Jain")
     case _:
            print("Invalid choice")
              

