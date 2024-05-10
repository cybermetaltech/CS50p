# deep

# prompts the user for the answer to the Great Question of Life, the Universe and Everything
# output Yes if user input is 42 or (case-insensitively) forty-two or forty two
# Otherwise output No.

answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
answer = answer.lower().strip()

if answer == "42" or answer == "forty-two" or answer == "forty two":
    print("Yes")
else:
    print("No")