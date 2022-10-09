# Write a python script to print first N even natural numbers in reverse order

# output: 
# for n=5:
# 20 18 16 14 12

n=int(input('Enter n: '))
for i in range(n,0,-1):
    print(2*i,end=' ')
    
    
# using while loop
i = n
while i>0:
    print(2*i,end=' ')
    i -= 1