# Write a python script to print Corona N times on the screen

n=int(input('Enter n: '))
for i in range(n):
    print('Corona')
    
# using while loop

# M1
n=int(input('Enter n: '))
while n:
    print('Corona')
    n -= 1

# M2
n=int(input('Enter n: '))
i=1
while i<=n:
    print('Corona')
    i -= 1
