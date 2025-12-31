#who pays the bill game\
import random
friends = ['Himanshu', 'Palak', 'Neha', 'Ansh']

#1 option
print(friends[random.randint(0,len(friends)-1)] + " is going to pay the bill today!")

#2 option
print(random.choice(friends) + " is going to pay the bill today!")