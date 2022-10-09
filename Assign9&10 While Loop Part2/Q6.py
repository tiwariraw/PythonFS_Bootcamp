# Write a python script to print first N even natural numbers

# output: 
# for n=5:
# 2 4 6 8 10

n=int(input('Enter n: '))
for i in range(1,n+1):
    print(2*i,end=' ')
    
    
# using while loop
i = 1
while i<=n:
    print(2*i,end=' ')
    i += 1