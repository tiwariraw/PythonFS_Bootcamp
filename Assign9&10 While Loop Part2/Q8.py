# Write a python script to print squares of first N natural numbers

# output: 
# for n=5:
# 1 4 9 16 25

n=int(input('Enter n: '))
for i in range(1,n+1):
    print(i*i,end=' ')            #print(i**2)
    

# using while loop
i = 1
while i<=n:
    print(i*i,end=' ')
    i += 1