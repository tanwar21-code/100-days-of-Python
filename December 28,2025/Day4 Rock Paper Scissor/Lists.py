#Lists are type of Data Structure

# fruits = [item1, item2]
fruits = ['cherry', 'apple', 'pear']
print(fruits[0]) #indexing of lists
print(fruits[-1])

fruits[0] = 'mango' #changing existing item
print(fruits[0])

fruits.append('pineapple') #adding item to end of the list
print(fruits[-1])

fruits.extend(['Gauava', 'Papaya']) #adding another list to existing list
print(fruits[-1])
print(fruits)

