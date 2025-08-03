# This section imports the different files required to run the whole program.
from operations.crypto_current import get_crypto_current
from operations.forex_convert import convert_currency
import time as t

# Keeps the program running
while True:
    """

    The user will select between four (4) different FinTech operations.
    Input will be processed correspondent to what operation incorporates their choice.

    """
    t.sleep(.5)
    print("\nChoose an operation:")
    print("\t\033[93m[1]\033[0m Get current cryptocurrency price")
    print("\t\033[93m[2]\033[0m Convert amount from Forex currency rates")
    print("\t\033[93m[3]\033[0m Exit")
    choice = input("Enter your choice: ")

    #Conditional for choice 1 (Get current cryptocurrency price)
    if choice == '1':
        # User selects a cryptocurrency to get the current price
        print("\n\033[91mCryptocurrency Price Checker\033[0m")
        print("Select a cryptocurrency:")
        print("\t\033[93m[1]\033[0m Bitcoin (BTC)")
        print("\t\033[93m[2]\033[0m Ethereum (ETH)")
        print("\t\033[93m[3]\033[0m Dogecoin (DOGE)")
        print("\t\033[93m[4]\033[0m Ripple (XRP)")
        crypto_choice = input("Enter your choice: ")

        # Dictionary to map user input to cryptocurrency symbols
        crypto_symbols = {
            '1': 'BTC',
            '2': 'ETH',
            '3': 'DOGE',
            '4': 'XRP'
        }
        # Check if the user's choice is valid
        if crypto_choice in crypto_symbols:
            # Get the current price of the selected cryptocurrency
            crypto_symbol = crypto_symbols[crypto_choice]
            prices = get_crypto_current(crypto_symbol)

            # If prices are successfully retrieved, it will display them
            # Otherwise, it displays an error message
            if prices:
                print(f"\nCurrent price of \033[93m{crypto_symbol}:\033[0m")
                print(f"\033[92m\tPHP: ₱{prices['PHP']}")
                print(f"\tUSD: ${prices['USD']}\033[0m")

            else:
                print("Failed to retrieve prices.")
                print("Please try again later.")

    # Conditional for choice 2 (Convert amount from Forex currency rates)
    elif choice == '2':
        # User inputs the amount they want to convert
        print("\n\033[91mForex Currency Converter\033[0m")
        amount = input("How much do you want to convert: ")

        # User selects the currency to convert from and to
        print("\nSelect a currency to convert \033[95mFROM\033[0m:")
        print("\t\033[93m[1]\033[0m Philippine Peso (PHP)")
        print("\t\033[93m[2]\033[0m US Dollar (USD)")
        print("\t\033[93m[3]\033[0m Euro (EUR)")
        print("\t\033[93m[4]\033[0m British Pound (GBP)")
        print("\t\033[93m[5]\033[0m Japanese Yen (JPY)")
        print("\t\033[93m[6]\033[0m Australian Dollar (AUD)")

        from_currency_choice = input("Enter your choice: ")

        print("\nSelect a currency to convert \033[94mTO\033[0m:")
        print("\t\033[93m[1]\033[0m Philippine Peso (PHP)")
        print("\t\033[93m[2]\033[0m US Dollar (USD)")
        print("\t\033[93m[3]\033[0m Euro (EUR)")
        print("\t\033[93m[4]\033[0m British Pound (GBP)")
        print("\t\033[93m[5]\033[0m Japanese Yen (JPY)")
        print("\t\033[93m[6]\033[0m Australian Dollar (AUD)")

        to_currency_choice = input("Enter your choice: ")

        # Dictionary to map user input to currency codes
        currency_symbols = {
            '1': 'PHP',
            '2': 'USD',
            '3': 'EUR',
            '4': 'GBP',
            '5': 'JPY',
            '6': 'AUD'
        }

        # Check if the user's choices are valid
        if from_currency_choice in currency_symbols and to_currency_choice in currency_symbols:
            # Get the currency codes based on user input
            from_currency = currency_symbols[from_currency_choice]
            to_currency = currency_symbols[to_currency_choice]

            converted_amount = convert_currency(float(amount), from_currency, to_currency)

            # If conversion is successful, it will display the converted amount
            # Otherwise, it displays an error message
            if converted_amount is not None:
                print(f"\nConverted \033[95m{amount} {from_currency}\033[0m to {to_currency}: \033[94m{converted_amount:.2f} {to_currency}\033[0m")
            else:
                print("Conversion failed. Please try again later.")
        

    elif choice == '3':
        print("\nExiting the program. Goodbye!")
        break

    else:
            print("Invalid choice. Please select a valid cryptocurrency.")
    
        