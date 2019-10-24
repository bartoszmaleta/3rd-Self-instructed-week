animals = ['cat', 'dog', 'goldfish', 'canary', 'cat']
print(type(animals))
print(animals)

animals_set = set(animals)
print(animals_set)
print(type(animals_set))

animals_unique_list = list(animals_set)
print(animals_unique_list)
print(type(animals_unique_list))

animals_unique_tuple = tuple(animals_unique_list)
print(animals_unique_tuple)
print(type(animals_unique_tuple))


print('\n-------------------------------------------- ')
marbles = {"red": 34, "green": 30, "brown": 31, "yellow": 29}
print(marbles)
print(type(marbles))


colours = list(marbles)  # the keys will be used by default
print(colours)
print(type(colours))

counts = tuple(marbles.values())  # but we can use a view to get the values
print(counts)
print(type(counts))

marbles_set = set(marbles.items())  # or the key-value pairs
print(marbles_set)
print(type(marbles_set))

print('\n-------------------------------------------- ')
colours_marbles = list(marbles.items())
print(colours_marbles)

tuple_marbles = tuple(marbles.items())
print(tuple_marbles)

print('\n-------------------------------------------- ')
# We can also convert a sequence to a dictionary, but only if it’s a sequence of pairs – each pair must itself be a sequence with two values: !!!!!!!!!!!!!!!!!!

# Python doesn't know how to convert this into a dictionary
# dict([1, 2, 3, 4])
# print(dict1)

# but this will work
dict2 = dict([(1, 2), (3, 4)])
print(dict2)

print('\n-------------------------------------------- ')
print('\n-------------------------------------------- ')
s = "abracadabra"

print(len(s))
print(s.index("a"))

print(s[0])
print(s[3:5])

print('\n-------------------------------------------- ')
# The membership operator has special behaviour when applied to strings: we can use it to determine 
# if a string contains a single character as an element, but we can also use it to check if a string contains a substring:

print('a' in 'abcd')  # True
print('ab' in 'abcd')  # also True

# this doesn't work for lists
print(['a', 'b'] in ['a', 'b', 'c', 'd'])  # False

print('\n-------------------------------------------- ')
abc_list = list("abracadabra")
print(abc_list)

print('\n-------------------------------------------- ')
list_of_letters = ['a', 'b', 'r', 'a', 'c', 'a', 'd', 'a', 'b', 'r', 'a']
print(list_of_letters)

s = "".join(list_of_letters)
print(s)

print('\n-------------------------------------------- ')
animals = ('cat', 'dog', 'fish')
print("This is a list:", animals)

# a space-separated list
print(" ".join(animals))

# a comma-separated list
print(",".join(animals))

# a comma-separated list with spaces
print(", ".join(animals))

print('\n-------------------------------------------- ')
# The opposite of joining is splitting. We can split up a string into a list of strings by using the split method. 
# If called without any parameters, split divides up a string into words, using any number of consecutive 
# whitespace characters as a delimiter. We can use additional parameters to specify a different delimiter 
# as well as a limit on the maximum number of splits to perform:

print("cat    dog fish\n".split())
print("cat|dog|fish".split("|"))
print("cat, dog, fish".split(", "))
print("cat, dog, fish".split(", ", 1))