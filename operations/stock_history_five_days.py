import yfinance as yf

def get_stock(ticker):
    """
    Fetch the stock (past 5 days) for a given ticker symbol.
    
    PARAM: ticker: The stock ticker symbol (e.g., 'AAPL', 'GOOGL').
    RETURN: The past 5 days stock for a Ticker or None if an error occurs.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period='5d')
        records = data.reset_index().to_dict('records')

        if not data.empty:
            for record in records:
                print(
                    f"\033[1;37m{record['Date'].date()}\033[0m | "
                    f"\033[1;34mOpen: {record['Open']:.2f}\033[0m | "
                    f"\033[1;32mHigh: {record['High']:.2f}\033[0m | "
                    f"\033[1;31mLow: {record['Low']:.2f}\033[0m | "
                    f"\033[1;33mClose: {record['Close']:.2f}\033[0m | "
                    f"\033[1;35mVolume: {int(record['Volume'])}\033[0m | "
                    f"\033[1;36mDividends: {record['Dividends']}\033[0m"
                )

        else:
            print(f"No data found for ticker: {ticker}")
            return None
        
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
 