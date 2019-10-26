print('\n-------------------------------------------- 1')

ADD, SUB, MUL, DIV = range(4)


def calculator(operation=ADD, output_format=float, *args):
    if not args:
        raise ValueError("At least one number must be entered.")

    result = args[0]
    for n in args[1:]:
        if operation == ADD:
            result += n
        elif operation == SUB:
            result -= n
        elif operation == MUL:
            result *= n
        elif operation == DIV:
            result /= n
        else:
            raise ValueError("Operations must be ADD, SUB, MUL or DIV.")

    if output_format == float:
        result = float(result)
    elif output_format == int:
        result = int(result)
    else:
        raise ValueError("Format must be float or int.")

    return result


initialize_calculator = calculator(ADD, int, 3, 4)
print(initialize_calculator)

print('\n-------------------------------------------- ')
initialize_calculator = calculator(ADD, float, 2, 3.0)
print(initialize_calculator)

initialize_calculator = calculator(ADD, int, 2, 3.0)
print(initialize_calculator)

initialize_calculator = calculator(DIV, float, 2, 3.0)
print(initialize_calculator)

initialize_calculator = calculator(DIV, int, 2, 3.0)
print(initialize_calculator)

