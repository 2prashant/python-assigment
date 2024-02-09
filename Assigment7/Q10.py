"""10. Write a program to display day name on the basis of user’s liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
"""
s=input("Enter your favorite color ")
l1=["yello","Blue","Orange","White","Black","Red"]
for colour in l1:
    if colour in s:
        c=colour
        break
else:
     c="other"
match c:
    case "yelloW":
        print("Monday")
    case "Blue":
        print("Tuesday")
    case "Orange":
        print("wednesday")
    case "White":
        print("Thursday")
    case "Black":
        print("Friday")
    case "Red":
        print("Saturday")
    case _:
        print("Other")
print()

    
