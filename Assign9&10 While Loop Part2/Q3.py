# Write a python script to print first N natural numbers in reverse order

# output: 
# for n=5: 
# 5 4 3 2 1

n=int(input('Enter n: '))
for i in range(n,0,-1):      # for i in range(n):
    print(i,end=' ')         #      print(n-i)
    
    
# using while loop

# M1
i = n
while i>0:
    print(i)
    i -= 1
    