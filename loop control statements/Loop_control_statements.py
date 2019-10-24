# Here is a simple Python example which adds the first ten integers together:

total = 0
i = 1

while i <= 10:
    total += i
    print(total)
    i += 1

print('\n-------------------------------------------- ')
# numbers is a list of numbers -- we don't know what the numbers are!
numbers = [1, 5, 2, 12, 14, 7, 18, 30, 40, 50, 222]
total = 0
i = 0

while i < len(numbers) and total < 100:
    total += numbers[i]
    print(total)
    i += 1
