WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

animals = ('cat', 'dog', 'fish')
print(animals)

# an empty tuple
my_tuple = ()
print(my_tuple)
print(type(my_tuple))

# we can access a single element
print(animals[0])

print('\n-------------------------------------------- ')
# we can get a slice
print(animals[1:])  # note that our slice will be a new tuple, not a list

# we can count values or look up an index
print(animals.count('cat'))
print(animals)

print('\n-------------------------------------------- ')
print(animals.index('cat'))
print(animals)

# ... but this is not allowed: !!!!!!!!!!!!!!
# animals.append('canary') 
print(animals)

# animals[1] = 'gerbil'
print(animals)

print('\n-------------------------------------------- ')
# What are tuples good for? We can use them to create a sequence of values that we don’t want to modify. 
# For example, the list of weekday names is never going to change. If we store it in a tuple,
#  we can make sure it is never modified accidentally in an unexpected place:

# Here's what can happen if we put our weekdays in a mutable list

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
print(WEEKDAYS)


def print_funny_weekday_list(weekdays):
    weekdays[5] = 'Caturday'  # this is going to modify the original list!
    print(weekdays)


print_funny_weekday_list(WEEKDAYS)

print(WEEKDAYS)  # oops

print('\n-------------------------------------------- ')
print("%d %d %d" % (1, 2, 3))

print('\n-------------------------------------------- ')
print(3)    # dont generate tuples
print((3))

print((3,))     # creates a tuple!!!!

