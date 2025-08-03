import requests

def convert_currency(amount, from_currency, to_currency):
    """

    Convert an amount from one currency to another using an online API (exchangerate-api.com).
    
    """

    # API endpoint for exchange rates
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"

    # Fetch the exchange rates
    try:
        response = requests.get(api_url)
        data = response.json()
        rates = data.get("rates", {})

        # Check if the target currency is in the rates
        if to_currency in rates:
            # Convert the amount
            converted_amount = amount * rates[to_currency]
            return converted_amount

        else:
            print(f"Error: {to_currency} is not a valid currency.")
            return None
        
    
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None
