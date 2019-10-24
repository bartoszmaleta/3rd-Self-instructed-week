print('\n-------------------------------------------- 1')

booknumber = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689",
}
print(booknumber)

print('\n-------------------------------------------- 2')
booknumber["Jane Doe"] = "+27 555 1024"
print(booknumber)

print('\n-------------------------------------------- 3')
booknumber["Anna Cooper"] = "+27 555 3237"
print(booknumber)

print('\n-------------------------------------------- 4')
print(booknumber["Bob Stone"])

print('\n-------------------------------------------- 5')
print(booknumber.get("Bob Stone", None))

print('\n-------------------------------------------- 6')
print(booknumber.keys())

print('\n-------------------------------------------- 7')
print(booknumber.values())