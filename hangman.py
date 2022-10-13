'''
Author: Zoha Qamar
3/19/21

Description: This program takes letters until a word is guessed or no chances are left.
'''
import random


# functions
def load_words(WORDLIST_FILENAME):
    """load_words. This function populates and returns a list of words, given the filename of the wordlist."""
    wordlist = list()
    # 'with' can automate finish 'open' and 'close' file
    with open(WORDLIST_FILENAME) as f:
         # fetch one line each time, include '\n'
        for line in f:
             # strip '\n', then append it to wordlist
            wordlist.append(line.rstrip('\n'))
    return wordlist

def get_letter() -> str:
    """
    Prompts user to enter a value until the user enters a letter
    Returns: alphabetic string of length one
    """
    letter = input("\nYour guess (letters only): ")

    while len(letter) > 1 or not letter.isalpha():
        print("Not a valid character. Please enter a letter.\n")
        letter = input("Your guess (letters only): ")
    return letter
    

# variables

wordlist = load_words('words.txt')  # create list of possible words
word = wordlist[random.randint(0, len(wordlist) - 1)]  # pick random word
chances = 10
missed = ""
display = ""
guess = ""

for i in word:
    if i.isalpha():
        display += "_ "
    elif i == "'" or i == "-" or i == " ":
        display += i + " "


# print game instructions and information

print("Hangman: Word guessing game\n\nHow to play: Guess the word by inputting one letter in every turn until you run out of chances or get the word right.\n")
print("Chances Remaining: " + str(chances))
print("Missed Letters/Digits: None")
print(display)


# loop until game is over

while chances > 0 and "_" in display:

    guess = get_letter().lower()

    if guess in display.lower() or guess in missed.lower():
        print("You have already tried this letter. Guess again!")
        guess = get_letter().lower()

    
    if guess not in word.lower():
        missed += guess
        print("This character is not present in the word.")
        chances -= 1
    
    else:
        index = []  # list of indexes where the guessed letter is in the word
        i = 0
        for letter in word.lower():
            if letter == guess:
                index.append(i)
            i += 1
                
        # update the display by adding the guessed letter in
        for i in range(len(index)):
            display = display[:index[i] * 2] + word[index[i]] + display[(index[i] * 2) + 1:]

    # print updated values
    print("Chances Remaining: " + str(chances))
    
    if missed == "":
        print("Missed Letters: None")
    else:
        print("Missed Letters: " + missed)
        
    print(display)


# output message when game is over

if "_" not in display:
    print("\nCongrats! You have guessed the word correctly and have won the game!")
else:
    print("\nYou have lost. The correct word was: " + word)

