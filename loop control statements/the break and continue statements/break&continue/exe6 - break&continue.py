print('\n-------------------------------------------- 1')
number = None  

while number != 99:  
    number = int(input("Please enter your number: (99 - for exit)"))
    
    if number % 2 == 0:
        print('The integer you entered is even. Your integer: ', number)

print('\n-------------------------------------------- 2')

number2 = 0
list_of_numbers = []
sum_of_numbers = 0

while True:
    number2 = int(input("What is your number? (-number to exit)"))
    print(number2)

    if number2 < 0:
        break
    elif number >= 0:
        list_of_numbers.append(number2)
        sum_of_numbers += number2
        print('The sum right now is: ', sum_of_numbers)

        average = ('The average right now is: ', float(sum_of_numbers / len(list_of_numbers)))
        print(average)


print('Exit value of sum: ', sum_of_numbers)
print('Exit value of average: ', average)

print('\n-------------------------------------------- 3')
menu = """-- Calculator Menu --
0. Quit
1. Add two numbers
2. Subtract two numbers
3. Multiply two numbers
4. Divide two numbers"""

selection = None

while selection != 0:
    print(menu)
    selection = int(input("Select an option: "))

    if selection not in range(5):
        print("Invalid option: %d" % selection)
        continue

    if selection == 0:
        exit()  # or continue or break

    a = float(input("Please enter the first number: "))
    b = float(input("Please enter the second number: "))

    if selection == 1:
        result = a + b
    elif selection == 2:
        result = a - b
    elif selection == 3:
        result = a * b
    elif selection == 4:
        result = a / b

    print("The result is %g." % result)
