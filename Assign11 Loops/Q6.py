# Write a python script to calculate factorial of a given number

# output:
# for n=5:
# factorial of 5 is 120

n = int(input('Enter n:'))
if n<0:
    print('Factorial of negative numbers is not possible to calculate')
else:
    fact = 1
    for i in range(1,n+1):   #better way: range(2,n+1)
        fact = fact*i
    print(fact)