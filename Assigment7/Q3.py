"""
3. Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
"""

print("a.check lengths of an isosceles")
print("b.check lengths of sides of right angled triangle or not")
print("c.check length are equilateral triangle or not")
print("d.Exit")
a=eval(input("Enter a Number="))
b=eval(input("Enter a number="))
c=eval(input("Enter a number="))
choice=(input("Enter your choice="))
match choice:
        case "a":
                    if(a==b or a==c or b==c or b==a ):
                            print("isosceles triangle")
                    else:
                            print("Not isosceles triangle")

        case "b":
                if(((a**a+b**b)==c**c) or ((a**a+c**c)==b**b) or ((c**c+b**b)==a**a)):
                        print("right angled triangle")
                else:
                        print("Not right angled triangle")
        case "c":
                if(a==b==c):
                        print("equilateral triangle")
                else:
                        print("Not equilateral triangle")
        case "d":
                 exit(0)
        case _:
                print("Invalid choice")

                
                
                        


         
    


