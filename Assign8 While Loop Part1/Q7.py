# Write a python script to print first 10 even natural numbers in reverse order

# output: 20 18 16 14 12 10 8 6 4 2

for i in range(10,0,-1):
    print(2*i,end=' ')
    
    
# using while loop
i = 10
while i>0:
    print(2*i,end=' ')
    i -= 1