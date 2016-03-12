HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMANPICS[len(missed_letters)])
    print()
    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()
    blanks = '_' * len(secret_word)
    for i in range(len(secret_word)):  # replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
    for letter in blanks:  # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()
