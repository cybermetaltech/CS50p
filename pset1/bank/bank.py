# bank

# implement a program that prompts the user for a greeting
# If the greeting starts with “hello”, output $0
# If the greeting starts with an “h” (but not “hello”), output $20
# Otherwise, output $100

greetings = input("Greetings: ")
greetings = greetings.lower().strip()

if "hello" in greetings:
    print("$0")
elif greetings[0] == "h":
    print("$20")
else:
    print("$100")