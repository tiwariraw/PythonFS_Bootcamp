# Write a Python script to create a list, where each element of the list is a digit of a given number.

n = input('Enter a number: ')
l1 = [int(e) for e in n]         # list comprehension
print(l1)