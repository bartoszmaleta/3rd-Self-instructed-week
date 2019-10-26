# By convention, the parameter name we use for the tuple is args and the name we use for the 
# dictionary is kwargs:
print('\n-------------------------------------------- ')


def make_greeting(title, name, surname, formal=True, time=None):
    if formal:
        fullname = "%s %s" % (title, surname)
    else:
        fullname = name

    if time is None:
        greeting = "Hello"
    else:
        greeting = "Good %s" % time

    return "%s, %s!" % (greeting, fullname)


def print_args(*args):
    for arg in args:
        print(arg)


def print_kwargs(**kwargs):
    for k, v in kwargs.items():
        print("%s: %s" % (k, v))


print_args("one", "two", "three")
print_args("one", "two", "three", "four")

print('\n-------------------------------------------- ')
print_kwargs(name="Jane", surname="Doe")
print_kwargs(age=10)

print('\n-------------------------------------------- ')
my_list = ["one", "two", "three"]
print_args(*my_list)

my_dict = {"name": "Jane", "surname": "Doe"}
print_kwargs(**my_dict)

print('\n-------------------------------------------- ')
my_dict = {
    "title": "Mr",
    "name": "John",
    "surname": "Smith",
    "formal": False,
    "time": "evening",
}

print(make_greeting(**my_dict))

print('\n-------------------------------------------- ')


def print_everything(name, time="morning", *args, **kwargs):
    print("Good %s, %s." % (time, name))

    for arg in args:
        print(arg)

    for k, v in kwargs.items():
        print("%s: %s" % (k, v))


print(print_everything(name="Bartosz", time="afternoon"))

print('\n-------------------------------------------- ')


def print_everything(*args, **kwargs):
    for arg in args:
        print(arg)

    for k, v in kwargs.items():
        print("%s: %s" % (k, v))


# we can write all the parameters individually
print_everything("cat", "dog", day="Tuesday")

print('\n-------------------------------------------- ')
print('\n-------------------------------------------- ')
t = ("cat", "dog")
d = {"day": "Tuesday"}

# we can unpack a tuple and a dictionary
print_everything(*t, **d)
print('\n-------------------------------------------- ')
print('\n-------------------------------------------- ')
# or just one of them
print_everything(*t, day="Tuesday")
print_everything("cat", "dog", **d)

print('\n-------------------------------------------- ')
print('\n-------------------------------------------- ')
# we can mix * and ** with explicit parameters
print_everything("Jane", *t, **d)

print('\n-------------------------------------------- ')
print_everything("Jane", *t, time="evening", **d)

print('\n-------------------------------------------- ')
print_everything(time="evening", *t, **d)

print('\n-------------------------------------------- ')
print('\n-------------------------------------------- ')
# none of these are allowed:
print_everything(*t, "Jane", **d)
print('\n-------------------------------------------- ')
print_everything(*t, **d, time="evening")