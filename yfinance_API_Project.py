import yfinance
import sys

def main():
    print("Welcome to the Stock Value Calculator!")
    print("This program will calculate the current value of your portfolio/stock holdings based on the ticker symbol and number of shares you own.")
    try:
        numberofstocks = int(input("How many stocks do u own inside your portfolio? "))
    except ValueError:
        sys.exit("We are sorry but it seems like your portfolio has 0 stocks as you have answered 0")
    else:
        n = 0 
        for _ in range(numberofstocks):
            ticker, shares = get_user_stock_value()
            price = get_stock_price(ticker)
            total_value = price * shares
            n += total_value
        print(f"The current value of your all of your shares of is: ${n:.2f}")


def get_user_stock_value():
    ticker = input("Please Input the Ticker symbol you own: ").strip().upper()
    shares = get_share_amount()
    return ticker, shares


def get_share_amount():
    while True:
        shares = float(input("Please Input the amount of shares you own of this stock?: "))
        if shares > 0:
            return shares
        else:
            print("Please enter a valid number of shares greater than 0.")
            return get_share_amount()



def get_stock_price(ticker):
    while True:
        try:
            data = yfinance.Ticker(ticker).info
            return data["regularMarketPrice"]
        except KeyError:
            print("Invalid Ticker Symbol. Please try again.")
            ticker = input("Please Input the Ticker symbol you own: ").strip().upper()


if __name__ == "__main__":
    main()
