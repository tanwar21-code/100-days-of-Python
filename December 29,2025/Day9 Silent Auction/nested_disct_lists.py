capitals = {
    'USA': 'Washington D.C.',
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome',
    'Spain': 'Madrid'
}
#Nested list in Dictionary
countries_info = {
    'USA': [['Washington D.C.', 'New York', 'Los Angeles'], ['English', 'Spanish'], 331000000],
    'France': [['Paris', 'Lyon', 'Marseille'], ['French'], 67000000],
    'Germany': [['Berlin', 'Munich', 'Frankfurt'], ['German'], 83000000],
    'Italy': [['Rome', 'Milan', 'Naples'], ['Italian'], 60000000],
    'Spain': [['Madrid', 'Barcelona', 'Valencia'], ['Spanish'], 47000000]
}

# Accessing nested list elements
print(countries_info['USA'][0][1])
print(countries_info['France'][2])

#nesting a dictionart in a dictionary
students = {    
    'Alice': {'age': 20,
               'major': 'Computer Science',
                 'GPA': 3.8},
    'Bob': {'age': 22,
             'major': 'Mathematics', 
             'GPA': 3.5},
    'Charlie': {'age': 21, 
                'major': 'Physics', 
                'GPA': 3.7}
}

# Accessing nested dictionary elements
print(students['Charlie']['major'])