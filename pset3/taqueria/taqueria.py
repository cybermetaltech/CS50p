# taqueria

# enables a user to place an order
# prompting for items, one per line, until the user inputs control-d (catching EOFError)
# display the total cost of all items inputted thus far, prefixed with a dollar sign with 2 decimals
# Treat the user’s input case insensitively. Ignore any input that isn’t an item.
# Assume that every item on the menu will be titlecased.

items = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# initialize the total
total = 0

while True:
    try:
        # get the user input and calculate the total
        user = input("Item: ").strip().title()

        total += items[user]
        print(f"Total: ${total:.2f}")

    except KeyError:
        # if the item is not in the list
        print("Invalid item. Please try again.")

    except EOFError:
        # end the program with ctrl+d
        print()
        break

