import yfinance as yf
import pandas as pd
from pandas_datareader import data


def main():
    pd.options.display.max_columns = None
    msft = yf.Tickers("MSFT VOD.L GOOGL")

    # Profile (description, sector, etc.)
    print(msft.tickers["GOOGL"].info)
    # Price data for the past 5 years (open, close, low, high, volume) / Daily basis for last 5 years
    print(msft.tickers["GOOGL"].history(period="5y"))
    # Financial indicators (market cap, EPS, P/E ratio, etc)
    print(data.get_quote_yahoo(msft.tickers))
    # Dividend related data (e.g. dividend date, yield)
    print(msft.tickers["MSFT"].dividends)
    # Earnings related data (e.g. earnings date, revenue)
    print(msft.tickers["GOOGL"].earnings)


if __name__ == '__main__':
    main()
