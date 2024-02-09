"""
6. Write a python program to append elements from another list to the current list.(
firstlist = ["Java", "Python", "SQL"]
secondlist = ["C", "Cpp", "NoSQL"] )
"""
firstlist = ["Java", "Python", "SQL"]
print(firstlist)
secondlist = ["C", "Cpp", "NoSQL"]
print(secondlist)
firstlist.append(secondlist)# append list
print(firstlist)
newlist=firstlist+secondlist  # cutcattination
print(newlist)

