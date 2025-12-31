#Logical Operators
#And, Or, Not
#And
#True if both statements are true
print(True and True)   #True
print(True and False)  #False
print(False and True)  #False
print(False and False) #False
#Or
#True if at least one statement is true
print(True or True)    #True
print(True or False)   #True
print(False or True)   #True
print(False or False)  #False
#Not
#Reverses the result, returns False if the result is true
print(not True)        #False
print(not False)       #True
#Example Usage

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
    elif age>= 45 and age<=55:
        bill = 0
        print('Your ticket is free')
    else:
        bill = 12
        print('Your ticket is 12$')

    wants_photo = input('Do you want to have a photo take? type y for yes and n for no\n')
    if wants_photo == 'y':
        #add three dollars to bill
        bill += 3

    print(f'Your final bill is {bill}$')
else:
    print('You cannot ride the rollercoaster')