import random
import os

wins = 0
losses = 0

hangman_drawings = [r"""
                    +----+
                    |    |
                    |    | 
                    |    O
                    |   
                    |    
                    |   /|\
                    |   / \
                    |_______""",
                    r"""
                    +----+
                    |    |
                    |    | 
                    |    O
                    |   /|\
                    |   / \
                    |
                    |
                    |_______""",
                    r"""
                    +----+
                    |    |
                    |    | 
                    |    O
                    |   /|\
                    |   / 
                    |
                    |
                    |_______""",
                    r"""
                    +----+
                    |    |
                    |    | 
                    |    O
                    |   /|\
                    |   
                    |
                    |
                    |_______""",
                    r"""
                    +----+
                    |    |
                    |    | 
                    |    O
                    |   /|
                    |   
                    |
                    |
                    |_______""",
                    r"""
                    +----+
                    |    |
                    |    | 
                    |    O
                    |    |
                    |   
                    |
                    |
                    |_______""",
                    r"""
                    +----+
                    |    |
                    |    | 
                    |    O
                    |    
                    |   
                    |
                    |
                    |_______""",
                    r"""
                    +----+
                    |    |
                    |    | 
                    |    
                    |    
                    |   
                    |
                    |
                    |_______""",
                    r"""
                    +----+
                    |    
                    |    
                    |    
                    |    
                    |   
                    |
                    |
                    |_______""",
                    r"""
                    
                    |
                    |
                    |
                    |
                    |
                    |
                    |
                    |_______""",
                    r"""
                    
                    
                    
                    
                    
                    
                    
                    
                     _______""",]

if os.path.exists("hangman_high_score.txt"):
    with open("hangman_high_score.txt") as f:
        high_score = int(f.read())
        score = 0
else:
    f = open("hangman_high_score.txt", "a")
    with open("hangman_high_score.txt", "w") as f:
        f.write("0")
        high_score = 0
        score = 0


def pick_random_word(difficulty):
    """
    Picks a random word from a text file.
    creates an array of dashes equal to the length of the word.
    Creates an array of singular letters of the word.
    Determines the number of guesses allowed depending on the length of word picked.
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
    And handles duplicates.
    """
    for i in range(0, len(split_word)):
        if split_word[i] == letter:
            dash_array[i] = letter

    print(' '.join(dash_array))


def hangman_prints(guesses_allowed):
    """
    Prints hangman for every guess done.
    Note that it will not print anything if the number of guesses allowed is greater than 11.
    This is due to the limited number of hangman drawings.
    """
    if guesses_allowed > 10:
        print(hangman_drawings[10])
    else:
        print(hangman_drawings[guesses_allowed])

    pass


def input_letter(dash_array, guesses_allowed, split_word):
    """
    Asks user for letter.
    Checks game status after each letter is submitted.
    Ends game if win/lose.
    """
    used_letters = []
    end_status = 0

    while True:

        if ' '.join(dash_array).find('_') == -1:
            print('\n===== YOU WIN =====\n')
            end_status = 1
            break

        if guesses_allowed <= 0:
            print("\n===== Game over =====\n")
            end_status = 2
            break

        letter = input("\nGuess a letter: ")

        if letter == 'quit':
            end_status = 2
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
            hangman_prints(guesses_allowed)
            printing_line(split_word, dash_array, letter.upper())
            print('\nGuesses left: ', guesses_allowed)
            continue
        except:
            guesses_allowed -= 1
            hangman_prints(guesses_allowed)
            print(' '.join(dash_array))
            print('\nGuesses left: ', guesses_allowed)
            continue

    guesses_left = guesses_allowed

    return end_status, guesses_left


def game():
    """
    Starts game and sets difficulty.
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

    print("Previous high score: ", high_score)
    print("Current total score: ", score)
    print(' '.join(dash_array))
    print("Allowed number of incorrect guesses: ", guesses_allowed)
    print("Type 'quit' to give up.")
    end_status, guesses_left = input_letter(
        dash_array, guesses_allowed, split_word)
    end_string = f"The word was {word}"

    return end_string, end_status, guesses_left


if __name__ in "__main__":

    while True:
        end_string, end_status, guesses_left = game()
        print(end_string)

        if end_status == 1:
            wins += 1
            score += guesses_left
        elif end_status == 2:
            losses += 1
        print(f"Wins: {wins} | Losses: {losses}")
        print("Total score: ", score)

        again = input(
            "Would you like to play again (Y for yes, anything else for no)? ")

        if again.upper() == 'Y':
            continue
        else:
            if score > high_score:
                with open("hangman_high_score.txt", "w") as f:
                    f.write(str(score))
            f.close()
            break

    print("Thanks for playing!!!")
