PETROL_PRICE_PER_LITRE = 5
print()

welcoming = ("*** Welcome to the fuel efficiency calculator! *** \n")
welcoming_alligned = welcoming     # should allign to the center
print(welcoming_alligned)

name_ask = ("Enter your name: ")
print(name_ask)
name = input()

distance_travelled_ask = ("Enter distance travelled in km: ")
print(distance_travelled_ask)
distance_travelled = float(input())

amount_paid_ask = ("Enter monetary value of fuel bought for the trip: ")
print(amount_paid_ask)
amount_paid = float(input())

fuel_consumed = amount_paid / PETROL_PRICE_PER_LITRE

efficiency_l_per_100_km = fuel_consumed / distance_travelled * 100
efficiency_km_per_l = distance_travelled / fuel_consumed

print("Hi, %s!" % name)
print("Your car's efficiency is %.2f litres per 100 km." % efficiency_l_per_100_km)
print("This means that you can travel %.2f km on a litre of petrol. " % efficiency_km_per_l)

print("\n Thanks foru using the program")

print()