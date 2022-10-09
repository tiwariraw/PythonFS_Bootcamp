# Q1 WPS to calculate radius of a circle
PI = 3.14
radius = float(input('Enter radius: '))
print(PI*radius*radius)

# Q2 WPS to print values of three variables, each in a new line
a,b,c = 2,4,6
print(a,b,c,sep='\n')

# Q3 WPS to print id of two variables containing the same integer values
#a and b are two different names referring to the same integer object (5) because their id's are same
a=5
b=5
print(id(a))         
print(id(b))

# Q4 WPS to print all the keyword
import keyword
print(keyword.kwlist)
print(f'total keyword = {len(keyword.kwlist)}')

# Q5Name the keywords used as data in python
True, False, None

# Q6 WPS to add two numbers 25(in octal) and 39(in hexadecimal) and display the result in binary format
num1 = 0o25       #dec equiv is 21 and bin equiv is 10101
num2 = 0x39       #dec equiv is 57 and bin quiv is 111001
print(num1+num2)  #sum should be 78 (in decimal) and 1001110(in binary)



# Q7 WPS to know the version of python you are using
import sys
print(sys.version)

# Q8 WPS to print "Ashish" as it is
print('"Ashish"')    
print("\"Ashish\"")

# Q9 WPS to remove the last digit of a given number.(eg. 2534 ---> 253)
n = int(input('Enter a number: '))
n = n//10  # Method2: n = int(n/10) 
print(n)

# Q10 WPS to get the last digit of a given number.(eg. 759 ---> 9)
n = int(input('Enter a number: '))
n = n%10 
print(n)

# Q11 WPS to swap data of two variable (Pythonic way)
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
a,b = b,a  
print('a = ',a,'b = ',b)
# https://www.youtube.com/watch?v=KdGndqToDOg   (ROT_TWO)
# https://betterprogramming.pub/you-didnt-truly-understand-the-infamous-python-trick-a-b-b-a-2e4e8634f5a9

# Q12 WPs to find x power y, where x and y are given by user
x = int('Enter a number: ')
y = int('Enter the power: ')
print(x**y)

# Q13 WPS which takes a 3 digit number from the user and displays its first digit
n = int(input('Enter a 3 digit number: '))
n = n//100
print(n)

# Q14 WPS which takes a 3 digit number from the user and displays only its middle digit
n = int(input('Enter a 3 digit number: '))
n = (n//10) % 10
print(n)

# Q15 WPS which takes a 3 digit number from the user and displays only its last digit
n = int(input('Enter a 3 digit number: '))
n = n%10
print(n)

# Q16 WPS to use "is" operator to display if both variables are referring to the same object or not
a = 5
b = 5
print(a is b)  # returns True if id of a and b is same

# ***for list object***

list1 = [2,4,6,8]
list2 = [2,4,6,8]
print(list1 is list2) #False
print(list1 == list2) #True

# Q17 WPS to use "in" operator to display the data present in the list
list1 = [2,5,7]
print(2 in list1) # True
print(3 in list1) # False


# Q18 WPS to use "not in" operator to display the data not present in the list
list1 = [2,5,7]
print(9 not in list1) # True
print(2 not in list1) # false

# Q19 WPS to print two given words in dictionary order
word1 = input('Enter first word: ')
word2 = input('Enter second word: ')
if word1<word2:
    print(word1,word2)
else:
    print(word2,word1)

    
# Q20 WPS to check whether a given number is a 3 digit number or not

# M1 
n = int(input('Enter a number: '))
if abs(n)>99 and abs(n)<1000:
    print('Three digit number')
else:
    print('Not a three digit number')

# M2
n = int(input('Enter a number: '))
if 99<n<1000:
    print('Three digit number')
else:
    print('Not a three digit number')

# Q21 WPS to check whether a given year is a leap year or not

# M1
year = int(input('Enter an year: '))
# check for century year
if year % 100 == 0:
    if year%400 == 0:
        print('Leap Year')
    else:
        print('Not a leap year')       
else:
    if year%4 == 0:
        print('Leap Year')
    else:
        print('Not a leap year')

# M2
year = int(input('Enter an year: '))
if year%400 == 0 or year%100 != 0 and year%4 == 0:
    print('Leap Year')
else:
    print('Not a leap year')

# Q22 WPS to print greatest number among given three numbers
print('Enter 3 numbers: ')
a,b,c = int(input()), int(input()), int(input())
if a>b:
    if a>c:
        print(f'{a} is greatest')
    else:
        print(f'{c} is greatest')
else:
    if b>c:
        print(f'{b} is greatest')
    else:
        print(f'{c} is greatest')

# Q23 WPS to accept one complex number from the user and display the greater number between real part and imaginary part
# real and imag are 2 attributes of complex class
z = complex(input('Enter a complex number: '))
if z.real > z.imag:
    print(z.real)
else:
    print(z.imag)  

# Q24 WPS to take the month value in numeric format and display the number of days in it. 
month = int(input('Enter month number(1-12): '))
if month in (1,3,5,7,8,10,12):
    print('31 days')
elif month in (4,6,9,11):
    print('30 days')
elif month==2:
    print('28 or 29 days')
else:
    print('Invalid month number')  

# Q25 WPS to check if a number is divisible by 5 or not
print('Divisible' if int(input('Enter a number: ')) % 5 == 0 else 'Not divisible')