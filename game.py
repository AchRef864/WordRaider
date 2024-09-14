import random as r

game_title = "WORD RAIDER"
words_file = open("words.txt","r")
word_bank = words_file.read().split("\n")
number_of_tries = 10
misplaced_letters = []
incorrect_letters = []
current_tries = 0
game_state = True
quit_game = "continue"
your_guess = ""

def welcome_page(t,w,n):
    print(f"Welcome to {t}.")
    print(f"the length of you word : {len(w)}.")
    print(f"you have {n} tries left.")
def word_to_guess(your_word_bank):
    return your_word_bank[r.randint(0,4)]
def check_letters(letter1,letter2):
    if letter1 == letter2:
        return True
    else:
        return False

word_to_guess=word_to_guess(word_bank)
welcome_page(game_title,word_to_guess,number_of_tries)

chose = input("Press any key to start?(always press q to quit)")

if (chose.lower() == "q") :
     print("FareWell!")
else:
    print("Welcome let's start")
    print(f"word length {len(word_to_guess)}")
    while(game_state):
        current_tries += 1
        if current_tries > number_of_tries :
            print(f"You Lost! the word is {word_to_guess}")
            game_state = False
            break
        your_guess = input(f"enter guess number {current_tries} : ")
        if your_guess.isalpha()==False:
            print("Try Again Only alphabetic characters allowed! :(")
            current_tries -= 1
        elif len(your_guess)!=5:
            print("Try Again 5 alphabetic characters only! :(")
            current_tries -= 1
        else:
            your_guess1 = list(your_guess)
            for c in range(0,len(your_guess1)) :
                if your_guess1[c] == word_to_guess[c]:
                    your_guess1[c] = word_to_guess[c]
                    if your_guess1[c] in misplaced_letters:
                        misplaced_letters.remove(your_guess1[c])
                elif your_guess1[c] in word_to_guess:
                    if your_guess1[c] not in misplaced_letters:
                        misplaced_letters.append(your_guess1[c])
                    your_guess1[c] = "_"
                else :
                    if your_guess1[c] not in incorrect_letters:
                        incorrect_letters.append(your_guess1[c])
                    your_guess1[c] = "_"
                print(f"{your_guess1[c]}", end = ' ')
                your_guess = ''.join(your_guess1)
        print(end = '\n')
        print(f"misplaced letters: {misplaced_letters}")
        print(f"incorrect letters: {incorrect_letters}")
        if your_guess == word_to_guess :
            print("You Won!!!")
            game_state = False

