print('Welcome to Tip Calcuator:-')
bill = float(input('What is the total bill:-\n'))
tip = float(input('What is tip, you want to give? 10, 12, or 15 %? :-\n'))
split = float(input('How many people will split the Bill:-\n'))

share = (bill + (bill*(tip/100)))/split
print(f'Your share of bill is {round(share,2)}.')
