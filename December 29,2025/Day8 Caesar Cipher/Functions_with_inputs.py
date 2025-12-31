def greet_with_name(name):
    print('Hello! Welcome to the program.')
    print('This program demonstrates functions with input.')
    print(f'Nice to meet you, {name}!')

user_name = input('Please enter your name: ')
greet_with_name(user_name)

greet_with_name('Alice')  # Example of calling the function with a direct argument