print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height>120:
    print('You can ride the rollercoaster')
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print('Your Ticket costs 5$')
    elif 12<age <=18:
        bill = 7
        print('Your ticket costs 7$')
    if age>18:
        bill = 12
        print('Your ticket is 12$')

    wants_photo = input('Do you want to have a photo take? type y for yes and n for no\n')
    if wants_photo == 'y':
        #add three dollars to bill
        bill += 3

    print(f'Your final bill is {bill}$')
else:
    print('You cannot ride the rollercoaster')