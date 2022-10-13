#store game in function
def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    #loop that keeps the game going
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        #looks for the correct character
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            #looks for duplicate letter in the future
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        #slices the hangman using wrong
        e = wrong + 1
        print("\n".join(stages[0: e]))
        #win condition
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}".format(word))