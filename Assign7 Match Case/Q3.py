# Write a menu driven program with the following options:
# a. Check whether a given set of three numbers are lengths of an isosceles
# triangle or not
# b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not
# c. Check whether a given set of three numbers are equilateral triangle or not
# d. Exit.

import sys

def main():
    while True:
        print('-------------------')
        print('1. Right Angled Triangle')       #pythagoras theorem     #usecase: 3,4,5
        print('2. Isoceles Triangle')           #two sides equal        #usecase: 3,3,5
        print('3. Equilateral Triangle')        #all(3) sides equal     #usecase: 3,3,3
        print('4. Exit')
        print('Enter three sides: ')
        a,b,c = int(input()),int(input()),int(input())
        ch = int(input('Enter your choice: '))
        
        match ch:
            case 1:
                if (a**2+b**2 == c**2) or (b**2+c**2 == a**2) or (a**2+c**2 == b**2):
                    print('Sides of a Right Angled Triangle')
                else:
                    print('Not a Right Angled Triangle')
            case 2:
                if (a==b!=c) or (a==c!=b) or (b==c!=a):
                    print('Sides of an Isoceles Triangle')
                else:
                    print('Not an Isoceles Triangle')
            case 3:
                if a==b==c:
                    print('Sides of an Equilateral Triangle')
                else:
                    print('Not an Equilateral Triangle')
            case 4:
                sys.exit()
            case _:
                print('Invalid Choice')   
            
if __name__ == '__main__':
    main()