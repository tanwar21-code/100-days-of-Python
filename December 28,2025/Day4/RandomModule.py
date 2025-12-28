#Generating a random number
# import random as rd

# a = rd.randint(1,10)
# print(a)
#we can also use word 'random' directly

import random #importing random module
r = random.randint(1,10)
print(r)

import my_module #importing our own module
print(my_module.my_favourite_number)

random_number_0_to_1 = random.random() #for generating floating point number between 0 and 1(not including 1)
print(random_number_0_to_1)

#and for generating floating point number between any two numbers we can use this core function by multiplying and adding
random_number_a_to_b = random.random() * 10 + 5 #for generating floating point number between 5 and 15(not including 15)
print(random_number_a_to_b)

#we can also use uniform function
random_number_a_to_b_uniform = random.uniform(5,15) #for generating floating point number between 5 and 15(including 15)
print(random_number_a_to_b_uniform)