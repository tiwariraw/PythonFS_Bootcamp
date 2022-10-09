# Write a python script to print cubes of first 10 natural numbers

# output: 1 8 27 64 125 216 343 512 729 1000

for i in range(1,11):
    print(i*i*i,end=' ')   #print(i**3)
    
    
# using while loop
i = 1
while i<=10:
    print(i*i*i,end=' ')
    i += 1