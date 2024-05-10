##### GAME #####

"""
BEGIN
Prompts the user for a level n
 -if the user does not input a positive integer: prompt again
Randomly generates an integer between 1 and n with random module
If the guess is smaller, output: Too small!
If the guess is larger, output: Too large!
If the guess is the same, output: Just right! and exit
END
"""

import random

while True:
    # prompt the user for the level and check the input
    level = input("Level: ").strip()
    
    if level.isdigit():
        level = int(level)
        
        if level >= 1:
            random_number = random.randint(1, level)
            print(random_number)
            
            # compare the input to the random_number
            while True:
                guess = input("Guess: ").strip()

                if guess.isdigit():
                    guess = int(guess)
                    
                    if guess < random_number:
                        print("Too small!")
                    elif guess > random_number:
                        print("Too large!")
                    else:
                        break  # exit the inner loop when the user guesses correctly
                else:
                    continue
            
            break  # exit the outer loop when the user enters a valid level

print("Just right!")

            
