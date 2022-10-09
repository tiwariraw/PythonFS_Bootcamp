# Write a python script to calculate sum of squares of first N natural numbers

# output:
# for n=6:
# sum=91 i.e. 1+4+9+16+25+36

n = int(input('Enter n:'))
sum = 0
for i in range(1,n+1):
    sum += i*i
print(sum)