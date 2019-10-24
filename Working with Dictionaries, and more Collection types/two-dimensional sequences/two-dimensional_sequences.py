my_table = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

print(my_table)
print(my_table[0][0])

# lists are mutable, so we can do this
my_table[0][0] = 42
print(my_table[0][0])

print('\n-------------------------------------------- ')
# When we use a two-dimensional sequence to represent tabular data, 
# each inner sequence will have the same length, because a table is 
# rectangular – but nothing is stopping us from constructing two-dimensional 
# sequences which don’t have this property:

my_2d_list = [
    [0],
    [1, 2, 3, 4],
    [5, 6],
]
print(my_2d_list)

print('\n-------------------------------------------- ')
my_3d_list = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
]
print(my_3d_list)
print(my_3d_list[0][0][0])

print('\n-------------------------------------------- ')
my_long_list = [0] * 100  # a long list of zeros
print(my_long_list)

print('\n-------------------------------------------- ')
# You might think of using this method to construct our timetable. 
# We can certainly use it to create a list of empty strings to represent a day:

day = [""] * 24
print(day)

print('\n-------------------------------------------- ')
# But what happens if we repeat a day seven times to make a week?

timetable = [day] * 7
print(timetable)

print('\n-------------------------------------------- ')
timetable[0][15] = "meeting with Jane"
print(timetable)

print('\n-------------------------------------------- ')
timetable = [[""] * 24 for day in range(7)]  # do not work how it should
timetable[0][15] = "meeting with Jane"
print(timetable)