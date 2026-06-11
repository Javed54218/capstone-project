# capstone-project

===== WELCOME TO HANGMAN =====

This project recreates the classic game of hangman in a terminal

How to run:
Run the following command in the terminal
 
    python3 hangman.py
Make sure words.txt is in the same directory as hangman.py

Project gameplay:
The terminal will then prompt with a selection of difficulty, which will determine how many guesses the user is allowed:
1 = easy
2 = medium
3 = hard

A word is selected randomly from a list in words.txt

The user must then input letters, which will repeat until the number of guesses allowed reaches zero or the user gets the correct answer.

The terminal will then ask the user of they want to play again by typing 'y' or 'Y'