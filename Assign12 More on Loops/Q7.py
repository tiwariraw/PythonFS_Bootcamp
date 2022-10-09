# Write a python script to print first N terms of a Fibonacci series

# output:
# n=10:
# 0 1 1 2 3 5 8 13 21 34

# M1
def main():
    n = int(input('Enter number of terms to print: '))
    fib(n)
    

def fib(n):
    a,b = 0,1
    while n:
        print(a,end=' ')
        a,b = b,a+b
        n -= 1


main()


# M2 (using generator)




