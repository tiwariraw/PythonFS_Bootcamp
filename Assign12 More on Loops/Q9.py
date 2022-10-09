# Write a python script to calculate HCF(Highest Common Factor) of two numbers

# hcf(4,6) = 2
# factors of 4: 1 2 4
# factors of 6: 1 2 3 6

n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
hcf=1
smallest = n1 if n1<n2 else n2
for i in range(1, smallest+1):
    if n1%i==0 and n2%i==0:
        hcf=i
print('Hcf is: ',hcf)

# HCF of two numbers is less than or equal to the smallest of the two. It can't be greater than small number.
# HCF(4,6) <=4