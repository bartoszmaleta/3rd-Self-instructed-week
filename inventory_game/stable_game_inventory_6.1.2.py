import operator
import csv

print()
print('\n-------------------------------------------- ')
print('\n-------------------------------------------- Step 1.0.')
step1 = 'Step 1. \nWrite a function named display_inventory(inventory) that would take any possible “inventory” and display it \n'
print(step1)

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


display_inventory(inv) 
print('\n-------------------------------------------- ')
print('\n-------------------------------------------- Step 2.0.')
step2_1 = 'Step 2. \nWrite a function named add_to_inventory(inventory, added_items) , where the inventory '
step2_2 = 'parameter is a dictionary representing the player’s inventory and the added_items parameter is a list like dragon_loot. '
step2_3 = 'The add_to_inventory() function should return a dictionary that represents the updated inventory. \n'
print(step2_1)
print(step2_2)
print(step2_3)

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, added_items):
    for item in dragon_loot:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1


add_to_inventory(inv, dragon_loot)
display_inventory(inv)
print('\n-------------------------------------------- ')
print('\n-------------------------------------------- Step 3.0.')
step2_1 = 'Step 3. \nWrite a function named print_table(inventory, order) that takes your inventory and  '
step2_2 = 'displays it in a well-organized table with each column right-justified. '
step2_3 = 'The input argument is an order parameter (string), which works as the following: '
step2_4 = ' - empty (by default) means the table is unordered'
step2_5 = ' - "count,desc" means the table is ordered by count (of items in the inventory) in descending order'
step2_6 = ' - "count,asc" means the table is ordered by count in ascending order \n'
print(step2_1)
print(step2_2)
print(step2_3)
print(step2_4)
print(step2_5)
print(step2_6)


def print_table(inventory, order=None):
    space = ' '
    vertical_line = '|'
    dash = '-'
    longest_string_in_inv = max(len(longest_string) for longest_string in inv)  # =9

    number_of_dashes = longest_string_in_inv + 3 + len('count')
    dashes = dash * number_of_dashes  # =17
    
    # if order is issubclass(int, str):
    #     print('asqwe')

    if order is not None:
        print('Choose order. You can choose between ascending and descending.')
        print("To display ascending table write: 'print_table(inv, 'count,asc')")
        print("To display descending table write: 'print_table(inv, 'count,desc')")
        print('\n Your inventory: \n')

    if order is None:
        print('You does not enter order. You can choose between ascending and descending.')
        print("To display ascending table write: 'print_table(inv, 'count,asc')")
        print("To display descending table write: 'print_table(inv, 'count,desc')")
        print('Right now the table will be printed without order!')
        # inv = order
        # asc_sorted_inv = sorted(inv.items(), key=operator.itemgetter(-1))
        print(dashes)
        print("{:<10} {:<15}".format('item_name |', 'count'))
        print(dashes)
        for keys, values in inv.items():
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
print('++++++++++++++++')
print('No order: ')
print()
print_table(inv)
print()
print('++++++++++++++++')
print()
print('Descending order: ')
print()
print_table(inv, 'count,desc')
print()
print('++++++++++++++++')
print('Ascending order: ')
print()
print_table(inv, 'count,asc')

print('\n-------------------------------------------- ')
print('\n-------------------------------------------- Step 4.0.')
step2_1 = 'Step 4. \nWrite a function named import_inventory(inventory, filename) which can import new inventory items  '
step2_2 = 'from a file - the filename comes as an argument, but by default it is import_inventory.csv. The import '
step2_3 = 'automatically merges items by name. The file format is plain text with comma separated values (CSV).  '
step2_4 = 'Example file content:'
step2_5 = 'ruby,rope,ruby,gold coin,ruby,axe \n'
print(step2_1)
print(step2_2)
print(step2_3)
print(step2_4)


def import_inventory(inventory, filename='/home/acer/Documents/3rd-Self-instructed-week/3rd-Self-instructed-week/import_inventory.csv'):
    with open('/home/acer/Documents/3rd-Self-instructed-week/3rd-Self-instructed-week/import_inventory.csv', encoding='utf-8') as imported_inventory:  
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


print('\n-------------------------------------------- ')
print('\n-------------------------------------------- Step 5.0.')
step2_1 = 'Step 5. \nWrite a function named export_inventory(inventory, filename) which can export all inventory items to a file.   '
step2_2 = 'The filename comes as an argument - if not, it automatically creates (and overwrites) the file '
step2_3 = 'called export_inventory.csv. The file format is the same plain text with comma separated values (CSV). \n'
print(step2_1)
print(step2_2)
print(step2_3)

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

print('\n-------------------------------------------- ')
print('\n-------------------------------------------- Step 6.1.1')
step2_1 = 'Step 6. \nEnsure your functions are working with specially named items,  '
step2_2 = 'which have a unicode character or accent in their name or other special characters (especially space, tab). \n'
print(step2_1)
print(step2_2)


monster_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, added_items):
    for item in monster_loot:
        if item in inv:
            inv[item] += 1
        else:
            inv[item] = 1


add_to_inventory(inv, monster_loot)
print_table(inv, 'count,asc')
# print_table(inv, 'asd')
# print_table(inv)
# print_table(inv, 5)
# print_table(inv, asd)     DOESN NOT WORK

print('\n-------------------------------------------- ')
print('\n-------------------------------------------- Step 6.1.2')
step2_1 = 'Step 6.1.2. \n Deleting loot'
print(step2_1)

# same as dragon_loot but with 'axe' at the end
deleting_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'axe']


def deleting_items_from_inventory_by_deleting_loot(inventory, deleted_items):
    def if_0_of_loot_deletes_item():
        if inv[item] <= 0:
            del inv[item]

    for item in deleting_loot:
        if item in inv:
            inv[item] -= 1
            if_0_of_loot_deletes_item()
        else:           
            inv[item] = 1


deleting_items_from_inventory_by_deleting_loot(inv, deleting_loot)
print_table(inv, 'count,asc')
