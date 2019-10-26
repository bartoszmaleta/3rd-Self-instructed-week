# Here is an example of a for loop in Java:

# for (int count = 1; count <= 8; count++) {
#     System.out.println(count);
# }

# In Python, for loops make this use case simple and 
# easy by allowing you to iterate over sequences directly. 
# Here is an example of a for statement which counts from 1 to 8:

for i in range(1, 9):
    print(i)

pets = ["cat", "dog", "budgie"]

for pet in pets:
    print(pet)

print('\n-------------------------------------------- Same thing:')
for i in range(len(pets)):  # i will iterate over 0, 1 and 2
    pet = pets[i]
    print(pet)    

print('\n-------------------------------------------- ')
for i, pet in enumerate(pets):
    pets[i] = pet.upper()  # rewrite the list in all caps
    print(pets[i])

print('\n-------------------------------------------- ')
numbers = [1, 2, 2, 3]

for i, num in enumerate(numbers):
    if num == 2:
        del numbers[i]

print(numbers)  # oops -- we missed one, because we shifted the elements around while we were 