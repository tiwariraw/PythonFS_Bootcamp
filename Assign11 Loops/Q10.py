# Write a python script to print the octal equivalent of a given decimal number. (do not use oct() method)

n = int(input('Enter n: '))
list1 = []
while n:
    list1.append(n%8)
    n=n//8
for i in reversed(list1):     #doesn't modifies the list
    print(i,end=' ')