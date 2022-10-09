# Write a python script to print first n prime numbers

# output:
# for n=10:   ----->first 10 prime numbers
# 2 3 5 7 11 13 17 19 23 29

def main():
    num = int(input('Enter how many primes to print? '))
    first_n_prime(num)


def is_prime(n):                    
    for i in range(2, n):           
        if n % i == 0:
            return -1
    return n
        
            
            
def first_n_prime(num):
    start=2
    while num:
        prime = is_prime(start)
        if prime != -1:
            print(prime,end=' ')
            num -= 1
        start += 1
        
        
        
        

main()