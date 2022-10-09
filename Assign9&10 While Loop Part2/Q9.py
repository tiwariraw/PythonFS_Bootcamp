# Write a python script to print cubes of first N natural numbers

# output: 
# for n=5:
# 1 8 27 64 125

n=int(input('Enter n: '))
for i in range(1,n+1):
    print(i*i*i,end=' ')   #print(i**3)
    
    
# using while loop
i = 1
while i<=n:
    print(i*i*i,end=' ')
    i += 1