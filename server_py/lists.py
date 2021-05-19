myList = ['a', 'b', 'c', 'd', 'e']
listTwo = ['x', 'y', 'z']
print(len(myList))
print(myList[1:], 'grab everything from index 1')
print(myList[:3], 'grab everything from index 0 till index 3 not included (0, 1, 2)')
print('before the reassignment:', myList)   # ['a','b','c','d','e']
myList[0] = 'NEW ITEM'                      # ['NEW ITEM','b','c','d','e']
myList.append('APPEND ITEM')                # ['NEW ITEM','b','c','d','e','APPEND ITEM']
myList.append(listTwo)                      # ['NEW ITEM','b','c','d','e','APPEND ITEM',['x', 'y', 'z']]
myList.extend(listTwo)                      # ['NEW ITEM','b','c','d','e','APPEND ITEM',['x', 'y', 'z'],'x', 'y', 'z']
item = myList.pop()
print(item, 'pop like in JS')
item2 = myList.pop(1)
print(item2, 'pop existing index')
print(myList[5][1], 'targetting nesting')
print('after the reassignment:', myList)    # ['NEW ITEM','c','d','e','APPEND ITEM',['x', 'y', 'z'],'x', 'y']

# LIST COMPREHENSION
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
first_col = [row[0] for row in matrix]
print(first_col)                            # [1, 4, 7]

# DICTIONARIES || HASH TABLES || OBJECT IN JS
my_stuff = {"key1": 'value1', 'key2': 'value2', 'key3': {'123': [1, 2, 3, 'grabMe']}}
print(my_stuff['key1'])
print(my_stuff['key2'])
print(my_stuff['key3']['123'][3].upper())

my_food = {'lunch': "pizza", "breakfast": 'eggs'}
my_food['lunch'] = 'burger'
my_food['dinner'] = 'pasta'
print(my_food['lunch'])
print(my_food)

# TUPLES, SET, BOOLEANS
True
False

my_tuple = (1, 2, 3)
print(my_tuple[0])

my_tuple = ('a', True, 123)
print(my_tuple)
# my_tuple[0] = 'NEW'  # throw an error, tuple is immutable like string is

my_set = set()
my_set.add(1)
my_set.add(5)
my_set.add(8)
my_set.add(8)
my_set.add(8)
my_set.add(8)
my_set.add(8)
my_set.add(-2)
my_set.add(0.3)
print(my_set)

x = set([1, 1, 1, 1, 1, 1, 1, 3, 3, 4, 4, 3, 3, 3, 4, 3])
print(x)
