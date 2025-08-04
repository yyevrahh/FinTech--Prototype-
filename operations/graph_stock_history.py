import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib
import os
matplotlib.use('Agg')  # Use non-interactive because it's for saving images

def get_stock_history(ticker):
    """
    Fetch the stock history for a given ticker symbol and save as an image.
    
    PARAM: ticker: The stock ticker symbol (e.g., 'AAPL', 'GOOGL').
    RETURN: Saves the stock history graph for the past month as a PNG file or None if an error occurs.
    """
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period='1mo')  # Fetching 1 month of data for better visualization

        if not data.empty:
            data.reset_index(inplace=True)
            plt.figure(figsize=(12, 6))
            plt.plot(data['Date'], data['Close'], marker='o')
            plt.title(f"Stock Price History for {ticker} (Last 30 Days)")
            plt.xlabel("Date")
            plt.ylabel("Closing Price (PHP)")
            plt.xticks(rotation=45)
            plt.grid()
            plt.tight_layout()
            
            # Save plot as an image file in the "saved graphs" folder
            save_dir = "saved graphs"
            os.makedirs(save_dir, exist_ok=True)
            filename = os.path.join(save_dir, f"{ticker}_stock_history.png")
            plt.savefig(filename, dpi=300, bbox_inches='tight')
            print(f"\nGraph saved as '{filename}'.")
            plt.close() # Close plot to free memory
            
        else:
            print(f"No data found for ticker: {ticker}")
            return None

    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None
