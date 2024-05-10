# plates

# prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not.
#    “All vanity plates must start with at least two letters.”
#    “vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
#    “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
#    “No periods, spaces, or punctuation marks are allowed.”

# assume that any letters in the user’s input will be uppercase
# is_valid returns True if s meets all requirements and False if it does not

# last case not checked: CS50P2

def main():
    plate = input("Plate: ").upper().strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Max <= 6 chars, min >= 2 chars
    if len(s) < 2 or len(s) > 6:
        return False

    # Check for the first two characters
    if s[0].isalpha() and s[1].isalpha():
        has_previous_number = False
        for i in s[2:]:
            if not i.isalnum() or (i == '0' and not has_previous_number):
                return False
            if i.isdigit():
                has_previous_number = True
            # no letters between numbers
            if i.isalpha() and has_previous_number == True:
                return False
        return True

    return False

main()
