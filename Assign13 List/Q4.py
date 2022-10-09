# Write a python script to Change the values "SQL" and "Reactnative" with the values "NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]

lst = ["Java", "SQL", "C", "Reactnative", "Javascript", "Python"]
lst.remove('SQL')
lst.insert(1,'NoSQL')
lst.remove('Reactnative')
lst.insert(3,'Flutter')
print(lst)