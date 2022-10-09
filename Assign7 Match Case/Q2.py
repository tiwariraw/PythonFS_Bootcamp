# Write a menu driven program to perform following operations - Addition, Subtraction,Multiplication, Division
import sys

def main():
    while True:
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')
        print('4. Divide')
        print('5. Exit')
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
        ch = int(input('Enter your choice: '))
        match ch:
            case 1:
                print('Addition is: ',num1+num2)
            case 2:
                print('Subtraction is: ',num1-num2)
            case 3:
                print('Multiplication is: ',num1*num2)
            case 4:
                print('True Division is: ',num1/num2)
            case 5:
                sys.exit()
            case _:
                print('Invalid Choice')   
            
if __name__ == '__main__':
    main()