# To solve this problem, we can write a function which modifies functions. We call a function 
# like this a decorator. Our function will take a function object as a parameter, and will 
# return a new function object – we can then assign the new function value to the old 
# function’s name to replace the old function with the new function. For example, 
# here is a decorator which logs the function name and its arguments to a log file 
# whenever the function is used:


# we define a decorator
def log(original_function):
    def new_function(*args, **kwargs):
        with open("log.txt", "w") as logfile:
            logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_function.__name__, args, kwargs))

        return original_function(*args, **kwargs)

    return new_function


# here is a function to decorate
def my_function(message):
    print(message)


# and here is how we decorate it
my_function = log(my_function)


print('\n-------------------------------------------- ')
# There is a shorthand syntax for applying decorators to functions: we can use the @ symbol 
# together with the decorator name before the definition of each function that we 
# want to decorate:


@log
def my_function(message):
    print(message)

# @log before the function definition means exactly the same thing as 
# my_function = log(my_function) after the function definition.


print('\n-------------------------------------------- ')
# We can pass additional parameters to our decorator. For example, we may want to 
# specify a custom log file to use in our logging decorator:


def log(original_function, logfilename="log.txt"):
    def new_function(*args, **kwargs):
        with open(logfilename, "w") as logfile:
            logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s.\n" % (original_function.__name__, args, kwargs))

        return original_function(*args, **kwargs)

    return new_function


@log("someotherfilename.txt")
def my_function(message):
    print(message)

# Python has several built-in decorators which are commonly used to decorate class methods. 
# We will learn about them in the next chapter.

# A decorator doesn’t have to be a function – it can be any callable object!!!!
# Some people prefer to write decorators as classes!!!!!!