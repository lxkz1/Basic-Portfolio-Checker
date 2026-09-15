# Portfolio Tracker (Python)

A command-line program that answers "how are my stocks doing right now?" without manually checking each one. The user tells it what they own — ticker symbol, shares held, and price paid per share — and it pulls live prices from Yahoo Finance to calculate current value, gain/loss in dollars, and gain/loss as a percentage, for each holding and for the portfolio as a whole.

## How it works technically

It uses the [yfinance](https://pypi.org/project/yfinance/) library (a free, no-API-key wrapper around Yahoo Finance data) to fetch each stock's current price via `Ticker(symbol).info['regularMarketPrice']`. Since that call fails with a `KeyError` on invalid tickers, input is validated in a retry loop so a typo doesn't crash the program — the user just gets prompted again until they enter something real.

## Current state

Ticker input and price-fetching are working, including the error-handling loop for bad tickers. That's the hardest, most failure-prone piece, and it's solid.

## Still to build

- Collecting shares owned and price paid (as numbers, not just the ticker) for each holding
- Looping so the user can enter multiple stocks instead of just one
- The actual math (current value, gain/loss $ and %)
- A clean display of each position plus a portfolio total
- Polish: better formatting, maybe saving/loading holdings from a file instead of retyping them each run

## Design choices

Functions over a class for now (dicts for holding data), since that matches where the author is at with Python and keeps the API-and-math debugging separate from learning OOP — refactoring into a class later, once it all works, is on the table as a stretch goal.

## Usage

```bash
pip install -r requirements.txt
python yfinance_API_Project.py
```

You'll be prompted to enter a ticker symbol (e.g. `AAPL`). Invalid symbols will prompt you to try again.
