 
inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}  
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def display_inventory2(inventory):
    for keys in inventory.keys():
        print(keys)
        
        for values in inventory.values():
            print(values)


display_inventory2(inv)

# for key in inv.keys():
#     inv[key] = int(inv[key])
#     # sum_of_things = 0
#     list_of_things = []
#     list_of_things.append(inv[key])
#     # sum_of_things += inv[key]
#     print(inv[key])
#     print(list_of_things)

# print(list_of_things)

# print(sum_of_things)



def sum_array(arr):
    if arr != 0:
        return(sum(arr) - min(arr) - max(arr)) 
    else:
        return None 


print(sum_array([3, 5, 7, 8, 2]))