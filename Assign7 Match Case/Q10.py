# Write a program to display day name on the basis of user’s liking of a colour. Ask user for his favorite colour. User can answer in a sentence like “I like red colour”.
# Use match case to display day name associated with the colour.
# a. yellow - Monday
# b. blue - Tuesday
# c. orange - Wednesday
# d. white - Thursday
# e. black - Friday
# f. red - Saturday
# g. all other colours - Sunday

def main():
    user_input = input('What is your favourite color? ').lower()
    
    match user_input:
        case user_input if 'yellow' in  user_input:
            print('Monday')
        case user_input if 'blue' in  user_input:
            print('Tuesday')
        case user_input if 'orange' in  user_input:
            print('Wednesday')
        case user_input if 'white' in  user_input:
            print('Thursday')
        case user_input if 'black' in  user_input:
            print('Friday')
        case user_input if 'red' in  user_input:
            print('Saturday')
        case _:
            print('Sunday')


if __name__ == '__main__':
    main()