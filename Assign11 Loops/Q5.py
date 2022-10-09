# Write a python script to calculate sum of first N even natural numbers

# output:
# for n=10:
# sum=110 i.e. 2+4+6+8+10+12+14+16+18+20

n = int(input('Enter n:'))
sum = 0
for i in range(1,n+1):
    sum += 2*i
print(sum)