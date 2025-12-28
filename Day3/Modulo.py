#Modulo Operator
# The modulo operator (%) returns the remainder of a division operation.
# For example, 7 % 3 returns 1 because 7 divided by 3 is 2 with a remainder of 1.
# Here are some examples of using the modulo operator in Python:
print("Modulo Operator Examples:")
print("7 % 3 =", 7 % 3)  # Output: 1
print("10 % 4 =", 10 % 4)  # Output: 2
print("15 % 6 =", 15 % 6)  # Output: 3

#Properties of Modulo Operator
# 1. a % b = a if a < b
# 2. a % b = 0 if a is divisible by b
# 3. (a + b) % c = [(a % c) + (b % c)] % c
# 4. (a * b) % c = [(a % c) * (b % c)] % c

#Checking Even or Odd
number = int(input("Enter a number to check if it's even or odd: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

