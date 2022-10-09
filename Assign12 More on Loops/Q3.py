# Write a python script to print all Prime numbers under 100

def print_prime(n):
    for i in range(2,n):
        flag=1
        for j in range(2,i):
            if i%j==0:
                flag=0
                break
        if flag==1:
            print(i,end=' ')

print_prime(101)
    