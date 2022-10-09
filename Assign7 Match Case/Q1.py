#Write a python script to display the number of days in a given month number.

# Logic: To combine multiple cases under one case, use | (pipe)
month = int(input('Enter a month number: '))
match month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:    # case month if month in (1,3,5,7,8,10,12):
        print('31 days')
    case 4 | 6 | 9 | 11:                 # case month if month in (4,6,9,1,):
        print('30 days')
    case 2:
        print('28 or 29 days')
    case other:                          # case _
        print('Enter a valid month number')
        
