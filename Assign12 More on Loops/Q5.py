# Write a python script to find next prime number of a given number

def main():
    n = int(input('Enter a number: '))
    if n<2:
        n=2
    np = next_prime(n)
    print(np)


def next_prime(n):
    while True:
        n = n+1
        for i in range(2,n):
            if n%i==0:
                break
        else:                 # ye else tab hi chalega jab break na chala ho for loop ka
            return n


main()