import urllib.request
import json

def convert_currency(amount, from_currency, to_currency):
    """
    Convert an amount from one currency to another using an online API.
    """
    api_url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    try:
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read())
            rates = data.get("rates", {})
            if to_currency in rates:
                converted_amount = amount * rates[to_currency]
                return converted_amount
            else:
                print(f"Error: {to_currency} is not a valid currency.")
                return None
    except Exception as e:
        print(f"Error fetching exchange rates: {e}")
        return None