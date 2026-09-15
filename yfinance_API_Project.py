import yfinance


def main():
    usersstockvalue = getuserstockvalue()
    sv = StockValueData(usersstockvalue)
    print(f"The current stock value of {usersstockvalue} is: ${sv}")

def getuserstockvalue():
    return input("Please Input the Ticker symbol you own: ")
    


def StockValueData(userdata):
    try: 
        data = yfinance.Ticker(userdata).info
        return data['regularMarketPrice']
    except KeyError:
        while True: 
            print("Invalid Ticker Symbol. Please try again.")
            userdata = getuserstockvalue()
            try:
                data = yfinance.Ticker(userdata).info
                return data['regularMarketPrice']
            except KeyError:
                continue


if __name__ == "__main__":
    main()