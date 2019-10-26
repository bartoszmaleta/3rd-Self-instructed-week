print('\n-------------------------------------------- 1')
number_string = ", ".join(str(n) for n in range(1, 11))
print(number_string)

print('\n-------------------------------------------- 2')
calendar = [[[] for w in range(4)] for m in range(12)]

(JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER) = range(12)

(WEEK_1, WEEK_2, WEEK_3, WEEK_4) = range(4)

calendar[JULY][WEEK_2].append("Go on holiday!")
print(calendar)

print('\n-------------------------------------------- 3')
# calendar2 = [[] for w in range(52)]
# print(calendar2)
# (WEEK_1, WEEK_2, WEEK_3, WEEK_4) = range(52)
# calendar2[WEEK_2].append("Go on holiday!")

# does not work!!!!