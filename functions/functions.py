# Here is a definition of a simple function which takes no parameters 
# and doesn’t return any values:


def print_a_message():
    print("Hello, world!")


# To call the function we use its name followed by round brackets 
# (with any parameters that the function takes in between them):

print_a_message()

num_str = str(3)
num = int("3")

people = list()  # make a new (empty) list
people = list((1, 2, 3))  # convert a tuple to a new list

my_function = print_a_message

# later we can call the function using the variable name
my_function()

# For example, if we define several functions which all call each other, the order in which we define them doesn’t matter as long as they are all defined before we start using them:


def my_function():
    my_other_function()


def my_other_function():
    print("Hello!")


# this is fine, because my_other_function is now defined
my_function()