import string,random

# Variables
letters = string.ascii_lowercase
words = ['hello','world','happy','angry']

# List of Words
chosen_word = words[random.randrange(0,len(words))]

# Get every unique letter in the chosen word
letters_in_word = []
for x in chosen_word:
    if not (x in letters_in_word):
        letters_in_word.append(x)

# Display System
used_letters = []
avaiable_letters = letters_in_word
def display_letter(guess_letter):
    used_letters.append(guess_letter)
    letters_display = 'Letters used: '
    for x in used_letters:
        letters_display += f'| {x} '
        try:
            avaiable_letters.remove(x)
        except ValueError:
            pass
    return letters_display

def display_word():
    chosen_word_display = ''
    for x in chosen_word:
        if x in used_letters:
            chosen_word_display += f'{x} '
        else:
            chosen_word_display += f'_ '
    return chosen_word_display
    
def hangman_art(lives):
    if lives == 6:
        print('     |------------           ')
        print('     |           |           ')
        print('     |                       ')
        print('     |                       ')
        print('     |                       ')
        print('     |                       ')
        print('_____|____________           ')
    if lives == 5:
        print('     |------------           ')
        print('     |           |           ')
        print('     |          (_)          ')
        print('     |                       ')
        print('     |                       ')
        print('     |                       ')
        print('_____|____________           ')
    if lives == 4:
        print('     |------------           ')
        print('     |           |           ')
        print('     |          (_)          ')
        print('     |           |           ')
        print('     |                       ')
        print('     |                       ')
        print('_____|____________           ')
    if lives == 3:
        print('     |------------           ')
        print('     |           |           ')
        print('     |          (_)          ')
        print('     |       ----|           ')
        print('     |                       ')
        print('     |                       ')
        print('_____|____________           ')
    if lives == 2:
        print('     |------------           ')
        print('     |           |           ')
        print('     |          (_)          ')
        print('     |       ----|----       ')
        print('     |                       ')
        print('     |                       ')
        print('_____|____________           ')
    if lives == 1:
        print('     |------------           ')
        print('     |           |           ')
        print('     |          (_)          ')
        print('     |       ----|----       ')
        print('     |          /            ')
        print('     |         /             ')
        print('_____|____________           ')
    if lives == 0:
        print('     |------------           ')
        print('     |           |           ')
        print('     |          (_)          ')
        print('     |       ----|----       ')
        print('     |          / \          ')
        print('     |         /   \         ')
        print('_____|____________           ')

# Input System
lives = 6
while not(lives == 0):
    try:
        guess_letter = input(f'Enter a letter (lower case): ')
        if (not (guess_letter in letters)) or not(guess_letter for guess_letter in ['',' ']):
            raise ValueError
        if guess_letter in used_letters:
            print('You alrealy chosed that letter')
            continue
        if not(guess_letter in letters_in_word):
            lives -= 1
        print(display_letter(guess_letter))
        print(display_word())
        hangman_art(lives)
        if avaiable_letters == []:
            print('You Guessed the Word')
            break
        continue
    except ValueError:
        print('ValueError')
        continue

print(f'The word is {chosen_word}')