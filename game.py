from graphics import display_board
import random
import urllib.request

def main():
    missed_letters = set()
    correct_letters = set()

    secret_word = get_word_from_url('http://randomword.setgetgo.com/get.php')

    #secret_word = get_random_word('words.txt')

    game_is_done = False

    while game_is_done == False:
        #print(secret_word)
        if check_gamestate(correct_letters, missed_letters, secret_word, game_is_done) == True:
            if replay() == True:
                game_is_done = False
                main()
            else:
.lower()
        display_board(missed_letters, correct_letters, secret_word)
        next_input = str(input("What is your next guess?   >")).lower()

        if next_input in missed_letters or next_input in correct_letters:
            print("You've Already Guessed That Letter... \n")
        else:
            if check_letter(next_input, secret_word) == True:
                correct_letters.update(next_input[0])
            else:
                missed_letters.update(next_input[0])

def replay():
    response = str(input("\n\n...Play Again???... y/n    > ")).lower()
    try:
        if response == 'y':
            return False
        else:
            return True
    except:
        print("I don't understand that input...")

def check_letter(letter, word):
    if letter in word:
        print("CORRECT!!!")
        print("\n")
        return True
    else:
        print("NOPE.")
        print("\n")
        return False

def check_gamestate(correct, misses, word, current_gamestate):
    if set(correct) == set(word):
        print("YAY! YOU WIN!!!!!!!!!!!")
        return True

    elif len(misses) >= len('hangman'):
        print("YOU LOSE\n"*20)

def get_word_from_url(url):
    f = urllib.request.urlopen(url)
    return(str(f.read().decode('utf-8')).lower())

def get_random_word(a_file):
    the_word = ''
    seed = random.randint(0, get_file_length(a_file))
    the_word = get_line(a_file, seed)
    return the_word

def get_line(a_file, line_pos):
    words = []
    with open(a_file, 'r') as f:
        for line in f:
            words.append(line)
        word = words[line_pos]
    return word

def get_file_length(a_file):
    with open(a_file, 'r') as f:
        num_lines = 0
        for line in f:
            num_lines += 1
    return num_lines


main()

##get_random_word print output
#print(get_file_length('words.txt'))
#print(random.randint(0, get_file_length('words.txt')))
#print(get_random_word('words.txt'))
