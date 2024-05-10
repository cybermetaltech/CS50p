##### BITCOIN #####

"""
-Expects the user to specify as a command-line argument the number of Bitcoins, they would like to buy.
If that argument cannot be converted to a float:
    -the program should exit via sys.exit with an error message.
-Queries the API for the CoinDesk Bitcoin Price Index:
    -https://api.coindesk.com/v1/bpi/currentprice.json
    -which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float.
-Be sure to catch any exceptions.
"""

import requests
import sys

def main():
    try:
        if len(sys.argv) < 2:
            sys.exit("Missing command-line argument")

        x = float(sys.argv[1])

        # get the actual value of bitcoin
        bitcoin_price = get_bitcoin_price()

        if bitcoin_price is not None:
            result = x * bitcoin_price
            print(f'${result:,.4f}')
        else:
            print("Unable to retrieve Bitcoin price.")

    except ValueError:
        sys.exit("Command-line argument is not a number")

def get_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # HTTP error for bad response
        data = response.json()

        # Check if the request was successful
        if response.status_code == 200:
            return data['bpi']['USD']['rate_float']
        else:
            print(f"Error: {data['error']['type']}")
            return None

    except requests.RequestException:
        print("An error occurred while making the request. Please try again later.")
        return None

if __name__ == "__main__":
    main()
