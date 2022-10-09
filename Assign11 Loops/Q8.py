# Write a python script to calculate sum of digits of a given number

# output:
# for n=325:              #positive number
# sum is 10 i.e (3+2+5)
# for n=-325:             #negative number
# sum is 10 i.e (3+2+5)

n = abs(int(input('Enter a number:')))   #abs() is used to handle negative numbers
sum = 0
while n:
    sum += n%10
    n = n//10
print(sum)


# M2 
n = input('Enter a number:') 
sum = 0   
for e in n:
    sum += int(e)              
print(sum)

# M3
n = input('Enter a number:') 
print(sum([int(e) for e in n]))     #sum() applied on list