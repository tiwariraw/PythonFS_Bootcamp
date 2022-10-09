# Write a python program to append elements from another list to the current list.
# firstlist = ["Java", "Python", "SQL"]
# secondlist = ["C", "Cpp", "NoSQL"] 

l1 = ["Java", "Python", "SQL"]
l2 = ["C", "Cpp", "NoSQL"] 
for e in l2:
    l1.append(e)
print(l1)