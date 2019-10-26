print('\n-------------------------------------------- 1')

ADD, SUB, MUL, DIV = range(4)


def calculator(a, b, operation=ADD, output_format=float):
    if operation == ADD:
        result = a + b
    elif operation == SUB:
        result = a - b
    elif operation == MUL:
        result = a * b
    elif operation == DIV:
        result = a / b
    else:
        raise ValueError("Operations must be ADD, SUB, MUL or DIV.")

    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = int(result)
    else:
        raise ValueError("Format must be float or int.")

    return result


initialize_calculator = calculator(3, 4, MUL, int)
print(initialize_calculator)

print('\n-------------------------------------------- ')
initialize_calculator = calculator(2, 3.0)
print(initialize_calculator)

initialize_calculator = calculator(2, 3.0, ADD, int)
print(initialize_calculator)

initialize_calculator = calculator(2, 3.0, DIV)
print(initialize_calculator)

initialize_calculator = calculator(2, 3.0, DIV, int)
print(initialize_calculator)

