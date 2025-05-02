# Program Title:	Mastermind

#Project Description:
#-------------------------
# This program will play the game of Mastermind with one human player and one computer player.
# The computer (codemaker) will first pick four colored “pegs” in a particular order, and then the human player (codebreaker) will try to guess the chosen colors by placing four pegs in the guessed order.
# For each guess, the computer will provide a clue about how well the human guessed. The human has 10 guesses to break the code.

# The codemaker will randomly choose four colors as hidden colors from the global list of color


# randomly choose the hidden colors
def  generateHiddenCode():
    import random
    # array of hidden sequence of code
    hiddenCode = []
    i = 0
    while i < 4:
        codeChar = random.randint(0,5)
        hiddenCode.append(codeChar)
        i += 1
    # generate the secret code using the randint function
    return hiddenCode

# function to handle the makeguess, checkguess functions
def makeGuess(hiddenCode):
    print('The secret code has been chosen. You have 10 tries to guess the code.\n')
    print('-----------------------------')
    print('Make a guess of four colors:')
    print('0 - red')
    print('1 - orange')
    print('2 - yellow')
    print('3 - green')
    print('4 - blue')
    print('5 - purple')
    print('-----------------------------') 
    guessCode = []
    # guess array to be returned and checked by the other function
    validGuesses = 1
    truth = False 
    while validGuesses <= 10 and truth == False :
# guessValid() function provides all exception handling necessary for the input
        guessCode = guessValid()
        clue = checkGuess(guessCode, hiddenCode)
        truth = cluePrinting(clue, guessCode, validGuesses, hiddenCode)
        validGuesses += 1
    return

def cluePrinting(clue, guessCode, validGuesses, hiddenCode):
    ALL_COLORS = ['red','orange','yellow','green','blue','purple']
    print('-----------------------------')
    yourGuess = []
    colorArray = []
    for i in range(len(guessCode)):
        color = guessCode[i]
        yourGuess.append(ALL_COLORS[color])
        color = hiddenCode[i]
        colorArray.append(ALL_COLORS[color])

    print('Your guess is:\n {0}\n'.format(yourGuess))

    if clue == [2,2,2,2]:
        print('Correct! You finished in {0} guesses\n'.format(validGuesses))
        return True
    elif validGuesses == 10:
        print('Your clue is: {0}\n\n'.format(clue))
        print('No more guesses, the hidden colors were:\n')
        print('{0}\n'.format(colorArray))
        return True
    else:
        # Changing this to a more readable clue format
        exact_matches = clue.count(2) # num colors in exact positions
        color_matches = clue.count(1) # num colors in wrong pos.
        print('Clues:\n')
        print('{0} exact matches (correct color in correct position)\n{1} color matches (correct color in wrong position).'.format(exact_matches,color_matches))
        print('You have {0} guesses left'.format((10-validGuesses)))
        print('-----------------------------')
        print('Make a guess of four colors:')
        print('0 - red')
        print('1 - orange')
        print('2 - yellow')
        print('3 - green')
        print('4 - blue')
        print('5 - purple')
        print('-----------------------------') 
        return False

# error checking for valid integer input 
def guessValid():
# guessCode input syntax will be:
# input: 0134        
    guessCode = []
    i = 0 
    while i < 4:
        try: 
            color = int(input('Guess color: '))
    # must be inbetween 0 and 5 (inclusive)
            if color >= 0 and color <= 5:
                guessCode.append(color)
                i += 1
            else:
                print('Invalid guess, try again:')
    # must be a number
        except TypeError:
            print('Invalid number, try again:')    
    # must be a value and not a space
        except ValueError:
            print('Invalid number, try again:')
    return guessCode

# test the guess and provide a correct clue to the user
def checkGuess(guessCode, hiddenCode):
# 2 – If the guess has a correct color in the correct position
# 1 – If the guess has a correct color, but in the wrong position
     # used to denote which spots have correctness
    checkedIndex = [-1, -1, -1, -1]
    # used to denote which guess entries have been used for comparison
    usedGuesses = [0, 0, 0, 0]

# loop for 2s
    for i in range(4):
        if guessCode[i] == hiddenCode[i]:
            # tick off that hiddencode[i] has been guessed exactly in
            usedGuesses[i] = -1      
            checkedIndex[i] = 2
    for i in range(4):
        for n in range(4):
            if guessCode[n] == hiddenCode[i] and n != i and checkedIndex[i] != 2:
                if checkedIndex[n] != 2 and usedGuesses[n] != -1:
                    usedGuesses[n] = -1
                    checkedIndex[i] = 1
                    break
                
    clue = clueReturn(checkedIndex)
    return clue

# used to create a simplified clue where you can't see the position of the clues
def clueReturn(checkedIndex):
    clue = []
    i = 3
    while i >= 0:
        if checkedIndex[i] == 1:
            clue.append(checkedIndex[i])
        if checkedIndex[i] == 2:
            clue.append(checkedIndex[i])
        i -= 1

    return clue

def playAgain():

    playAgain = input('Would you like to play again? (Y/N)')
    if playAgain == 'y' or playAgain == 'Y':
        return False
    elif playAgain =='n' or playAgain =='N':
        return True


def main(seedIn):
    truth = False
    import random
    random.seed(seedIn)
    while truth == False:
        # implements the pseudocode by calling the defined functions that are above
        # hiddenCode is array with hidden code in slots 0->3 with numbers range 0->5
        hiddenCode = generateHiddenCode()
        makeGuess(hiddenCode)
        truth = playAgain()
    print('\nThank you for playing. Good-bye!')
    return


if __name__ == "__main__":
    seed = int(input("Enter a random seed (any number): "))
    main(seed)
