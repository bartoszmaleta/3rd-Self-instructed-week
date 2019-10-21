print()

welcoming = ("*** Welcome to the temperature converter! *** \n")
welcoming_alligned = welcoming     # should allign to the center
print(welcoming_alligned)

name_ask = ("Enter your name: ")
print(name_ask)
name = input()

temp_in_fahrenheit_ask = ("Enter the temperature in Fahrenheit: ")
print(temp_in_fahrenheit_ask)
temp_in_fahrenheit = float(input())
# temp_in_fahrenheit = int(temp_in_fahrenheit)

temp_in_celsius = (5/9) * (temp_in_fahrenheit - 32)

print()
print("---------------------------------------")
print("Hi, %s!" % name)
print("The temperature in Fahrenheit is: %.2f !" % temp_in_fahrenheit)
print("And the temperature in Celsius is: %.2f !" % temp_in_celsius)

print("%g = %g" % (temp_in_fahrenheit, temp_in_celsius))
print()
print(temp_in_celsius)