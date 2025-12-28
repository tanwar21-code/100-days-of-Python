#index error
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
print(fruits[7])
# --- IGNORE ---
# Traceback (most recent call last):
#   File "D:/Learning Python/December 28,2025/Day4/index_Error.py", line 2, in <module>
#     print(fruits[7])
# IndexError: list index out of range
# --- IGNORE ---
#fix index error
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
print(fruits[6])
num_of_fruits = len(fruits)
print(fruits[num_of_fruits - 1])