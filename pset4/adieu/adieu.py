# adieu

# prompts the user for names, one per line, 
# until the user inputs control-d
# Assume that the user will input at least one name
# Output adieu to the names
# -separating two names with one and
# -three names with two commas and one and

#!/usr/bin/env python3

import inflect

p = inflect.engine()
names = []

while True:
    try:
        name = input("Name: ").strip().title()
        names.append(name)

    except EOFError:
        # end the program with ctrl+d
        print()
        break

names_list = p.join(names)
adieu = "Adieu, adieu, to "

# output the result
print(adieu + names_list)
