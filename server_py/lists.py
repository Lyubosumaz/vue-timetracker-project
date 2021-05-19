myList = ['a','b','c','d','e']
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
matrix = [[1,2,3],[4,5,6],[7,8,9]]
first_col = [row[0] for row in matrix]
print(first_col)                            # [1, 4, 7]

# DICTIONARIES || HASH TABLES || OBJECT IN JS
my_stuff = {"key1": 'value', 'key2': 'value'}