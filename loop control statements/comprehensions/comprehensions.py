numbers = [1, 5, 2, 12, 14, 7, 18]

doubles = []
for number in numbers:
    doubles.append(2 * number)
print(numbers)
print(doubles)

print('\n-------------------------------------------- ')
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(numbers)
print(even_numbers)

print('\n-------------------------------------------- ')
animals = ['aardvark', 'cat', 'dog', 'opossum']

vowel_animals = []
for animal in animals:
    if animal[0] in 'aeiou':
        vowel_animals.append(animal)
    print(animal[1])  # second letter of name of animal

print(animals)
print(vowel_animals)

print('\n-------------------------------------------- ')
# That’s quite an unwieldy way to do something very simple. 
# Fortunately, we can rewrite simple loops like this to use a cleaner 
# and more readable syntax by using comprehensions.

# A comprehension is a kind of filter which we can define on an iterable 
# based on some condition. The result is another iterable. Here are some 
# examples of list comprehensions:

doubles = [2 * number for number in numbers]
print(doubles)

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

vowel_animals = [animal for animal in animals if animal[0] in 'aeiou']
print(vowel_animals)

# The comprehension is the part written between square brackets on each line. 
# Each of these comprehensions results in the creation of a new list object.

print('\n-------------------------------------------- ')
numbers = [1, 5, 2, 12, 14, 7, 18]
print(numbers)

print('\n-------------------------------------------- ')
# a generator comprehension
doubles_generator = (2 * number for number in numbers)
print(doubles_generator)
print(numbers)

print('\n-------------------------------------------- ')
# a set comprehension
doubles_set = {2 * number for number in numbers}
print(doubles_set)  # http://pythontutor.com to check how it works with order

print('\n-------------------------------------------- ')
# a dict comprehension which uses the number as the key and the doubled number as the value
doubles_dict = {number: 2 * number for number in numbers}
print(doubles_dict)

print('\n-------------------------------------------- ')
sum_doubles = sum(2 * number for number in numbers)
print(sum_doubles)

