# Write a python program to check whether a given string is a multiword string or single word string using match case statement

#Logic: single word or multi word can be checked based on the presence or absence of space present

def main():
    s1 = input('Enter a string: ').strip()   #strip() becuase user can give a single word followed by one or more spaces(ashish )
    match s1:
        case s1 if ' ' in s1:
            print('Multi word String')
        case s1 if ' ' not in s1:
            print('Single Word String')


if __name__ == '__main__':
    main()
    
#strip() removes leading and trailing spaces