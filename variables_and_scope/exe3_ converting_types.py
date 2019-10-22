print("--------- 1 ---------")

number1 = float("8.8")
print(number1)
print(type(number1))

print("--------- 2 ---------")
number_2_1 = round(8.8)
print(number_2_1)
print(type(number_2_1))
number_2_1_int = int(number_2_1)
print(number_2_1_int)
print(type(number_2_1_int))
# or

print("--------- 2.1. ---------")
number2 = int(8.8)
number2_rounded = round(number2)
print(number2)
print(number2_rounded)
print(type(number2_rounded))

print("--------- 3 ---------")
number3 = int(round(float("8.8")))
print(number3)
print(type(number3))

print("--------- 4 ---------")
number4 = str("8.8")
print(number4)
print(type(number4))

print("--------- 5 ---------")
number5 = str("8")
print(number5)
print(type(number5))

print("--------- 6 ---------")
number6 = float(8)
print(number6)
print(type(number6))

print("--------- 7 ---------")
number7 = bool(8)
print(number7)
print(type(number7))