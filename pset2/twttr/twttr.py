# twttr

# prompts the user for a str of text
# outputs that same text but with all vowels (A, E, I, O, and U) omitted
# whether inputted in uppercase or lowercase


user = input("Input: ")
vowels = "aeiouAEIOU"

# Create a copy of the user's input
output = user

# Loop through the vowels
for vowel in vowels:
    # Replace each vowel in the output with an empty string
    output = output.replace(vowel, '')

print(f"Output: {output}")