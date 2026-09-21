# Portfolio Checker (Python)

A command-line program that answers "what is my portfolio worth right now?" without manually checking each stock. The user tells it how many stocks they own, then the ticker symbol and number of shares for each one. It pulls live prices from Yahoo Finance and prints the total current value of all holdings.

## How it works technically

It uses the [yfinance](https://pypi.org/project/yfinance/) library (a free, no-API-key wrapper around Yahoo Finance data) to fetch each stock's current price via `Ticker(symbol).info['regularMarketPrice']`. Since that call fails with a `KeyError` on invalid tickers, input is validated in a retry loop so a typo doesn't crash the program — the user just gets prompted again until they enter something real.

## Current state

Working: entering any number of holdings, live price lookup with retry on bad tickers, validation that share counts are greater than 0, and a total portfolio value.

Not built yet: price paid per share and gain/loss calculations, a per-holding breakdown, and saving/loading holdings between runs.

## Example session

Prices below are illustrative; the program fetches the live price each time you run it.

```
Welcome to the Stock Value Calculator!
This program will calculate the current value of your portfolio/stock holdings based on the ticker symbol and number of shares you own.
How many stocks do u own inside your portfolio? 2
Please Input the Ticker symbol you own: aapl
Please Input the amount of shares you own of this stock?: 10
Please Input the Ticker symbol you own: msft
Please Input the amount of shares you own of this stock?: 2.5
The current value of your all of your shares of is: $2856.25
```

## Things worth knowing

- **Input is forgiving where it matters:** tickers are trimmed and uppercased, so ` aapl ` works as `AAPL`. Fractional shares (e.g. `2.5`) are accepted, and a share count of 0 or less asks again.
- **Prices are not guaranteed real-time.** The value comes from Yahoo Finance's `regularMarketPrice`, which can be delayed depending on the exchange.
- **Needs an internet connection** on every run, since nothing is cached or saved between runs.
- **Total is labelled in `$`, but no currency conversion is done.** Tickers listed on non-US exchanges are priced in their local currency, so mixing them can give a misleading total.
- **Non-numeric input for the stock count** exits the program with a message. A non-numeric share count is not handled yet and will raise an error.

## Design choices

Functions over a class for now (dicts for holding data), since that matches where the author is at with Python and keeps the API-and-math debugging separate from learning OOP — refactoring into a class later, once it all works, is on the table as a stretch goal.

## Usage

```bash
pip install -r requirements.txt
python yfinance_API_Project.py
```

Enter how many different stocks you hold, then for each one its ticker symbol (e.g. `AAPL`) and the number of shares. Invalid ticker symbols will prompt you to try again.
