# camel

# prompts the user for the name of a variable in camel case
# outputs the corresponding name in snake case
# Assume that the user’s input will indeed be in camel case

user = input("camelCase: ").strip()
snake_case = ""

for i, char in enumerate(user):
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char.lower()

print(snake_case)