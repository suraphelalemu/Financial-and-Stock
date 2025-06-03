import pandas as pd
import matplotlib.pyplot as plt

def load_data(stock):
    # Example: Load stock data (you can replace this with your data source)
    # For demonstration, let's create a dummy DataFrame
    dates = pd.date_range(start='2022-01-01', periods=100)
    prices = pd.Series(range(100), index=dates)
    return pd.DataFrame({'Date': dates, 'Close': prices})

def plot_stock_data(stock, df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Date'], df['Close'], label='Close Price')
    plt.title(f"{stock} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.show()

def plot_rsi(stock, df):
    # Placeholder for RSI plotting
    pass

def plot_macd(stock, df):
    # Placeholder for MACD plotting
    pass