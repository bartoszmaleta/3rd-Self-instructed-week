import operator

print()
print('\n-------------------------------------------- Step 1')

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
# sum_of_things_in_inventory = inv['rope'] + inv['torch'] + inv['dagger'] + inv['arrow'] + inv['ruby']
# print(sum_of_things_in_inventory)


def display_total_number_of_inventory():
    list_of_values = list(inv.values())
    # print("List of numbers of inventory: ", list_of_values)
    sum_of_things = 0

    for value in list_of_values:
        sum_of_things += value

    # print(inv['gold coin'])
    print("The sum of all things: ", sum_of_things)
    sum_of_things_without_gold_coins = sum_of_things - inv['gold coin']
    print("The sum of all things without gold coins: {:d}".format(sum_of_things_without_gold_coins))
    # print("The sum of things without gold coins:", sum_of_things_without_gold_coins)
    # print(sum_of_things)


# display_total_number_of_inventory()


def display_inventory(inventory):
    for items, values in inventory.items():
        print(items, ':', values)  
    # print("Inventory: \n        Total number of items: ") 
    display_total_number_of_inventory()


print('\n-------------------------------------------- ')

display_inventory(inv) 

print('\n-------------------------------------------- Step 2')

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, added_items):
    for item in dragon_loot:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1


add_to_inventory(inv, dragon_loot)
display_inventory(inv)

print('\n-------------------------------------------- Step 3.3.')

print()
print('Descending order: ')
print()


def display_inventory_with_columns(inventory, order):
    if order == 'count,desc':
        desc_sorted_inv = order
        desc_sorted_inv = sorted(inv.items(), key=operator.itemgetter(-1))
        print("{:<15} {:<15}".format('item_name', 'count'))
        for keys, values in desc_sorted_inv:
            count = values
        #     acapits = "{:<15} {:<15}".format(keys, count)
            print("{:<15} {:<15}".format(keys, count))
        display_total_number_of_inventory()
    
    elif order == 'count,asc':
        asc_sorted_inv = order
        asc_sorted_inv = sorted(inv.items(), key=operator.itemgetter(-1), reverse=True)
        print("{:<15} {:<15}".format('item_name', 'count'))
        for keys, values in asc_sorted_inv:
            count = values
        #     acapits = "{:<15} {:<15}".format(keys, count)
            print("{:<15} {:<15}".format(keys, count))
        display_total_number_of_inventory()


desc_sorted_inv = sorted(inv.items(), key=operator.itemgetter(-1))
display_inventory_with_columns(inv, 'count,desc')

print()
print('++++++++++++++++')
print('Ascending order: ')
print()

asc_sorted_inv = sorted(inv.items(), key=operator.itemgetter(-1), reverse=True)
display_inventory_with_columns(inv, 'count,asc')

print('\n-------------------------------------------- Step 3.4.')
print()

# space = ' '
# spaces_and_vertical_line = ' | '
# dash = '-'
# longest_string_in_inv = max(len(longest_string) for longest_string in inv)
# print(longest_string_in_inv)

# number_of_dashes = longest_string_in_inv + 3 + len('count')
# print(number_of_dashes)

# dashes = dash * number_of_dashes
# print(dashes)
# print('item name | count')
# print(dashes)


def display_inventory_with_columns_testing(inventory, order):
    space = ' '
    vertical_line = '|'
    dash = '-'
    
    longest_string_in_inv = max(len(longest_string) for longest_string in inv)  # =9

    number_of_dashes = longest_string_in_inv + 3 + len('count')
    dashes = dash * number_of_dashes  # =17

    if order == 'count,desc':
        desc_sorted_inv = order
        desc_sorted_inv = sorted(inv.items(), key=operator.itemgetter(-1), reverse=True)
        print(dashes)
        print("{:<10} {:<15}".format('item_name |', 'count'))
        print(dashes)
        for keys, values in desc_sorted_inv:
            # count = values
            
            number_of_whitespaces_before_item_name = longest_string_in_inv - len(keys)
            whitespaces_before_item_name = ' ' * number_of_whitespaces_before_item_name
            keys_with_spaces_and_line = whitespaces_before_item_name + keys + space + vertical_line
            
            values_str = str(values)
            length_of_count = len('count')
            number_of_whitespaces_before_count = length_of_count - len(values_str)
            whitespaces_before_count = ' ' * number_of_whitespaces_before_count
            count_with_spaces = whitespaces_before_count + values_str

            print("{:<0} {:<15}".format(keys_with_spaces_and_line, count_with_spaces))
        
        print(dashes)
        print()
        display_total_number_of_inventory()
    
    elif order == 'count,asc':
        asc_sorted_inv = order
        asc_sorted_inv = sorted(inv.items(), key=operator.itemgetter(-1))
        print(dashes)
        print("{:<10} {:<15}".format('item_name |', 'count'))
        print(dashes)
        for keys, values in asc_sorted_inv:
            # count = values
            
            number_of_whitespaces_before_item_name = longest_string_in_inv - len(keys)
            whitespaces_before_item_name = ' ' * number_of_whitespaces_before_item_name
            keys_with_spaces_and_line = whitespaces_before_item_name + keys + space + vertical_line
            
            values_str = str(values)
            length_of_count = len('count')
            number_of_whitespaces_before_count = length_of_count - len(values_str)
            whitespaces_before_count = ' ' * number_of_whitespaces_before_count
            count_with_spaces = whitespaces_before_count + values_str

            print("{:<0} {:<15}".format(keys_with_spaces_and_line, count_with_spaces))
        
        print(dashes)
        print()
        display_total_number_of_inventory()        


print()
print('Descending order: ')
print()
display_inventory_with_columns_testing(inv, 'count,desc')
print()
print('++++++++++++++++')
print('Ascending order: ')
print()
display_inventory_with_columns_testing(inv, 'count,asc')

