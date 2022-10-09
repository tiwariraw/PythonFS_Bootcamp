# Write a program which takes user’s age and display the category of person. 
# Age below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -Experienced, Age above or equal 60 - Senior Citizen.
import sys

def main():
    age = int(input('Enter your age: '))
    
    if age<=0:
        print('Invalid age')
        sys.exit()
        
    match age:
        case age if age<10:
            print('Kid')
        case age if age<20:
            print('Teen')
        case age if age<40:
            print('Young')
        case age if age<60:
            print('Experienced')
        case age if age>=60:
            print('Senior Citizen')


if __name__ == '__main__':
    main()