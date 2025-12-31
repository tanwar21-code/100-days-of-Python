bmi = 84/(1.65**2)

print(bmi)

print(int(bmi)) # Print the integer value of the bmi., it means it floors the value to the nearest whole number.

print(round(bmi)) # Print the rounded value of the bmi., it means it rounds the value to the nearest whole number by rounding up if the decimal is 0.5 or higher.

print(round(bmi,3)) # Print the bmi rounded to 3 decimal places.

#Assignment Operators in Python

score = 0
    #user scores a point

score += 1  # This is equivalent to score = score + 1
print(score)

score *= 2  # This is equivalent to score = score * 2
print(score)

score -= 1  # This is equivalent to score = score - 1
print(score)

score /= 3  # This is equivalent to score = score / 3
print(score)

score %= 2  # This is equivalent to score = score % 2
print(score)

score **= 3  # This is equivalent to score = score ** 3
print(score)

score //= 2  # This is equivalent to score = score // 2
print(score)

#f-strings in Python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
    # This will output: My name is Alice and I am 30 years old.
