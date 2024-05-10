# interpreter

# prompts the user for an arithmetic expression
# then calculates and outputs the result as a floating-point value
# Assume that the user’s input will be formatted as x y z
# with one space between x and y and one space between y and z, wherein: x is an integer | y is +, -, *, or / | z is an integer
# Assume that, if y is /, then z will not be 0.


user = input("Expression: ").lower().strip()

data = user.split(" ")
x = float(data[0])
y = data[1]
z = float(data[2])


if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/" and z != 0:
    print(x / z)
