"""
2. Write a menu driven program to perform following operations - Addition, Subtraction,
Multiplication, Division
"""
a=int(input("Enter a number"))
b=int(input("Enter a number"))

print("\n1.Addition")
print("2.substraction")
print("3.Multiplication")
print("4.Divid")
print("\nEnter your choice=")
choice=int(input())
match choice:
    case 1:
        print("add=",(a+b))
    case 2:
        print("sub=",(a-b))
    case 3:
        print("multi=",(a*b))
    case 4:
        print("divid",a/b)
    case _:
        print("Invalid Choice")

