a = [1, 2, 3]
b = a
a.append(4)

print(b)

# It may surprise you but the answer is [1, 2, 3, 4]. This is because a and b are 
# variables that refer to the same list, and .append() will modify that list.

print('\n-------------------------------------------- ')
# You can pass objects to functions and modify them

# Here is another example:


def modify_board(board, idx, mark):
    board[idx] = mark


my_board = [' '] * 9
print(my_board)  # will print: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

modify_board(my_board, 4, 'X')
print(my_board)  # will print: [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']

# The modify_board function does not return the new board. It modifies the board in-place.

print('\n-------------------------------------------- ')
a = "Hello"
b = a
a += " world"

print(b)

# This time, the answer will be just "Hello", not "Hello world". This is because a is a string, 
# and strings are immutable: they are never changed in-place. So a += "world" will create a new 
# string, and b will still refer to the old one.

print('\n-------------------------------------------- ')
# Here is how it looks like in PythonTutor:
# If you create a new object, you will have to pass it back
# Let's take a look at another function:

# Does not work:


def multiply_by_2(num):
    num *= 2


my_num = 10
multiply_by_2(my_num)
print(my_num)  # will still print 10
# The multiply_by_2 function looks like modify_board, but it doesn't actually work. This is 
# because it does not modify a number in place, it sets the num variable to a new number, 
# while my_num is still the old number.

# To make the example work, you need to return the new number:


def multiply_by_2(num):
    return num * 2


my_num = 10
my_num = multiply_by_2(my_num)
print(my_num)  # will print 20
# Notice how we return the value in the function (return num * 2), and assign the 
# result to the variable again (my_num = multiply_by_2(my_num)).

print('\n-------------------------------------------- ')
# Objects can be copied
# Let's go back to the example with lists. What if we want to modify one list (a), 
# but also keep the other one (b)?

# We need to copy the list, so that we have two separate objects:

a = [1, 2, 3]
b = list(a)  # create a new list from a
print(a)
print(b)

a.append(4)

print(a)  # [1, 2, 3, 4]
print(b)  # [1, 2, 3]

print('\n-------------------------------------------- ')
# [optional] Shallow and deep copying
# Note that the situation is a bit different when you have, for example, a list of lists. 
# If you have a list like [[1, 2, 3]] (a list inside a list), and try to copy it, you will 
# end up with something like this:

# https://learn.code.cool/krk-progbasics/#/../pages/python/modifying-objects

# Now a and b refer to two separate outer lists, but both outer lists refer to a single inner 
# list. The inner list did not get copied. This is known as a shallow copy, because the copy 
# is only one level deep.

# If you want to copy everything, you need to make a deep copy. Here is an article that 
# explains the difference:

# https://realpython.com/copying-python-objects/

print('\n-------------------------------------------- ')
# Quiz
print('\n-------------------------------------------- ')
# [optional] Value and reference semantics
# You might hear the terms value semantics and reference semantics in connection with modifying variables. Some languages, like C++, allow you to use value or reference semantics:

# "Value semantics" mean all variables store separate values. If you pass a value, you copy it.

# For example, the following program in C++ has value semantics:

# void modify_broken(vector<int> sequence) {
    # // this will only modify a copy of the vector
    # sequence[2] = 0;
# }

# vector<int> v;
# modify_broken(v);  // will NOT modify the contents of v
# "Reference semantics" mean that function arguments are just references to other variables, and you can modify the original variable.

# For example, the following program in C++ has reference semantics (note the & which marks a reference):

# void modify(int &number) {
    # // this will modify the original variable
    # number = number * 2;
# }

# int x = 10;
# modify(x);  // will set x to 20

print('\n-------------------------------------------- ')
