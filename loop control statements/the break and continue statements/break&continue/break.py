print('\n-------------------------------------------- break')
x = 1

while x <= 10:
    print(x)
    x += 1
    
    if x == 5:
        break

print('\n-------------------------------------------- ')
for x in range(1, 10 + 1):  # this will count from 1 to 10
    print(x)

    if x == 5:
        continue

print('\n-------------------------------------------- ')
# Note that if we replaced break with continue in the first example, 
# we would get an infinite loop – because the continue statement 
# would be triggered before x could be updated. x would stay equal to 5, 
# and keep triggering the continue statement, for ever!

# First example with continue:
# x = 1

# while x <= 10:
    # if x == 5:
        # continue

    # print(x)
    # x += 1


print('\n-------------------------------------------- ')
valid_number = 10
age = int(input("Please enter your age: "))
# while age != valid_number:  # let's assume that we've defined valid_number elsewhere
# same as:
while not age == valid_number:  # let's assume that we've defined valid_number elsewhere
    age = int(input("Please enter your age: "))

print('\n-------------------------------------------- ')
valid_number3 = 12

while True:
    age3 = int(input("Please enter your age: "))
    if valid_number3 == age3:
        break

print('\n-------------------------------------------- ')
valid_number2 = 11
age2 = None  # we can initialise age to something which is not a valid number
while age2 != valid_number2:  # now we can use the condition before asking the user anything
    age2 = int(input("Please enter your age: "))


