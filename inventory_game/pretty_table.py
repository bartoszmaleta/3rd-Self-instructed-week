d = {1: ["Python", 33.2, 'UP'],
     2: ["Java", 23.54, 'DOWN'],
     3: ["Ruby", 17.22, 'UP'],
     10: ["Lua", 10.55, 'DOWN'],
     5: ["Groovy", 9.22, 'DOWN'],
     6: ["C", 1.55, 'UP']
     }

print("{:<8} {:<15} {:<10} {:<10}".format('Pos', 'Lang', 'Percent', 'Change'))
for k, v in d.items():
    lang, perc, change = v
    print("{:<8} {:<15} {:<10} {:<10}".format(k, lang, perc, change))

inv = {
        'rope': 1, 
        'torch': 6, 
        'gold coin': 42, 
        'dagger': 1, 
        'arrow': 12
        } 

x = 10

print("{:<15} {:<15}".format('item_name', 'count'))
for keys, values in inv.items():
    count = values
#     acapits = "{:<15} {:<15}".format(keys, count)
    print("{:<15} {:<15}".format(keys, count))