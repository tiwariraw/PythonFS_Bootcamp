# Write a python script to calculate sum of cubes of first N natural numbers

# output:
# for n=5:
# sum=225 i.e. 1+8+27+64+125

n = int(input('Enter n:'))
sum = 0
for i in range(1,n+1):
    sum += i*i*i
print(sum)