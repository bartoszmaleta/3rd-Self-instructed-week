# week = [""] * 7
# print(week)

# print('\n-------------------------------------------- ')
# monthtable = [week] * 4
# print(monthtable)

print('\n-------------------------------------------- 1')
monthtable = []
for m in range(12):
    month = []
    for w in range(4):
        month.append([])
        
    monthtable.append(month)

print(monthtable)

print('\n-------------------------------------------- 2')
(JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER, NOVEMBER, DECEMBER) = range(12)

(WEEK_1, WEEK_2, WEEK_3, WEEK_4) = range(4)

monthtable[JULY][WEEK_2].append("Go on holiday!")

print(monthtable)