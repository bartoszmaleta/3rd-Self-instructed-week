marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29}
print(marbles)
personal_details = {
    "name": "Jane Doe",
    "age": 38,  # trailing comma is legal!!!!
}
print(personal_details)

print('\n-------------------------------------------- ')
print(marbles["green"])
print(personal_details["name"])

# This will give us an error, because there is no such key in the dictionary!!!!!!!!!!!!
# print(marbles["blue"])

# modify a value
marbles["red"] += 3
print(marbles["red"])

personal_details["name"] = "Jane Q. Doe"
print(personal_details["name"])

print('\n-------------------------------------------- ')
# The keys of a dictionary don’t have to be strings – they can be any immutable type, 
# including numbers and even tuples. We can mix different types of keys and different types of values in one dictionary. 
# Keys are unique – if we repeat a key, we will overwrite the old value with the new value. 
# When we store a value in a dictionary, the key doesn’t have to exist – it will be created automatically:

battleship_guesses = {
    (3, 4): False,
    (2, 6): True,
    (2, 5): True,
}

surnames = {}  # this is an empty dictionary
surnames["John"] = "Smith"
surnames["John"] = "Doe"
print(surnames)  # we overwrote the older surname

print('\n-------------------------------------------- ')
marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29}
print(marbles)
marbles["blue"] = 30  # this will work
print(marbles)
# marbles["purple"] += 2 # this will fail -- the increment operator needs an existing value to modify!!!!!

print('\n-------------------------------------------- commonly used methods of dictionary objects:')
marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29}
print(marbles)

# Get a value by its key, or None if it doesn't exist
print(marbles.get("orange"))

print(marbles.get("brown"))


# We can specify a different default
print(marbles.get("orange", 0))     # zero after coma means new default
print(marbles)


print('\n-------------------------------------------- 2 commonly used methods of dictionary objects:')
# Add several items to the dictionary at once
marbles.update({"orange": 34, "blue": 23, "purple": 36})
print(marbles)

# All the keys in the dictionary
marbles.keys()
print(marbles.keys())

# All the values in the dictionary
marbles.values()
print(marbles.values())

# All the items in the dictionary
marbles.items()
print(marbles.items())

print('\n-------------------------------------------- ')
# We can check if a key is in the dictionary using in and not in:

print("purple" in marbles)
print("white" not in marbles)
print("lagoon" in marbles)

print('\n-------------------------------------------- ')
# We can also check if a value is in the dictionary using in in conjunction with the values method:

print("Smith" in surnames.values())

print('\n-------------------------------------------- ')
# You should avoid using mykey in mydict.keys() to check for key membership, 
# however, because it’s less efficient than mykey in mydict. !!!!!

print('\n-------------------------------------------- ')
# Note

# in Python 2, keys, values and items return list copies of these sequences, 
# iterkeys, itervalues and iteritems return iterator objects, and viewkeys, viewvalues and 
# viewitems return the view objects which are the default in Python 3 (but these are only available in Python 2.7 and above). 
# In Python 2 you should really not use mykey in mydict.keys() to check for key membership – if you do, you will be 
# searching the entire list of keys sequentially, which is much slower than a direct dictionary lookup.