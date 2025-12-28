height = 1.65 
weight = 84

# Write your code here.
# Calculate the bmi using weight and height.
bmi = 84/(1.65**2)

print(bmi)
print(int(bmi)) # Print the integer value of the bmi., it means it floors the value to the nearest whole number.
print(round(bmi)) # Print the rounded value of the bmi., it means it rounds the value to the nearest whole number by rounding up if the decimal is 0.5 or higher.
print(round(bmi,3)) # Print the bmi rounded to 3 decimal places.