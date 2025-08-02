# This section imports the different files required to run the whole program.
from crypto_current import get_crypto_current

# Keeps the program running
while True:
    """
        The user will select between four (4) different FinTech operations.
        Input will be processed correspondent to what operation incorporates their choice.
    """
    print("Choose an operation:")
    print("[1] Get current cryptocurrency price")
    print("[2] Exit")
    choice = input("Enter your choice: ")

    #Conditional for choice 1 (Get current cryptocurrency price)
    if choice == '1':
        print("\nSelect a cryptocurrency:\n\t[1] Bitcoin (BTC)\n\t[2] Ethereum (ETH)\n\t[3] Dogecoin (DOGE)\n\t[4] Ripple (XRP)")
        crypto_choice = input("Enter your choice: ")
        crypto_symbols = {
            '1': 'BTC',
            '2': 'ETH',
            '3': 'DOGE',
            '4': 'XRP'
        }
        if crypto_choice in crypto_symbols:
            crypto_symbol = crypto_symbols[crypto_choice]
            prices = get_crypto_current(crypto_symbol)
            if prices:
                print(f"\nCurrent price of {crypto_symbol}:")
                print(f"\tPHP: ₱{prices['PHP']}")
                print(f"\tUSD: ${prices['USD']}")
            else:
                print("Failed to retrieve prices.")
                print("Please try again later.")
        else:
            print("Invalid choice. Please select a valid cryptocurrency.")
    elif choice == '2':
        print("\nExiting the program. Goodbye!")
        break
        