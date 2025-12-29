def life_in_weeks(age):
    years_remaining = 90 - age
    weeks = years_remaining * 52
    print(f'You have {weeks} weeks left.')

user_age = int(input('Enter your age: '))
life_in_weeks(user_age)