# Write a python script to print first N odd natural numbers in reverse order

# output: 
# for n=5:
# 19 17 15 13 11 

n=int(input('Enter n: '))
for i in range(n,0,-1):
    print(2*i-1,end=' ')
    

# using while loop
i = n
while i>0:
    print(2*i-1,end=' ')
    i -= 1