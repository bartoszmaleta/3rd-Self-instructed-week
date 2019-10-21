# LISTS

products = ['milk', 'cheese', 'sausages', 'cheese']

print(products)
print(type(products))
print(products[1])

products.append('water')
print(products)
count_products = products.count('cheese')

print(count_products) 

subproducts = ['meat', 'ketchup']

products.extend(subproducts)

print(products)

# ------------------------------
# TUPLES

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)

print(type(t))


# ------------------------------
# DICTIONARIES

# equipment = ['sword', 'shield', 'helmet']
# print(equipment[0])

person = {
    'age': 26,
    'firstname': 'Bartosz',
    'lastname': 'Maleta',
}

print(person)

print(type(person))

print(person['age'], end=' ')
print(person['firstname'], end=' ')
print(person['lastname'], end=' ')
print()
print()
print(person.get('height', 24))  # returns default value, it means after comma value

print(person.get('outfit', 'dont have'))
print()

keys = person.keys()       # its a list! 
print(keys)
print(type(keys))

print()

values = person.values()
print(values)
print(type(values))

print()

items = person.items()
print(items)
print(type(items))