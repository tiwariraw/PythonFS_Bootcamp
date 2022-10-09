# Write a python script to calculate sum of first N odd natural numbers

# output:
# for n=10:
# sum=100 i.e. 1+3+5+7+9+11+13+15+17+19

n = int(input('Enter n:'))
sum = 0
for i in range(1,n+1):
    sum += 2*i-1
print(sum)