# Write a python script to print squares of first 10 natural numbers

# output: 1 4 9 16 25 36 49 64 81 100

for i in range(1,11):
    print(i*i,end=' ')            #print(i**2)
    

# using while loop
i = 1
while i<=10:
    print(i*i,end=' ')
    i += 1