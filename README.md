# Hangman Game

This is a simple console-based Hangman game implemented in Python. The game randomly selects a word from a predefined list and challenges the player to guess it one letter at a time.

## How to Play

1. Run the `hangman.py` file in a Python environment.
2. The game will randomly select a word from its dictionary and display a series of dashes representing the letters in the word.
3. Guess a letter by typing it and pressing Enter.
4. If the letter is in the word, it will be revealed in the corresponding position(s). If not, you will lose one attempt.
5. Keep guessing until you either complete the word or run out of attempts.

## Files

- `hangman.py`: The main Python script for running the game.
- `words.py`: Contains a list of words that the game can select from.

## Dependencies

This project uses standard Python libraries and does not require any additional dependencies.

## How to Customize the Word List

If you want to add or remove words from the game, you can edit the `words.py` file. Simply modify the list of words to your liking.

```python
word_list = [
    "python",
    "hangman",
    "programming",
    # Add or remove words as needed
]
