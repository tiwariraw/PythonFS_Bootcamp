# Write a python script to count digits in a given number

# output:
# for n=3798:
# Number of digits is 4

n = abs(int(input('Enter a number:')))   #abs() is used to handle negative numbers
count = 0
if n==0:           # 0 is also a one digit number
    count=1
while n:
    count += 1
    n = n//10
print(count)



# M2 
n = input('Enter a number:')    #taking input as str and not int
if '-' in n:                    #for negative numbers
    n = n.replace('-','')
digits = len(n)                 #applying len() method of str class
print(digits)