import operator
import csv

print()
print('\n-------------------------------------------- Step 1.0.')

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


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

print('\n-------------------------------------------- Step 2.0.')

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, added_items):
    for item in dragon_loot:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1


add_to_inventory(inv, dragon_loot)
display_inventory(inv)

print('\n-------------------------------------------- Step 3.0.')


def print_table(inventory, order=None):
    space = ' '
    vertical_line = '|'
    dash = '-'
    
    # if order is issubclass(int, str):
    #     print('asqwe')

    if order is not None:
        print('Choose correct order. You can choose between ascending and descending.')
        print("To display ascending table write: 'print_table(inv, 'count,asc')")
        print("To display descending table write: 'print_table(inv, 'count,desc')")

    if order is None:
        print('You does not enter order. You can choose between ascending and descending.')
        print("To display ascending table write: 'print_table(inv, 'count,asc')")
        print("To display descending table write: 'print_table(inv, 'count,desc')")

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
print_table(inv, 'count,desc')
print()
print('++++++++++++++++')
print('Ascending order: ')
print()
print_table(inv, 'count,asc')

print('\n-------------------------------------------- Step 4.0.')


def import_inventory(inventory, filename='import_inventory.csv'):
    with open('import_inventory.csv', encoding='utf-8') as imported_inventory:  
        csv_file_in_reader_state = csv.reader(imported_inventory)
        for data_from_file in csv_file_in_reader_state:
            list_of_inventory_from_file = data_from_file
        
        if list_of_inventory_from_file == [] or "," not in str(list_of_inventory_from_file):
            empty_list_error = ("Import file is empty or has incorrect content")
            print(empty_list_error)

    def add_to_inventory_from_csv_file(inventory, added_items):
        for item in list_of_inventory_from_file:
            if item in inv:
                inv[item] += 1
            else:
                inv[item] = 1
    
    add_to_inventory_from_csv_file(inv, list_of_inventory_from_file)
    print_table(inv, 'count,desc')


import_inventory(inv)


print('\n-------------------------------------------- Step 5.0.')
print(inv)
    

def csv_from_dict_export_preparing(dictionary, title_line):
    title_line = str(title_line[:])
    title_line = title_line.strip(" ,.  ")
    
    # \n ending check
    if "\n" not in title_line:
        title_line = title_line + "\n"
    
    # replace ", " with "," without space
    elif ", " in title_line:
        title_line = title_line.replace(", ", ",", title_line.count(", "))

    export_ready_list = [title_line]  # it's first line, which will be extended with loop, that reads all pairs in inventory dict
    export_ready_list.extend(str(key) + "," + str(dictionary[key]) + "\n" for key in dictionary)  # line format: "key,value\n"
    return export_ready_list


def export_inventory(inventory, filename):
    export_file = open(filename, "w")  
    csv_title_line = "item_name,count"
    inventory_list_export = csv_from_dict_export_preparing(inventory, csv_title_line)  # changes inventory to an exportable list
    export_file.writelines(inventory_list_export)
    export_file.close()
    file_created_or_override = 'Good job! Inventory exported to file "export_inventory.csv"! The file is in the main folder.'
    print()
    print(file_created_or_override)
    print()


exported_file_name = "export_inventory.csv"
export_inventory(inv, exported_file_name)

print('\n-------------------------------------------- Step 6.1.1')

monster_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, added_items):
    for item in monster_loot:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1


add_to_inventory(inv, monster_loot)
# print_table(inv, 'count,asc')
# print_table(inv, 'asd')
# print_table(inv)
# print_table(inv, 5)
# print_table(inv, asd)     DOESN NOT WORK


