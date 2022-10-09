# Write a python script to calculate sum of first N natural numbers

# output:
# for n=5:
# sum=15 i.e. 1+2+3+4+5

n = int(input('Enter n:'))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)