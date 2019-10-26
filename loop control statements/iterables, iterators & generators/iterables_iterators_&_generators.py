import itertools

# These two loops will do exactly the same thing:

for i in (1, 2, 3, 4, 5):
    print(i)

for i in range(1, 6):
    print(i)

print('\n-------------------------------------------- ')
# this will not be very helpful
print(range(100))

print('\n-------------------------------------------- ')
# this will show you all the generated values
print(list(range(100)))

print('\n-------------------------------------------- ')
animals = ['cat', 'dog', 'fish']

for first_animal in animals:
    for second_animal in animals:
        print("Yesterday I bought a %s. Today I bought a %s." % (first_animal, second_animal))

print('\n-------------------------------------------- ')
# unlike range, count doesn't have an upper bound, and is not restricted to integers
# for i in itertools.count(1):
#     print(i) # 1, 2, 3....

# for i in itertools.count(1, 0.5):
#     print(i) # 1.0, 1.5, 2.0....

# cycle repeats the values in another iterable over and over
# for animal in itertools.cycle(['cat', 'dog']):
#     print(animal) # 'cat', 'dog', 'cat', 'dog'...

# repeat repeats a single item
# for i in itertools.repeat(1): # ...forever
#     print(i) # 1, 1, 1....

for i in itertools.repeat(1, 3):  # or a set number of times
    print(i)  # 1, 1, 1

print('\n-------------------------------------------- ')
# chain combines multiple iterables sequentially
numbers = [1, 5, 2, 12, 14, 7, 18]

for i in itertools.chain(numbers, animals):
    print(i)  # print all the numbers and then all the animals

print('\n-------------------------------------------- ')
for i in zip((1, 2, 3), (4, 5, 6)):
    print(i)

print('\n-------------------------------------------- ')
for i in zip(range(5), range(5, 10), range(10, 15)):
    print(i)