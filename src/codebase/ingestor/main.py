import yfinance as yf
import pandas as pd
from pandas_datareader import data
from helper import destination


def main():
    pd.options.display.max_columns = None
    tickers = yf.Tickers("MSFT VOD.L GOOGL")

    destination.save(prepare_info(tickers.tickers), "yfinance_info")
    destination.save(prepare_history(tickers.tickers), "yfinance_history")
    destination.save(data.get_quote_yahoo(tickers.tickers), "yfinance_indicator")
    destination.save(prepare_dividends(tickers.tickers), "yfinance_dividend")
    destination.save(prepare_earnings(tickers.tickers), "yfinance_earning")


# Profile (description, sector, etc.)
def prepare_info(tickers):
    all_info = []
    for ticker_name in tickers:
        tickers[ticker_name].info["ticker"] = ticker_name
        all_info.append(tickers[ticker_name].info)
    return pd.DataFrame(all_info)[["shortName", "longName", "sector", "fullTimeEmployees",
                                   "longBusinessSummary", "city", "state", "country", "website"]]


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
