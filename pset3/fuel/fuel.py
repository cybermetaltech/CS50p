# fuel

# prompts the user for a fraction, formatted as X/Y
# outputs, as a percentage rounded to the nearest integer
# if 1% or less remains, output E
# if 99% or more remains, output F
# X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again
# catch any exceptions like ValueError or ZeroDivisionError


from fractions import Fraction

while True:
    user = input("Fraction: ").strip()

    try:
        fraction = Fraction(user)
        result = round(fraction.numerator / fraction.denominator * 100)

        # check if numerator > denominator
        if fraction.numerator > fraction.denominator:
            raise ValueError

        # output the result
        if result == 0 or result == 1:
            print("E")
        elif result == 99 or result == 100:
            print("F")
        else:
            print(f"{result}%")

    except ValueError:
        print("Enter a valid fraction")

    except ZeroDivisionError:
        print("Cannot divide by 0")

    else:
        break
