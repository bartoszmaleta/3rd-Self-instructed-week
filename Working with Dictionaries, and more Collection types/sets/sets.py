print()
animals = {'cat', 'dog', 'goldfish', 'canary', 'cat'}
print(animals)  # the set will only contain one cat

print('\n-------------------------------------------- ')
even_numbers = {2, 4, 6, 8, 10}
big_numbers = {6, 7, 8, 9, 10}
print(even_numbers)
print(type(even_numbers))
print(big_numbers)

# subtraction: big numbers which are not even
print(big_numbers - even_numbers)

# union: numbers which are big or even
print(big_numbers | even_numbers)

# intersection: numbers which are big and even
print(big_numbers & even_numbers)

# numbers which are big or even but not both
print(big_numbers ^ even_numbers)

print('\n-------------------------------------------- ')
# It is important to note that unlike lists and tuples sets are not ordered.
# When we print a set, the order of the elements will be random. 
# If we want to process the contents of a set in a particular order,
# we will first need to convert it to a list or tuple and sort it:

print(animals)
print(sorted(animals))
print(type(sorted(animals)))    # list

print('\n-------------------------------------------- ')
# this is an empty dictionary
a = {}
print(type(a))

# this is how we make an empty set
b = set()
print(b)
print(type(b))