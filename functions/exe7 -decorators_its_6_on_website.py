print('\n-------------------------------------------- 1')


def log(original_function, logfilename="log.txt"):
    def new_function(*args, **kwargs):
        result = original_function(*args, **kwargs)

        with open(logfilename, "w") as logfile:
            logfile.write("Function '%s' called with positional arguments %s and keyword arguments %s. The result was %s.\n" % (original_function.__name__, args, kwargs, result))

        return result

    return new_function


@log
def add(x, y):
    return x + y


print(add(5.5, 10))

with open("log.txt", "r") as logfile:
    print(logfile.read())