
print('\n-------------------------------------------- 1 mine')
total = 0
i = 1
a = 3

while total < 200:
    total += i**2
    print(total)
    i += 1

print(a**2)
print('\n-------------------------------------------- 1 answer')
# Answear:
total = 0
number = 0

while total < 200:
    number += 1
    total += number**2

print("Total: %d" % total)
print("Last number: %d" % number)

print('\n-------------------------------------------- 2 mine')
chances = 0
user_answear = 0

while user_answear != 'football' and chances < 10:
    user_answear = input('Guess the word: ')
    chances += 1
    left_chances = 10 - chances
    print('Number of your guesses: ', chances, '! You have only ', left_chances, 'left chances')

print('\n-------------------------------------------- 2 answer')
# Answear:
GUESSES_ALLOWED = 10
SECRET_WORD = "caribou"

guesses_left = GUESSES_ALLOWED
guessed_word = None

while guessed_word != SECRET_WORD and guesses_left:
    guessed_word = input("Guess a word: ")

    if guessed_word == SECRET_WORD:
        print("You guessed! Congratulations!")
    else:
        guesses_left -= 1
        print("Incorrect! You have %d guesses left." % guesses_left)