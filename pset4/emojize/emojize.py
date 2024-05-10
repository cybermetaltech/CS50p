# emojize

# prompts the user for a str in English
# outputs the “emojized” version of that str

import emoji

user = input("Input: ").lower().strip()
print(emoji.emojize(user, language="alias"))
