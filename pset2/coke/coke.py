# coke

# prompts the user to insert a coin, one at a time, each time informing the user of the amount due
# Once the user has inputted at least 50 cents, output how many cents in change the user is owed


amount = 0
total = 50

while amount < total:
    print(f"Amount Due: {total - amount}")
    user = int(input("Insert Coin: ").strip())

    # check the coins (5, 10 or 25)
    if user == 5 or user == 10 or user == 25:
        amount += user

# print the positive changed owed (if any)
print(f"Change Owed: {amount - total}")
