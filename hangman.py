import random


def pick_random_word(difficulty):
    """
    Picks a random word from a text file
    creates an array of dashes equal to the length of the word
    Creates an array of singular letters of the word
    Determines the number of guesses allowed depending on the length of word picked
    """

    split_word = []
    dash_array = []

    with open('words.txt') as f:
        words = f.read().splitlines()
        word_choice = random.choice(words)
    word = word_choice.upper()

    for character in word:
        split_word.append(character)
        dash_array.append('_')

    if len(word) <= 5:
        if difficulty == 1:
            guesses_allowed = 9
        elif difficulty == 2:
            guesses_allowed = 7
        elif difficulty == 3:
            guesses_allowed = 5
    else:
        if difficulty == 1:
            guesses_allowed = round(1.8 * len(word))
        elif difficulty == 2:
            guesses_allowed = round(1.4 * len(word))
        elif difficulty == 3:
            guesses_allowed = len(word)

    return word, split_word, dash_array, guesses_allowed


def printing_line(split_word, dash_array, letter):
    """
    Replaces dash with letter if guessed correctly
    And handles duplicates
    """
    for i in range(0, len(split_word)):
        if split_word[i] == letter:
            dash_array[i] = letter

    print(' '.join(dash_array))


def input_letter(dash_array, guesses_allowed, split_word):
    """
    Asks user for letter
    Checks game status after each letter is submitted
    Ends game if win/lose
    """
    used_letters = []

    while True:

        if ' '.join(dash_array).find('_') == -1:
            print('\n===== YOU WIN =====\n')
            break

        if guesses_allowed <= 0:
            print("\n===== Game over =====\n")
            break

        letter = input("\nGuess a letter: ")

        if letter == 'quit':
            break

        if letter.upper() in used_letters:
            print('Letter already used, try again.')
            print(' '.join(dash_array))
            continue

        if len(letter) != 1:
            print("\nInvalid input, please try again")
            print(' '.join(dash_array))
            continue

        used_letters.append(letter.upper())
        print('used letters:', ' '.join(used_letters))

        try:
            index_of_letter = split_word.index(letter.upper())
            printing_line(split_word, dash_array, letter.upper())
            print('\nGuesses left: ', guesses_allowed)
            continue
        except:
            guesses_allowed -= 1
            print(' '.join(dash_array))
            print('\nGuesses left: ', guesses_allowed)
            continue
    pass


def game():
    """
    Starts game
    """
    print('\n===== WELCOME TO HANGMAN =====\n')
    print('\n')
    print('Select a difficulty: ')
    print('1. Easy\n2. Medium\n3. Hard\n')

    while True:
        selection = input("1, 2 or 3: ")
        if selection == '1':
            word, split_word, dash_array, guesses_allowed = pick_random_word(1)
            break
        elif selection == '2':
            word, split_word, dash_array, guesses_allowed = pick_random_word(2)
            break
        elif selection == '3':
            word, split_word, dash_array, guesses_allowed = pick_random_word(3)
            break
        else:
            print("Invalid input, try again")
            continue

    print(' '.join(dash_array))
    print("Allowed number of incorrect guesses: ", guesses_allowed)
    print("Type 'quit' to give up.")
    input_letter(dash_array, guesses_allowed, split_word)

    return f"The word was {word}"


while True:
    print(game())

    again = input(
        "Would you like to play again (Y for yes, anything else for no)? ")

    if again.upper() == 'Y':
        continue
    else:
        break

print("Thanks for playing!!!")
