 ##### PROFESSOR ######

"""
-Prompts the user for a level, n.
    -If the user does not input 1, 2, or 3, the program should prompt again.
-Randomly generates ten (10) math problems formatted as X + Y = ,
wherein each of X and Y is a non-negative integer with digits.
-No need to support operations other than addition (+).
-Prompts the user to solve each of those problems.
    -If an answer is not correct (or not even a number)
        -the program should output EEE and prompt the user again,
    If the user has still not answered correctly after three tries
        -the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
"""


import random

def main():
    level = get_level()
    score_value = 0

    for _ in range(10):
        x, y = generate_integer(level)
        score_value += score_equation(x, y)

    print(f"Score: {score_value}")

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999), random.randint(100, 999)
    else:
        raise ValueError("Invalid level. Choose 1, 2, or 3.")

def score_equation(x, y):
    score_value = 0
    correct_answer = False
    attempt = 0

    while True:
        # Display the math problem and wait for input
        user_input = input(f"{x} + {y} = ")

        # Check if the answer is correct
        if user_input.isdigit() and int(user_input) == x + y:
            # The answer is correct, break out of the inner loop
            if attempt == 0:
                score_value += 1
            correct_answer = True
            break
        else:
            # The answer is incorrect, print the error message
            attempt += 1
            print("EEE")

            if attempt == 3:
                print(f"{x} + {y} = {x + y}")
                break

    return score_value

if __name__ == "__main__":
    main()
