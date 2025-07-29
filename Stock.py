stock_prices = {"AAPL": 220, "TSLA": 250, "GOOGL": 300, "MSFT": 350}
n = int(input("Enter no of different types of stocks you own: "))
portfolio = {}
for _ in range(n):
    stock = input("Enter stock symbol you own: ").upper()
    quantity = int(input(f"Enter quantity of {stock}: "))
    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print(f"{stock} is not in the stock price list. Skipping.")

total_investment = 0
print("Investment Breakdowm")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
print(f"\nTotal investment value: {total_investment}")
