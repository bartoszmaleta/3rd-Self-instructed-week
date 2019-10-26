# We can use our knowledge of loops to simplify some kinds of redundant code. 
# Consider this example, in which we prompt a user for some personal details:

# # name = input("Please enter your name: ")
# # surname = input("Please enter your surname: ")
# # # let's store these as strings for now, and convert them to numbers later
# # age = input("Please enter your age: ")
# # height = input("Please enter your height: ")
# weight = input("Please enter your weight: ")

# How can we improve on this? We can separate the parts of these lines that 
# differ from the parts that don’t, and use a loop to iterate over them. 
# Instead of storing the user input in separate variables, we are 
# going to use a dictionary – we can easily use the property names as keys, 
# and it’s a sensible way to group these values:

person = {}

for prop in ["name", "surname", "age", "height", "weight"]:
    person[prop] = input("Please enter your %s: " % prop)
