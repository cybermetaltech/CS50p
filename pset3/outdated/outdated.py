# outdated

# prompts the user for a date, anno Domini, in month-day-year order
#   -9/8/1636 or September 8, 1636
# output that same date in YYYY-MM-DD format
# if input is not a valid date in either format, prompt the user again
# assuming that every month has no more than 31 days

months = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}


while True:
    user = input("Date: ").strip().title()

    # numrical month
    if '/' in user:
        # check the input
        date = user.split('/')

        # check if the month is in text form
        try:
            month = int(date[0])
        except ValueError:
            print("Invalid month. Please enter a valid date.")
            continue

        # check if month is digit
        if date[0].isdigit:
            date[0] = int(date[0])
            date[1] = int(date[1])

            if (1 <= date[0] <= 12) and (1 <= date[1] <= 31):
                # reverse the input
                new_date = date[::-1]

                # month and day back to str
                new_date[-1] = str(new_date[-1]).zfill(2)
                new_date[-2] = str(new_date[-2]).zfill(2)

                # add any missing 0 for the clean output
                new_date[0] = str(new_date[0].zfill(2))
                new_date[1] = str(new_date[1].zfill(2))

                # swap positions of day and month
                new_date[1], new_date[2] = new_date[2], new_date[1]

                # output the result
                result = '-'.join(new_date)
                print(result)
                break
            else:
                user = input("Date: ")


    # month word
    elif ',' in user:
        # make the input a list to work with
        date_lst = user.split(' ')

        # check if the day is entered before the month
        try:
            day = int(date_lst[1].replace(',', ''))
        except ValueError:
            continue

        # check if the day is between 1 and 31
        if 1 <= day <= 31:
            # format the date
            year = date_lst[2]
            day = str(day)
            day = day.zfill(2)
            # loop through the dictionnary to verify the input
            for k, v in months.items():
                if v == date_lst[0]:
                    print(f"{year}-{k}-{day}")
            break
