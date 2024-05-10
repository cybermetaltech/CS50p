# grocery

# prompts the user for items, one per line, until the user inputs control-d
# output the user’s grocery list
#   -all uppercase
#   -sorted alphabeticaly
#   -prefixing each line with the number of times the user inputted that item
# case insensitive


items_count= {}

while True:
    try:
        item = input()

        if item in items_count:
            items_count[item] += 1
        else:
            items_count[item] = 1

    except EOFError:
        # sort the names alphabetically
        for item in sorted(items_count.keys()):
            count = items_count[item]
            print(f"{count} {item.upper()}")
        break