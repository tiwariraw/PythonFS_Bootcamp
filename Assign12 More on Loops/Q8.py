# Write a python script to calculate LCM(Least Common Multiple) of two numbers

# lcm(4,6) = 12
# multiples of 4: 4 8 12 16 20 24 28 32 36 40 ...
# multiples of 6: 6 12 18 24 30 36 42 48 54 60 ...

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
largest = n1 if n1>n2 else n2
for i in range(largest, n1*n2+1):
    if i%n1==0 and i%n2==0:
        break
print('LCM is: ',i)