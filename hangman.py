import string

from termcolor import colored
hangman = ['''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
      ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']


print(colored('''
                               __ 
 _ _ _     _                  |  |
| | | |___| |___ ___ _____ ___|  |
| | | | -_| |  _| . |     | -_|__|
|_____|___|_|___|___|_|_|_|___|__|                                
''', "red"))

word = ["s", "q", "u", "i", "d"]
guess = []
letters = []
c=0
d=0
while True:
    guess.clear()
    letters.clear()
    print(colored("\t\t\t\t 'Yes' to continue ", "magenta", attrs=['bold']))
    print(colored("\t\t\t\t 'No' to exit", "magenta", attrs=['bold']))
    a=input("Enter option : ")
    if a=="Yes":
        print(colored("Your word is in the category, Ocean \n _ _ _ _ _ ", "blue", attrs=['bold']))
        while True:
            b=input("\n" "Guess a letter : ")
            if b in guess:
                print(colored("You already entered that letter, try another letter", "yellow", attrs=['bold']))
                continue
            if b in word:
                d=d+1
                print(colored("Correct guess", "green", attrs=['bold']))
                guess.append(b)
                if b=="s":
                    letters.insert(0,"S")
                    print(letters)
                elif b=="q":
                    letters.insert(1,"Q")
                    print(letters)
                elif b=="u":
                    letters.insert(2,"U")
                    print(letters)
                elif b=="i":
                    letters.insert(3,"I")
                    print(letters)
                elif b=="d":
                    letters.insert(4,"D")
                    print(letters)
            if d==len(word):
                print(colored("You won! Congratulations!", "grey", attrs=['bold']))
                print(colored("The word was, Squid \n", "blue", attrs=['bold']))
                break
            if b not in word:
                c=c+1
                print(colored("Wrong guess, try again", "red", attrs=['bold']))
                print(hangman[c])
                if c==6:
                    print(colored("Sorry, you lost. Try again later!", "red"))
                    print(hangman[6])
                    break

    else:
        break




