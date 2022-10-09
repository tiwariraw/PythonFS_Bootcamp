# Write a python script to print first 10 natural numbers in reverse order

# output: 10 9 8 7 6 5 4 3 2 1

for i in range(10,0,-1):
    print(i,end=' ')
    
    
# using while loop

# M1
i = 10
while i>0:
    print(i)
    i -= 1
    
# M2
i = 1
while i<=10:
    print(11-i)
    i += 1