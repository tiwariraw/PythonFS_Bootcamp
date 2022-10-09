# Write a python program to check whether a given number is positive, negative or zero using match case statement

def main():
    n = int(input('Enter a number: '))
    match n:
        case n if n>0:
            print('Positive')
        case n if n<0:
            print('Negative')
        case n if n==0:
            print('Zero')
            


if __name__ == '__main__':
    main()