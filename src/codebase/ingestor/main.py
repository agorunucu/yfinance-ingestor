import yfinance as yf
import pandas as pd
from pandas_datareader import data


def main():
    pd.options.display.max_columns = None
    tickers = yf.Tickers("MSFT VOD.L GOOGL")

    print(prepare_info(tickers.tickers))
    print(prepare_history(tickers.tickers))
    print(data.get_quote_yahoo(tickers.tickers))
    print(prepare_dividends(tickers.tickers))
    print(prepare_earnings(tickers.tickers))


# Profile (description, sector, etc.)
def prepare_info(tickers):
    all_info = []
    for ticker_name in tickers:
        tickers[ticker_name].info["ticker"] = ticker_name
        all_info.append(tickers[ticker_name].info)
    return pd.DataFrame(all_info)


# Price data for the past 5 years (open, close, low, high, volume)
def prepare_history(tickers):
    all_history = []
    for ticker_name in tickers:
        # Daily basis data for the past N years
        history = tickers[ticker_name].history(period="5y")
        history["ticker"] = ticker_name
        all_history.append(history)
    return pd.concat(all_history)


# Price data for the past 5 years (open, close, low, high, volume)
def prepare_dividends(tickers):
    all_dividends = []
    for ticker_name in tickers:
        dividends = tickers[ticker_name].dividends.to_frame()
        dividends["ticker"] = ticker_name
        all_dividends.append(dividends)
    return pd.concat(all_dividends)


# Earnings related data (e.g. earnings date, revenue)
def prepare_earnings(tickers):
    all_earnings = []
    for ticker_name in tickers:
        earnings = tickers[ticker_name].earnings
        earnings["ticker"] = ticker_name
        all_earnings.append(earnings)
    return pd.concat(all_earnings)


if __name__ == '__main__':
    main()
