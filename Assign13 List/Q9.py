# Write a Python script to create a list of city names taken from the user.

l1 = []
while True:
    city = input('Enter a city name: ')
    l1.append(city)
    user_choice = input("Press 'q' to quit or any other key to continue: ")
    if user_choice == 'q':
        break
    
print(l1)