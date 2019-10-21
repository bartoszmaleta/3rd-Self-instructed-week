# convention for marking variables to indicate that their values
# are not meant to change!

NUMBER_OF_DAYS_IN_WEEK = 7
NUMBER_OF_MONTHS_IN_A_YEAR = 12

MAXIMUM_MARK = 80
tom_mark = 58

print(('Toms mark is %.2f%%' % (tom_mark / MAXIMUM_MARK * 100)))

print(('Toms mark is %.2f' % (tom_mark / MAXIMUM_MARK * 100)))

print('%.2i' % 21)
print('%.2f' % 21)
print('%.2f%%' % 21)

# --------------------------------------

LOWER, UPPER, CAPITAL = 1, 2, 3
name = 'jane'
print_style = UPPER

if print_style == LOWER:
    print(name.lower())
elif print_style == UPPER:
    print(name.upper())
elif print_style == CAPITAL:
    print(name.capitalize())
else:
    print('Unknown style option!')
