import cryptocompare as crypto_c

def get_crypto_current(crypto_symbol):
    """

    Fetch the current price of a cryptocurrency from:
    param: crypto_symbol: The symbol of the cryptocurrency (e.g., 'BTC', 'ETH').
    return: The current price of the cryptocurrency in PHP and USD.

    """
    try:
        # Fetch Philippine pesos price from given cryptocurrency symbol
        pesos_price = crypto_c.get_price(crypto_symbol, currency='PHP')
        # For US dollars
        usd_price = crypto_c.get_price(crypto_symbol, currency='USD')
        
        #Return the fetched prices in dictionary format
        return {
            'PHP': pesos_price[crypto_symbol]['PHP'],
            'USD': usd_price[crypto_symbol]['USD']
        }
    except Exception as e:
        print(f"Error fetching data for {crypto_symbol}: {e}")
        return None