#functions with more than one input
def greet_with(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')

greet_with("Jack", "New York")
greet_with(location="Los Angeles", name="Emily")
greet_with("Michael", location="Chicago")
greet_with(name="Sarah", location="Miami")
greet_with('sanfrancisco', 'john') #positional arguments
greet_with(location='boston', name='linda') #keyword arguments