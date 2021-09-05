import yfinance as yf
import pandas as pd
from pandas_datareader import data


def main():
    pd.options.display.max_columns = None
    tickers = yf.Tickers("MSFT VOD.L GOOGL")

    print(prepare_info(tickers.tickers))
    # Price data for the past 5 years (open, close, low, high, volume) / Daily basis for last 5 years
    # print(tickers.tickers["GOOGL"].history(period="5y"))
    # Financial indicators (market cap, EPS, P/E ratio, etc)
    # print(data.get_quote_yahoo(tickers.tickers))
    # Dividend related data (e.g. dividend date, yield)
    # print(tickers.tickers["MSFT"].dividends)
    # Earnings related data (e.g. earnings date, revenue)
    # print(tickers.tickers["GOOGL"].earnings)


# Profile (description, sector, etc.)
def prepare_info(tickers):
    all_info = []
    for ticker_name in tickers:
        tickers[ticker_name].info["ticker"] = ticker_name
        all_info.append(tickers[ticker_name].info)
    return pd.DataFrame(all_info)


if __name__ == '__main__':
    main()
