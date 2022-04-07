
'''
Simple Wordle Program (wordle.py)

Game Explanation:
- User is allowed to guess six words at most to find the solution
- A description of each character is provided upon each guess
- Gray characters are not in the solution
- Yellow characters are in the solution but not the correct position in the 
- Green characters are in the solution and at the correct position in the solution
'''

import random

# Functions --------------------------------------------------------------------------------------------------

# guess()
# Function for getting each guess
# Input: int, representing current guess number
# Output: string, representing word that the user guessed
def guess(guess_num):

    # Original guess
    guess = input("Guess {0}: ".format(guess_num))

    # Makes guess all uppercase for future comparisons
    guess = guess.upper()

    # Checks if guess is invalid (not a five-letter word or not a valid Scrabble word)
    # While guess is invalid, keeps requesting a new guess
    while (len(guess) != 5 or guess not in words):
        guess = input("Invalid word. New guess {0}: ".format(guess_num))
        guess = guess.upper()
        
    return guess

# comparison()
# Function for comparing guess to solution
# Inputs: two strings, guess representing the user's guess and sol representing the solution
# Output: boolean, representing whether the guess matches the solution 
def comparison(guess, sol):

    # Guess matches the solution
    if guess == sol:
        return True

    # Guess does not math the solution
    else:

        # List of each character in guess and solution respectively
        guess_chars = list(guess)
        sol_chars = list(sol)

        # Copy of list of each character in solution
        # Will become a list of characters that are not green later
        sc = list(sol)

        # List representing color of each character in guess
        # -1 is gray, 0 is yellow, and 1 is green
        colored_guess = [-1, -1, -1, -1, -1]

        # Counter representing index in following for loop
        count = 4

        # Looks at each character in guess from end to start
        for i in reversed(guess_chars):

            # Current character in guess matches the character and position in the solution
            if i == sol_chars[count]:

                # Current character is green
                colored_guess[count] = 1

                # Removes the current character from copy solution list since it is green 
                del sc[count]
                
            count -= 1

        # At this point, only gray and/or yellow characters exist in sc

        # Looks at each character in guess again
        for i in range(len(guess_chars)):

            # Current character in color-representing list is gray
            if colored_guess[i] == -1:

                # Current character is in the altered copy list of the solution
                if guess_chars[i] in sc:

                    # Current character must be yellow
                    colored_guess[i] = 0

                    # Removes found character
                    sc.remove(guess_chars[i])

        # Counter used to index for following print statements
        index = 0

        # Looks at each int in color-representing list and prints respective message
        for i in colored_guess:

            # int is gray
            if i == -1:
                print(guess_chars[index], "at position", index+1, "is gray")

            # int is yellow
            elif i == 0:
                print(guess_chars[index], "at position", index+1, "is yellow")

            # int is green
            else:
                print(guess_chars[index], "at position", index+1, "is green")

            index += 1

    # Guess does not completely match solution
    return False            
            
# Source Code --------------------------------------------------------------------------------------------------

# Reads five-letter word file
file = open('filtered.txt', 'r')
words = file.read()

# Chooses random five-letter word to be solution
sol_index = random.randrange(0, 6*(8258-1), 6)
sol = words[sol_index:sol_index+5]

# Requests six guesses
for i in range(1, 7):

    # User's guess is stored in current_guess
    current_guess = guess(i)

    # Guess matches solution
    # Prints congratulatory message and breaks from loop
    if comparison(current_guess, sol) == True:
        print("\nCongratulations, you won!")
        print("Number of attemps:", str(i))
        break

    # Guess does not match solution
    else:

        # User has reached final guess and therefore lost
        if i == 6:
            print("\nYou failed :p")
            print("The word was:", sol)

    # Empty line for formatting
    print("\n")
