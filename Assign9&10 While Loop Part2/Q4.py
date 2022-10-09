# Write a python script to print first N odd natural numbers

# output: 
# for n=5
# 1 3 5 7 9

n=int(input('Enter n: '))
for i in range(n):
    print(2*i+1,end=' ')
    
    
    
# using while loop
i = 1
while i<=n:
    print(2*i+1,end=' ')
    i += 1