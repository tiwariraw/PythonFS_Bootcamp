# Write a program which takes a number from user. Print Even if the number is even, print Negative Odd if the number is negative odd number and print Positive Odd if number is positive odd number.

def main():
    n = int(input('Enter a number: '))
    match n:
        case n if n%2==0:
            print('Even')
        case n if n<0 and n%2==1:
            print('Negative Odd')
        case n if n>0 and n%2==1:
            print('Positive Odd')


if __name__ == '__main__':
    main()