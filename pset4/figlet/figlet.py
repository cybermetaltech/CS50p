# figlet

# Expects zero or two command-line arguments:
#   Zero if the user would like to output text in a random font.
#   Two if the user would like to output text in a specific font
#       the first of the two should be -f or --font
#       the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.

# If the user provides two command-line arguments
#   if the first is not -f or --font or the second is not the name of a font
#   the program should exit via sys.exit with an error message.

import sys
from pyfiglet import Figlet

# font names
font_names = [
        "slant",
        "rectangles",
        "alphabet",
]
# create a pyfiglet font variable
f = Figlet(font="slant")

try:
    # zero arg: render a random font
    if len(sys.argv) == 1:
        user = input("Input: ")
        f = Figlet() # the default font
        print(f.renderText(user))
    else:
        # flag to select the font: -f or --font
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            print("Invalid usage")
            sys.exit(1)
        # get the font from the font-names list
        else:
            font_name = sys.argv[2]
            if font_name not in font_names:
                print("Invalid usage")
                sys.exit(1)
            else:
                user = input("Input: ")
                f = Figlet(font=font_name)
                print(f.renderText(user))

except IndexError:
    print("Error")
    sys.exit(1)
