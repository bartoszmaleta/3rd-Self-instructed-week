print('\n-------------------------------------------- 1')

print()
person = {}

properties = [
    ("name", str.upper),
    ("surname", str),
    ("age", int),
    ("height", float),
    ("weight", float),
]

for prop, p_type in properties:
    person[prop] = p_type(input("Please enter your %s: " % prop))

print(properties)
print(person)


print('\n-------------------------------------------- ')
