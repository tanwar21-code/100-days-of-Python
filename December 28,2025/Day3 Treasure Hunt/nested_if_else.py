#nested if -else
print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm? "))

if height>120:
    print('You can ride the rollercoaster')
    age = int(input("What is your age? "))
    if age < 12:
        print('Your Ticket costs 5$')
    elif 12<age <=18:
        print('Your ticket costs 7$')
    if age>18:
        print('Your ticket is 12$')
else:
    print('You cannot ride the rollercoaster')