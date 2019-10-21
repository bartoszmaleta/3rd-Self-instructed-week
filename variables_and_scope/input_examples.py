# First option -------------
# height = int(input('Enter height of rectangle: '))
# width = int(input('Enter width of rectangle: '))

# print('The area of the rectangle is %d' % (width * height))


# ------------------------------------------------
# Second option ------------- does not work properly! 
# try:
#     height = int(input('Enter height of rectangle: '))
#     width = int(input('Enter width of rectangle: '))
# except ValueError as e:  # if a value error occurs, we will skip to this point
#     print("Error reading height and width: %s" % e)

# print('The area of the rectangle is %d' % (width * height))


# ------------------------------------------------
# Third option ------------- does not work properly! 

correct_input = False 

while not correct_input:
    try:
        height = int(input("Enter height of rectangle: "))
        width = int(input("Enter width of rectangle: "))
    except ValueError:
        print("Please enter valid integers for the height and width.")
    else:  # this will be executed if there is no value error
        correct_input = True

print('The area of the rectangle is %d' % (width * height))