# tip

# implement function: dollars_to_float
#   -str as input (formatted as $##.##, wherein each # is a decimal digit)
#   -remove the leading $, and return the amount as a float.
#   -For instance, given $50.00 as input, it should return 50.0.
# implement function: percent_to_float
#   -str as input (formatted as ##%, wherein each # is a decimal digit)
#   -remove the trailing %, and return the percentage as a float.
#   -For instance, given 15% as input, it should return 0.15.


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d = d.strip("$")
    d = float(d)
    d = round(d, 1)
    return d


def percent_to_float(p):
    p = p.strip("%")
    p = float(p)
    p = p / 100
    return p


main()
