# Doesnt work!!

# # first let's define weekday names
# WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
# print('\n-------------------------------------------- ')

# # day = [""] * 24
# # print(day)
# print('\n-------------------------------------------- ')
# timetable = [[""] * 24 for day in range(7)]  
# timetable[0][15] = "meeting with Jane"
# print(timetable)
# print('\n-------------------------------------------- ')


# # # now we iterate over each day in the timetable
# # for day in timetable:
#     # # and over each timeslot in each day
#     # for i, event in enumerate(day):
#         # if event:  # if the slot is not an empty string
#             # print("%s at %02d:00 -- %s" % (WEEKDAYS[0], i, event))

# for day in timetable:
#     day_name = WEEKDAYS[day]
#     for i, event in enumerate(day):
#         if event:
#             print("%s at %02d:00 -- %s" % (day_name, i, event))