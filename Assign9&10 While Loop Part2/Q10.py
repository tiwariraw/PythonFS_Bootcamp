# Write a python script to print first 10 multiples of N

# output: 
# for n=6:
# 5 10 15 20 25 30 35 40 45 50

n=int(input('Enter n: '))
for i in range(1,11):
    print(n*i,end=' ')
    
    
# using while loop
i = 1
while i<=10:
    print(f'{n}*{i} = {n*i}')
    i += 1