print('\n-------------------------------------------- 1')
months = ('JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER')

days_in_months = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

print(len(months))
print(len(days_in_months))

month_days_dict = {}

for month, days in zip(months, days_in_months):
    month_days_dict[month] = days

print(month_days_dict)

print('\n-------------------------------------------- 2')

month_days_dict_without_loop = dict(zip(months, days_in_months))
print(month_days_dict_without_loop)
