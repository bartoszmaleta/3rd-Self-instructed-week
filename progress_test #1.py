

def alphabet_filter(word):
    # Write your code here
    vowels = ['o', 'i', 'y', 'e', 'a', 'u']
    consonants = ['b, c, d, f, g, h, j, k, l, m ,n ,p, q, r, s, t, v, w, x, z']
    list_of_input = []

    string_to_split_different_size = input('What is your string?')
    string_to_split = string_to_split_different_size.lower()
    inputed_string = string_to_split[0]
    for i in string_to_split:
        list_of_input.append(i)
    
    print(list_of_input)
    if list_of_input[1] in vowels:
        print('it works')
    print(inputed_string)

    if len(string_to_split) > 0:
        for letters in vowels:
            print('vowels: ', letters)
        for letters in consonants:
            print('consonants: ', letters)
    
    # return word_consonants, word_vowels


word = 0
alphabet_filter(word)


#
# Complete the 'alphabet_filter' function below.
#
# The function is expected to return TWO STRINGS,
# the first containing consonants only, the second containing vowels only, in their original order.
# The function accepts STRING word as parameter.
#

# def alphabet_filter(word):
#     # Write your code here
#     string_to_split_different_size = input('What is your string?')
#     string_to_split = string_to_split_different_size.lower()
#     first = string_to_split[0]
#     print(first)
    
#     return word_consonants, word_vowels

# alphabet_filter()

# alphabet_filter(word)
