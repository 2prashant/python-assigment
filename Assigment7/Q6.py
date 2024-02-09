"""6. Write a python program to check whether a given string is a multiword string or single
word string using match case statement.
"""
x=input("Enter string")
x=x.strip()
match x:
     case x if ' ' in x:
          print("multiword string")
     case x if ' ' not in x:
          print("single world string")
     case _:
          print("Invalid input")
