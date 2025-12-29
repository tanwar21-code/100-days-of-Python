programming_dictionary = {
    "Function": "A block of code which only runs when it is called. You can pass data, known as parameters, into a function.",
    "Variable": "A reserved memory location to store values. In programming, variables are used to hold data that can be changed later in the program.",
    "Loop": "A sequence of instructions that is continually repeated until a certain condition is reached   .",
}
# Adding a new entry to the dictionary
programming_dictionary["List"] = "A collection which is ordered and changeable. In Python, lists are written with square brackets."

# Retrieving an item from the dictionary
print(programming_dictionary["Function"])

# Creating an empty dictionary
empty_dictionary = {}

# Wiping an existing dictionary
# programming_dictionary = {}

# Editing an item in the dictionary
programming_dictionary["Function"] = "A reusable block of code that performs a specific task."

# Looping through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])