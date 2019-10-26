# Sometimes there is a good reason to want to have two versions of the same 
# function with different sets of parameters. You can achieve something similar to this by 
# making some parameters optional. To make a parameter optional, we need to supply a default 
# value for it. Optional parameters must come after all the required parameters in the 
# function definition:


def make_greeting(title, name, surname, formal=True):
    if formal:
        return "Hello, %s %s!" % (title, surname)

    return "Hello, %s!" % name


print(make_greeting("Mr", "John", "Smith"))
print(make_greeting("Mr", "John", "Smith", False))

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


print(make_greeting("Mr", "John", "Smith"))
print(make_greeting("Mr", "John", "Smith", False))
print(make_greeting("Mr", "John", "Smith", False, "evening"))

print('\n-------------------------------------------- ')
# What if we want to pass in the second optional parameter, but not the first? 
# So far we have been passing positional parameters to all these functions – a tuple of 
# values which are matched up with parameters in the function signature based on their 
# positions. We can also, however, pass these values in as keyword parameters – we can 
# explicitly specify the parameter names along with the values:

print(make_greeting(title="Mr", name="John", surname="Smith"))
print(make_greeting(title="Mr", name="John", surname="Smith", formal=False, time="evening"))

print('\n-------------------------------------------- ')
# We can mix positional and keyword parameters, but the keyword parameters must come 
# after any positional parameters:

# this is OK
print(make_greeting("Mr", "John", surname="Smith"))
# this will give you an error !!!!!!!!!!!!!!!
# print(make_greeting(title="Mr", "John", "Smith"))

print('\n-------------------------------------------- ')
# We can specify keyword parameters in any order – they don’t have to match the order in the 
# function definition:

print(make_greeting(surname="Smith", name="John", title="Mr"))
# Now we can easily pass in the second optional parameter and not the first:

print(make_greeting("Mr", "John", "Smith", time="evening"))

print('\n-------------------------------------------- ')
# We should be careful when using mutable types as default parameter values in function 
# definitions if we intend to modify them in-place:


def add_pet_to_list(pet, pets=[]):
    pets.append(pet)
    return pets


list_with_cat = add_pet_to_list("cat")
list_with_dog = add_pet_to_list("dog")

print(list_with_cat)
print(list_with_dog)  # oops Not exactly what we wanted!

print('\n-------------------------------------------- ')
# Remember that although we can execute a function body many times, a function definition is 
# executed only once – that means that the empty list which is created in this function 
# definition will be the same list for all instances of the function. What we really 
# want to do in this case is to create an empty list inside the function body:


def add_pet_to_list(pet, pets=None):
    if pets is None:
        pets = []
    pets.append(pet)
    return pets


# print(pets)
# add_pet_to_list("cat")
# print(add_pet_to_list)

print_pets_list = add_pet_to_list("dog")
print(print_pets_list)