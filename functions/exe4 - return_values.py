
def calculate_the_factorial_of_a_given_number(given_number_str):
    given_number = int(given_number_str)
    # total = 1
    # given_number = 5
    # i = 0
    if given_number <= 0:
        print("Wrong number. ")
    
    if given_number == 1:
        return 1
        # for given_number in range(1, given_number + 1):
            #  total *= given_number - i
            #  i += 1
    return given_number * calculate_the_factorial_of_a_given_number(given_number - 1)


print("The factorial of given number is: ", calculate_the_factorial_of_a_given_number(5))

