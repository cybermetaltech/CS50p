# meal

# prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time
# If it’s not time for a meal, don’t output anything at all
# user’s input will be formatted in 24-hour time as #:## or ##:##
# assume that each meal’s time range is inclusive (7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast)


def main():
    hour = input("What time is it? ")
    result = convert(hour)

    # if tree for the answer
    if 7.0 <= result <= 8.0:
        print("breakfast time")
    elif 12.0 <= result <= 13.0:
        print("lunch time")
    elif 18.0 <= result <= 19.0:
        print("dinner time")


def convert(time):
    # converts time str in 24-hour format to the corresponding number of hours as a float : "7:30" > 7.5
    hours, minutes = map(int, time.split(':'))
    result = hours + minutes / 60.0
    return result


if __name__ == "__main__":
    main()
