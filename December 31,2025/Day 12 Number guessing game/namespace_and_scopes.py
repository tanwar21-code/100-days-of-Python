enemies = 1

def increase_enemies():
    enemies = 2
    print(f'Enemies inside function: {enemies}')

increase_enemies()
print(f'Enemies outside function: {enemies}')

#Local Scope
def potion():
    potion_strength = 2
    print(potion_strength)

potion()
print(potion_strength) #it gives a name error because it is not defined in the global scope
#it can only be accessed inside the function

#Global Scope
player_health = 10
print(player_health)

def drink_potion():
    potion_strength = 2
    print(player_health)

drink_potion()