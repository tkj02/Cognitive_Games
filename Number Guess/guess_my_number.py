from random import randint

# Introduction
print("Guess the unqiue 4-digit code I'm thinking of! You get 10 tries.\n")

# Randomly chooses a potential solution
solution = str(randint(0, 9999))

# Randomly chooses another solution if digits are not unique 
while len(solution) != len(set(solution)):
    solution = str(randint(0, 9999))

    # Prepends '0' to non-4 digit solutions
    if len(solution) != 4:
        for prepend in range(0, 4-len(solution)):
            solution = '0' + solution

# Maximum number of turns
max_turns = 10

# Current turn number
turn = 0

# Takes turn
while turn < max_turns:

    # Gets valid guess from user
    guess = int(input("Enter unique 4-digit code: "))
    
    # Prepends '0' to non-4 digit solutions
    if len(str(guess)) != 4:
        guess = str(guess)
        for prepend in range(0, 4-len(str(guess))):
            guess = '0' + guess
            
    while len(str(guess)) != len(set(str(guess))) or len(str(guess)) != 4:
        guess = str(input("Invalid. Enter new unique 4-digit code: "))

    # Variables for storing correct info
    correct_digits = 0
    correct_positions = 0

    guess = str(guess)

    # Determines number of correct digits and positions in guess
    for digit in range(len(guess)):
        if guess[digit] == solution[digit]:
            correct_positions += 1
        if guess[digit] in solution:
            correct_digits += 1

    # User wins game
    if guess == solution:
        print("Congratuations! You won!\n")
        break

    # Outputs response
    print("Number of correct digits:", correct_digits, "\nNumber of correct positions:", correct_positions, "\n")

    # Moves to next turn
    turn += 1

# User loses game
if turn == max_turns:
    print("You lost :( Better luck next time!\n The solution was:", solution)
