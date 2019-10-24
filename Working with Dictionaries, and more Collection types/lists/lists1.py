# a list of strings
animals = ['cat', 'dog', 'fish', 'bison']

# a list of integers
numbers = [1, 7, 34, 20, 12]

one_variable = 1
another_variable = 2
third_variable = 3

things = [
    one_variable,
    another_variable,
    third_variable,  # this trailing comma is legal in Python
]

print(things)

print('\n-------------------------------------------- ')
print(animals[0])  # cat
print(numbers[1])  # 7

# This will give us an error, because the list only has four elements
# print(animals[6]) 

print(animals[2:])  # ['fish', 'bison']
print(animals[:2])  # ['cat', 'dog']
print(animals[:])  # a copy of the whole list

print(animals[::2])  # ['cat', 'fish']

print('\n-------------------------------------------- ')
# assign a new value to an existing element
animals[3] = "hamster"

# add a new element to the end of the list
animals.append("squirrel")
print(animals)

# remove an element by its index
del animals[2]
print(animals)
animals.pop(2)
print(animals)

print('\n-------------------------------------------- ')
# Because lists are mutable, we can modify a list variable without assigning the variable a completely new value.
# Remember that if we assign the same list value to two variables, any in-place changes that we make while referring
#  to the list by one variable name will also be reflected when we access the list through the other variable name:

# animals = ['cat', 'dog', 'goldfish', 'canary']
# pets = animals # now both variables refer to the same list object

# animals.append('aardvark')
# print(pets) # pets is still the same list as animals

# animals = ['rat', 'gerbil', 'hamster'] # now we assign a new list value to animals
# print(pets) # pets still refers to the old list

# pets = animals[:] # assign a *copy* of animals to pets
# animals.append('aardvark')
# print(pets) # pets remains unchanged, because it refers to a copy, not the original list

print('\n-------------------------------------------- ')
numbers = [34, 67, 12, 29]
my_number = 67
print(numbers)

if my_number in numbers:
    print("%d is in the list!" % my_number)

my_number = 90
if my_number not in numbers:
    print("%d is not in the list!" % my_number)

# Note

# in and not in fall between the logical operators (and, or and not) and the identity operators (is and is not) in the order of precedence.

print('\n-------------------------------------------- ')
print(len(animals))
print(sum(numbers))
print(any([1, 0, 1, 0, 1]))  # are any of these values true?
print(all([1, 0, 1, 0, 1]))  # are all of these values true?

print('\n-------------------------------------------- ')
numbers = [1, 2, 3, 4, 5]

# we already saw how to add an element to the end
numbers.append(5)
print(numbers)

# count how many times a value appears in the list
numbers.count(5)
print(numbers)

# append several values at once to the end
numbers.extend([56, 2, 12])
print(numbers)

# find the index of a value
numbers.index(3)
print(numbers)

# if the value appears more than once, we will get the index of the first one
numbers.index(2)
print(numbers)

# if the value is not in the list, we will get a ValueError!
# numbers.index(42)
print(numbers)

# insert a value at a particular index
numbers.insert(0, 45)  # insert 45 at the beginning of the list
print(numbers)

# remove an element by its index and assign it to a variable
my_number = numbers.pop(0)
print(numbers)

# remove an element by its value
numbers.remove(12)
print(numbers)

# if the value appears more than once, only the first one will be removed
numbers.remove(5)
print(numbers)

print('\n-------------------------------------------- ')
numbers = [3, 2, 4, 1]

# these return a modified copy, which we can print
print(numbers)
print(sorted(numbers))
print(list(reversed(numbers)))

# the original list is unmodified
print(numbers)

print('\n-------------------------------------------- ')
# now we can modify it in place
print(numbers)
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)
print(type(numbers))
# The reversed function actually returns a generator, not a list (we will look at generators in the next chapter),
#  so we have to convert it to a list before we can print the contents.

print('\n-------------------------------------------- ')
# Here are some major differences between lists and arrays:

# - An array has a fixed size which you specify when you create it. If you need to add or remove elements, you have to make a new array.
# - If the language is statically typed, you also have to specify a single type for the values which you are going to put in the array when you create it.
# - In languages which have primitive types, arrays are usually not objects, so they don’t have any methods – they are just containers.

