# Write a python script to print first 10 odd natural numbers in reverse order

# output: 19 17 15 13 11 9 7 5 3 1

for i in range(10,0,-1):
    print(2*i-1,end=' ')
    

# using while loop
i = 10
while i>0:
    print(2*i-1,end=' ')
    i -= 1