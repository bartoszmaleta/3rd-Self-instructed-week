print('\n-------------------------------------------- 1 mine')

number = 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for i in range(0, len(numbers)):
    total += numbers[i]
    print(total)

print('\n-------------------------------------------- 1 answer')
    
total = 0

for i in range(1, 10 + 1):
    total += i

print(total)

print('\n-------------------------------------------- 2')
# Remember that we can use the sum function to sum a sequence:

print(sum(range(1, 10 + 1)))

print('\n-------------------------------------------- 3')
# given_number = int(input('What is the number? '))
given_number = 5    # just to make it easier to use! above line is also good!
# 5 factorial is 5! = 5 x 4 x 3 x 2 x 1 = 120
# does not work!!!
i = 0

for given_number in range(1, given_number + 1):
    total *= given_number - i
    i += 1

print(total)

print('\n-------------------------------------------- 4')
total_sum = 0
total_product = 1
total_average = 0

for i in range(1, 11):
    input_number = float(input('What is your number? '))
    total_sum += input_number
    total_product *= input_number

print("Total sum is: ", total_sum)
print("Total product is: ", total_product)
total_average = total_sum / 10
print("Total average is: ", total_average)

print('\n-------------------------------------------- 5')
total_sum = 0
total_product = 1
total_average = 0
numbers = []

for i in range(1, 11):
    input_number = float(input('What is your number? '))
    numbers.append(input_number)
print(numbers)

for num in numbers: 
    total_sum += num
    total_product *= num

print("Total sum is: ", total_sum)
print("Total product is: ", total_product)
total_average = total_sum / 10
print("Total average is: ", total_average)